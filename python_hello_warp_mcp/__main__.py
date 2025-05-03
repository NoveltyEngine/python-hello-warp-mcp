#!/usr/bin/env python
# python_hello_warp_mcp/__main__.py
"""
Command-line entry point for the Hello World MCP server.
This allows the server to be run as:
  python -m python_hello_warp_mcp
"""

from python_hello_warp_mcp.server import run_server

def main():
    # Run the server with stdio transport
    run_server()

if __name__ == "__main__":
    main()
