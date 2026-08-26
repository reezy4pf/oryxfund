#!/usr/bin/env python3
"""
Oryx Fund Static Page Generator Wrapper
Delegates to build_clean_isolated_system.py
"""
import sys
import os

from build_clean_isolated_system import generate_all

if __name__ == "__main__":
    generate_all()
