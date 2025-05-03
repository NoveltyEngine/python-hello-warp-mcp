#!/usr/bin/env python
# python_hello_warp_mcp/__main__.py
"""
Command-line entry point for the Hello World MCP server.
This allows the server to be run as:
  python -m python_hello_warp_mcp [--transport stdio|sse]
"""

import argparse
from python_hello_warp_mcp.server import run_server

def main():
    parser = argparse.ArgumentParser(description="MCP Hello World Server")
    parser.add_argument("--transport", choices=["stdio", "sse"], default="stdio",
                      help="Transport mode (stdio or sse, default: stdio)")
    args = parser.parse_args()
    
    # Run the server with the specified transport
    run_server(transport=args.transport)

if __name__ == "__main__":
    main()
