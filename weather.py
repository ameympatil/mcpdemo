from mcp.server.fastmcp import FastMCP

mcp = FastMCP('Weather')

@mcp.tool()
async def get_weather(location:str)->str:
    """
    Gets the weather of the location.
    """
    return f"It's raining now in Mumbai."

if __name__ == "__main__":
    mcp.run(transport = "streamable-http")