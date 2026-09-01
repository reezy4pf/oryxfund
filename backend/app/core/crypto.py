"""
ORYX FUND — FIELD-LEVEL ENVELOPE ENCRYPTION ENGINE (backend/app/core/crypto.py)
Implements AES-256-GCM field-level envelope encryption with dynamic Data Encryption Keys (DEKs)
and context authentication (KDPA 2019 / CBK Cybersecurity Guidelines compliant).
"""

import os
import json
import base64
from typing import Optional
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class EnvelopeEncryptionEngine:
    """
    AES-256-GCM Envelope Encryption Engine.
    In production AWS environments, the Master Key is managed by AWS KMS (CMK).
    For standalone operation, a 256-bit Key Encryption Key (KEK) is derived from system secrets.
    """
    def __init__(self, master_kek_bytes: Optional[bytes] = None):
        # 256-bit Key Encryption Key (KEK)
        self.master_kek = master_kek_bytes or os.environ.get(
            "ORYX_MASTER_KEK", 
            "oryx_fund_2026_master_kek_32_bytes_len__"
        ).encode("utf-8")[:32].ljust(32, b"0")

    def encrypt_field(self, plaintext_value: str, context_identifier: str) -> Optional[str]:
        """
        Encrypts a sensitive PII field using a dynamic Data Encryption Key (DEK).
        Returns a base64 encoded string:
        [Encrypted DEK Length (2B)] + [Encrypted DEK] + [IV (12B)] + [Ciphertext + Tag]
        """
        if plaintext_value is None:
            return None

        encryption_context = {
            "origin": "oryx_fund_core",
            "entity_id": context_identifier,
            "compliance": "KDPA_2019"
        }
        context_bytes = json.dumps(encryption_context, sort_keys=True).encode("utf-8")

        # 1. Generate ephemeral 256-bit Data Encryption Key (DEK)
        plaintext_dek = AESGCM.generate_key(bit_length=256)

        # 2. Wrap (encrypt) the DEK using the Master KEK
        kek_aesgcm = AESGCM(self.master_kek)
        dek_iv = os.urandom(12)
        encrypted_dek = kek_aesgcm.encrypt(dek_iv, plaintext_dek, context_bytes)
        wrapped_dek_payload = dek_iv + encrypted_dek

        # 3. Encrypt the actual sensitive field using the ephemeral DEK
        dek_aesgcm = AESGCM(plaintext_dek)
        payload_iv = os.urandom(12)
        ciphertext = dek_aesgcm.encrypt(payload_iv, plaintext_value.encode("utf-8"), context_bytes)

        # 4. Assemble composite serial envelope
        dek_len = len(wrapped_dek_payload).to_bytes(2, byteorder="big")
        composite_payload = dek_len + wrapped_dek_payload + payload_iv + ciphertext

        # Memory hygiene: delete plaintext DEK reference
        del plaintext_dek

        return base64.b64encode(composite_payload).decode("utf-8")

    def decrypt_field(self, encrypted_payload_b64: str, context_identifier: str) -> Optional[str]:
        """
        Unwraps DEK and decrypts the field ciphertext with integrity authentication.
        """
        if encrypted_payload_b64 is None:
            return None

        composite_payload = base64.b64decode(encrypted_payload_b64.encode("utf-8"))

        encryption_context = {
            "origin": "oryx_fund_core",
            "entity_id": context_identifier,
            "compliance": "KDPA_2019"
        }
        context_bytes = json.dumps(encryption_context, sort_keys=True).encode("utf-8")

        # 1. Parse envelope lengths
        dek_len = int.from_bytes(composite_payload[0:2], byteorder="big")
        wrapped_dek_payload = composite_payload[2 : 2 + dek_len]
        dek_iv = wrapped_dek_payload[0:12]
        encrypted_dek = wrapped_dek_payload[12:]

        offset = 2 + dek_len
        payload_iv = composite_payload[offset : offset + 12]
        ciphertext = composite_payload[offset + 12 :]

        # 2. Unwrap DEK using Master KEK
        kek_aesgcm = AESGCM(self.master_kek)
        plaintext_dek = kek_aesgcm.decrypt(dek_iv, encrypted_dek, context_bytes)

        # 3. Decrypt field ciphertext using DEK
        dek_aesgcm = AESGCM(plaintext_dek)
        decrypted_bytes = dek_aesgcm.decrypt(payload_iv, ciphertext, context_bytes)

        del plaintext_dek
        return decrypted_bytes.decode("utf-8")

# Singleton instance
crypto_engine = EnvelopeEncryptionEngine()
