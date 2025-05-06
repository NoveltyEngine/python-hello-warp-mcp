# Hello World MCP Server for Warp Terminal

A starting point for anyone who wants to create their own MCP server.  It's Warp-specific because I didn't taken the time to make it generic/universal, but it shouldn't take much work to make work for anything.

## Installation

### Development Installation

```bash
# Clone the repository
git clone https://github.com/NoveltyEngine/python-hello-warp-mcp.git
cd python-hello-warp-mcp

# Set up virtual environment (if not already created)
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install the package in development mode
uv pip install -e ".[dev]"  # Alternatively: pip install -e ".[dev]"
```

## Usage

### For Warp Terminal Integration

To use with Warp Terminal, go to the page to create a new MCP server, and enter this in "Command to run":

```bash
/path/to/your/python -m python_hello_warp_mcp
```

This allows Warp Terminal to communicate with your MCP server via standard input and output.

## Features

This simple MCP server provides:

1. A `hello` tool that returns a greeting message
2. A `greeting://` resource that provides a personalized greeting

## License

MIT
