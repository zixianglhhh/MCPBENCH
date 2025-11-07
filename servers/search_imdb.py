from mcp.server.fastmcp import FastMCP
mcp = FastMCP('search_imdb')

@mcp.tool()
def search_imdb(primary_title) -> str:
    '''"""
Search for movies and TV shows using their titles.

Args:
    primary_title (str): The exact title of the movie or TV show to search for. 

Returns:
    str: A formatted string containing the title, genre, subtitle availability, 
    and IMDb ID if a match is found. If no match is found, returns a message 
    indicating that no results were found for the given title.
"""'''
    imdb_database = [{'title': 'Hotel Mumbai', 'genre': 'Suspense', 'subtitles': True, 'imdb_id': 'tt5461944'}, {'title': 'JT Leroy', 'genre': 'Non-fiction', 'subtitles': False, 'imdb_id': 'tt5460522'}, {'title': 'Captain Marvel', 'genre': 'Adventure', 'subtitles': True, 'imdb_id': 'tt4154664'}, {'title': 'Mad Max', 'genre': 'Fantasy', 'subtitles': True, 'imdb_id': 'tt1392190'}, {'title': 'Dogman', 'genre': 'Drama', 'subtitles': False, 'imdb_id': 'tt6768578'}, {'title': 'Say Anything', 'genre': 'Romance', 'subtitles': False, 'imdb_id': 'tt0098258'}, {'title': 'Alice in Wonderland', 'genre': 'Fantasy', 'subtitles': True, 'imdb_id': 'tt1014759'}, {'title': 'Hackers', 'genre': 'Drama', 'subtitles': True, 'imdb_id': 'tt0113243'}, {'title': 'Dr. Strangelove', 'genre': 'Comedy', 'subtitles': False, 'imdb_id': 'tt0057012'}, {'title': 'Hellboy', 'genre': 'Fantasy', 'subtitles': True, 'imdb_id': 'tt2274648'}, {'title': 'The Poseidon Adventure', 'genre': 'Adventure', 'subtitles': False, 'imdb_id': 'tt0069113'}]
    search_results = [entry for entry in imdb_database if entry['title'].lower() == primary_title.lower()]
    if not search_results:
        return f"No results found for the title '{primary_title}'. Please check the title and try again."
    result = search_results[0]
    response = f"Title: {result['title']}\nGenre: {result['genre']}\nSubtitles available: {('Yes' if result['subtitles'] else 'No')}\nIMDb ID: {result['imdb_id']}"
    return response
if __name__ == '__main__':
    mcp.run(transport='stdio')