# -*- coding: utf-8 -*-
"""GenPark Bio-Agent CLI."""
import sys
from .server import run_test

def main():
    if "--test" in sys.argv:
        sys.exit(0 if run_test() else 1)
    print("GenPark Bio-Agent v2.0.0 (MCP JSON-RPC 2.0)")
    print("Run with --test to verify, or connect via stdio MCP.")

if __name__ == "__main__":
    main()
