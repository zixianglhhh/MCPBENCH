from mcp.server.fastmcp import FastMCP
mcp = FastMCP('get_directors')

@mcp.tool()
def get_directors(imdb_id) -> str:
    '''"""
Retrieve the directors of a movie.

Given a valid IMDb movie identifier, this function returns the name of the movie's director.
If the IMDb ID format is invalid or the movie cannot be found, an error message is returned.

Args:
    imdb_id (str): The IMDb identifier of the movie (e.g., 'tt0113243').

Returns:
    str: A message containing the director's name if found, or an error message if the IMDb ID
    is invalid or the movie is not found.
"""'''
    movie_directors_db = {'tt0098258': 'Cameron Crowe', 'tt0113243': 'Iain Softley', 'tt0057012': 'Stanley Kubrick', 'tt2274648': 'Neil Marshall'}
    if not isinstance(imdb_id, str) or not imdb_id.startswith('tt'):
        return 'Error: Invalid IMDb ID format. Please provide a valid IMDb ID.'
    director = movie_directors_db.get(imdb_id)
    if director:
        return f'The director of the movie with IMDb ID {imdb_id} is {director}.'
    else:
        return 'Error: Movie not found in the database. Please check the IMDb ID and try again.'
if __name__ == '__main__':
    mcp.run(transport='stdio')