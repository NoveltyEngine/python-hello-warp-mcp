# python_hello_warp_mcp/server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("HelloWorldServer")

# Add a simple greeting tool
@mcp.tool()
def hello(name: str = "World") -> str:
    """Say hello to someone"""
    return f"Hello, {name}!"

# Add a resource that provides information
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}! Welcome to MCP on Warp Terminal."

def run_server(transport: str = "stdio"):
    """Run the MCP server with the specified transport
    
    Args:
        transport: The transport to use (stdio or sse, default: stdio)
    """
    # Run the MCP server directly with the specified transport
    mcp.run(transport=transport)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="MCP Hello World Server")
    parser.add_argument("--transport", choices=["stdio", "sse"], default="stdio",
                      help="Transport mode (stdio or sse, default: stdio)")
    args = parser.parse_args()
    
    # Run the server with the specified transport
    run_server(transport=args.transport)
