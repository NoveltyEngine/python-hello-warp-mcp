# Hello World MCP Server for Warp Terminal

A simple "Hello World" Machine Conversational Protocol (MCP) server implementation for Warp Terminal.

## Quick Start for Warp Terminal

To use this MCP server with Warp Terminal, add this line to your Warp configuration:

```json
{
  "mcp_server_command": "/path/to/your/python -m hello_world_mcp"
}
```

Make sure to replace `/path/to/your/python` with the actual path to your Python interpreter (ideally in a virtual environment).

## Installation

### Development Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/hello_world_mcp.git
cd hello_world_mcp

# Set up virtual environment (if not already created)
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install the package in development mode
uv pip install -e ".[dev]"  # Alternatively: pip install -e ".[dev]"
```

## Usage

### For Warp Terminal Integration

To use with Warp Terminal, run the server with the standard "stdio" transport:

```bash
# Run using stdio transport for Warp Terminal integration (default)
python -m hello_world_mcp

# Or explicitly specify stdio transport
python -m hello_world_mcp --transport stdio
```

This allows Warp Terminal to communicate with your MCP server via standard input and output.

### For HTTP Access (Optional)

For testing or debugging, you can also run the server with the SSE (Server-Sent Events) transport:

```bash
# Run with SSE transport for HTTP access
python -m hello_world_mcp --transport sse
```

## Features

This simple MCP server provides:

1. A `hello` tool that returns a greeting message
2. A `greeting://` resource that provides a personalized greeting

## Project Structure

```
hello_world_mcp/
├── hello_world_mcp/
│   ├── __init__.py
│   ├── __main__.py  # CLI entry point
│   └── server.py    # MCP server implementation
├── README.md
├── LICENSE
├── .gitignore
└── pyproject.toml
```

## License

MIT
