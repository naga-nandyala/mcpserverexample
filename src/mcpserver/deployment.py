from mcp.server.fastmcp import FastMCP


mcp = FastMCP("demo")


@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Adds two numbers together.
    Args:
        a: First number
        b: Second number
    Returns:
        The sum of a and b
    """
    return a + b