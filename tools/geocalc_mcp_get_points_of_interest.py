from mcp.server.fastmcp import FastMCP
mcp = FastMCP('geocalc_mcp_get_points_of_interest')

@mcp.tool()
def geocalc_mcp_get_points_of_interest(city, category, radius_km=None,) -> str:
    '''```python
"""
Find points of interest (POIs) near a specified city, optionally filtered by category and search radius.

If no POIs are found within the specified radius, the radius may be increased (default is 10 km).
The category should be a single lowercase word (hyphenated words like "child-friendly" count as one word).
If no category is specified, the default category is "general".

The `city` parameter must contain only the city name without additional qualifiers.
For example:
    - Valid: "Portland", "New York"
    - Invalid: "Portland, OR", "New York City"

Args:
    city (str): Name of the city to search in. Must be the exact city name without state, country, or other qualifiers.
    category (str): Category names to filter POIs. Each category must be a single lowercase word.
        Defaults to "general" if not provided.
    radius_km (float or str, optional): Search radius in kilometers. Defaults to 10 km if not provided or empty.

Returns:
    str: A formatted string listing the matching POIs and their details, or a message indicating no results or invalid input.
"""
```'''
    mock_database = {'Toronto': {'general': [{'name': 'CN Tower', 'type': 'Landmark', 'distance_km': 2}, {'name': 'Royal Ontario Museum', 'type': 'Museum', 'distance_km': 5}], 'child-friendly': [{'name': "Ripley's Aquarium", 'type': 'Aquarium', 'distance_km': 3}]}, 'Phoenix': {'general': [{'name': 'Desert Botanical Garden', 'type': 'Garden', 'distance_km': 10}], 'child-friendly': [{'name': 'Phoenix Zoo', 'type': 'Zoo', 'distance_km': 8}, {'name': "Children's Museum of Phoenix", 'type': 'Museum', 'distance_km': 4}]}, 'New York': {'general': [{'name': 'Statue of Liberty', 'type': 'Landmark', 'distance_km': 6}, {'name': 'Central Park', 'type': 'Park', 'distance_km': 3}], 'music': [{'name': 'Metropolitan Museum of Art', 'type': 'Rock Concert', 'distance_km': 4}]}, 'San Diego': {'general': [{'name': 'Balboa Park', 'type': 'Park', 'distance_km': 5}, {'name': 'San Diego Zoo', 'type': 'Zoo', 'distance_km': 7}]}, 'Philadelphia': {'museum': [{'name': 'Philadelphia Museum of Art', 'type': 'Museum', 'distance_km': 4}]}, 'San Francisco': {'general': [{'name': 'Golden Gate Park', 'type': 'Park', 'distance_km': 6}], 'museum': [{'name': 'San Francisco Museum of Modern Art', 'type': 'Museum', 'distance_km': 3}], 'garden': [{'name': 'San Francisco Botanical Garden', 'type': 'Garden', 'distance_km': 2}]}}
    default_radius_km = 10
    if not category:
        category = 'general'
    if not radius_km:
        radius_km = default_radius_km
    if city not in mock_database:
        return 'Invalid city. Please provide a valid city.'
    points_of_interest = []
    if city in mock_database and category in mock_database[city]:
        points_of_interest.extend([poi for poi in mock_database[city][category] if poi['distance_km'] <= radius_km])
    if not points_of_interest:
        return f'No points of interest found within {radius_km}km for the specified categories.'
    formatted_output = f'Points of Interest in {city}:\n'
    for poi in points_of_interest:
        formatted_output += f"- {poi['name']} ({poi['type']}), {poi['distance_km']}km away from the searching point\n"
    return formatted_output
if __name__ == '__main__':
    mcp.run(transport='stdio')