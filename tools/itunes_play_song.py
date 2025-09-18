from mcp.server.fastmcp import FastMCP
mcp = FastMCP('itunes_play_song')

@mcp.tool()
def itunes_play_song(song) -> str:
    '''"""
Play a specific song in iTunes using the song title.

Args:
    song (str): The exact title of the song to be played in iTunes.

Returns:
    str: A confirmation message indicating that the specified song is being played.
"""'''
    return f"Playing '{song}' on iTunes."
if __name__ == '__main__':
    mcp.run(transport='stdio')