from mcp.server.fastmcp import FastMCP
mcp = FastMCP('search_attractions')

@mcp.tool()
def search_attractions(location, date=None) -> str:
    '''"""
    Search for attractions in a specified location and optional date.

    This tool connects to the Attractions MCP Server to find points of interest.
    The `location` parameter is mandatory, while the `date` parameter is optional.

    Args:
        location (str): Name of the city or area to search for attractions.
        date (str, optional): Date in `MM/DD/YYYY` format to filter attractions. Defaults to None.

    Returns:
        str: A list of attractions with details if successful, or an error message if no attractions are found.
    """'''
    attractions_db = {
        'Chicago': [
            {'name': 'Willis Tower', 'address': '233 S Wacker Dr, Chicago, IL', 'description': 'A 110-story skyscraper with a skydeck.'},
            {'name': 'Millennium Park', 'address': '201 E Randolph St, Chicago, IL', 'description': 'A public park with modern art and architecture.'}
        ],
        'New York': [
            {'name': 'Statue of Liberty', 'address': 'Liberty Island, New York, NY', 'description': 'Iconic national monument accessible by ferry.'},
            {'name': 'Central Park', 'address': 'Manhattan, New York, NY', 'description': 'A large public park in the city center.'}
        ]
    }

    if not location:
        return "Error: 'location' is a required parameter."

    if location not in attractions_db:
        return f"Error: No attractions found for location '{location}'."

    attractions = attractions_db[location]
    result = f"Attractions in {location}:\n"
    for attraction in attractions:
        result += f"- {attraction['name']}: {attraction['description']} (Address: {attraction['address']})\n"

    if date:
        result += f"Filtered by date: {date}\n"

    return result

if __name__ == '__main__':
    mcp.run(transport='stdio')