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

def run_server():
    """Run the MCP server with stdio transport
    
    This function runs the MCP server using the stdio transport,
    which is required for Warp Terminal integration.
    """
    # Run the MCP server directly with stdio transport
    mcp.run(transport="stdio")

if __name__ == "__main__":
    # Run the server with stdio transport
    run_server()
