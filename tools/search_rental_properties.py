from mcp.server.fastmcp import FastMCP
mcp = FastMCP('search_rental_properties')

@mcp.tool()
def search_rental_properties(location, property_type, rating=None) -> str:
    '''"""
Search for rental listings based on specified criteria, including city name, property type, and optional minimum rating.

The `location` parameter must contain only the name of a city (e.g., "Portland" is valid, but "Portland, OR" is not; "New York" is valid, but "New York City" is not). The `property_type` must be provided in lowercase (e.g., "house", "apartment"). If `rating` is provided, only properties with a rating greater than or equal to this value will be returned.

Args:
    location (str): Name of the city where the property is located. Must not include state, country, or other qualifiers.
    property_type (str): Type of property in lowercase (e.g., "house", "apartment").
    rating (float, optional): Minimum acceptable property rating. Defaults to None.

Returns:
    str: A formatted string listing matching properties, or a message indicating no matches were found.
"""'''
    rental_properties_db = [{'location': 'New York', 'property_type': 'house', 'rating': 4.0, 'property_id': 'NY123'}, {'location': 'Paris', 'property_type': 'house', 'rating': 4.5, 'property_id': 'PAR456'}, {'location': 'San Francisco', 'property_type': 'house', 'rating': 4.3, 'property_id': 'SF789'}, {'location': 'Oakley', 'property_type': 'apartment', 'rating': 4.2, 'property_id': 'OAK123'}, {'location': 'Santa Rosa', 'property_type': 'apartment', 'rating': 4.1, 'property_id': 'SRO123'}, {'location': 'London', 'property_type': 'house', 'rating': 4.4, 'property_id': 'LN987'}, {'location': 'San Francisco', 'property_type': 'house', 'rating': 4.6, 'property_id': 'SF654'}, {'location': 'Portland', 'property_type': 'house', 'rating': 4.0, 'property_id': 'PT321'}, {'location': 'Los Angeles', 'property_type': 'apartment', 'rating': 4.3, 'property_id': 'LA852'}, {'location': 'Seattle', 'property_type': 'house', 'rating': 4.5, 'property_id': 'SE741'}]
    filtered_properties = []
    if not rating:
        for property in rental_properties_db:
            if location and property['location'].lower() == location.lower() and (property['property_type'] == property_type):
                filtered_properties.append(property)
    else:
        for property in rental_properties_db:
            if location and property['location'].lower() == location.lower() and (property['property_type'] == property_type) and (property['rating'] >= float(rating)):
                filtered_properties.append(property)
    response = ''
    if filtered_properties:
        for prop in filtered_properties:
            response += f"Location: {prop['location']}, Type: {prop['property_type']}, Rating: {prop['rating']}, Property ID: {prop['property_id']}\n"
    else:
        response = 'No properties found matching the criteria.'
    return response
if __name__ == '__main__':
    mcp.run(transport='stdio')