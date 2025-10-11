from mcp.server.fastmcp import FastMCP
mcp = FastMCP('itunes_search')

@mcp.tool()
def itunes_search(artist) -> str:
    '''"""
Search the music library for tracks by a given artist name.

Args:
    artist (str): The exact name of the artist to search for. 

Returns:
    str: A formatted string listing matching tracks in the format 
        "Artist - Title (Album, Genre)" separated by newlines, 
        or an error message if the input is invalid, 
        or a message indicating no matches were found.
"""'''
    mock_itunes_library = [{'artist': 'El Alfa', 'title': 'La Romana', 'album': 'El Hombre', 'genre': 'Latin'}, {'artist': 'Frank Ocean', 'title': 'Nikes', 'album': 'Blonde', 'genre': 'R&B'}, {'artist': 'Karolina Protsenko', 'title': 'Fly', 'album': 'Fly', 'genre': 'Pop'}, {'artist': 'Brunettes Shoot Blondes', 'title': 'Every Monday', 'album': 'Bittersweet', 'genre': 'Rock'}, {'artist': 'Mozart', 'title': 'Eine kleine Nachtmusik', 'album': 'Classical Favorites', 'genre': 'Classical'}, {'artist': 'Adele', 'title': 'Hello', 'album': '25', 'genre': 'Pop'}, {'artist': 'Drake', 'title': 'God\'s Plan', 'album': 'Scorpion', 'genre': 'Hip-Hop'}, {'artist': 'Taylor Swift', 'title': 'Lover', 'album': 'Lover', 'genre': 'Pop'}, {'artist': 'The Weeknd', 'title': 'Blinding Lights', 'album': 'After Hours', 'genre': 'R&B'}, {'artist': 'Billie Eilish', 'title': 'Bad Guy', 'album': 'When We All Fall Asleep, Where Do We Go?', 'genre': 'Pop'}]
    if not isinstance(artist, str) or not artist.strip():
        return 'Error: Invalid input. Please provide a valid search term.'
    artist = artist.strip().lower()
    results = []
    for track in mock_itunes_library:
        if artist == track['artist'].lower():
            results.append(track)
    if results:
        result_strings = [f"{track['artist']} - {track['title']} ({track['album']}, {track['genre']})" for track in results]
        return '\n'.join(result_strings)
    else:
        return 'No tracks found matching your search criteria.'
if __name__ == '__main__':
    mcp.run(transport='stdio')