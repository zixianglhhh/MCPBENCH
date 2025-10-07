from mcp.server.fastmcp import FastMCP
mcp = FastMCP('search_restaurant')

@mcp.tool()
def search_restaurant(location, cuisineTypes) -> str:
    '''"""
Find restaurants based on a specified city and cuisine type.

The `location` parameter must be the name of a city only, without state, country, or additional descriptors. 
For example, "Portland" is valid, but "Portland, OR" is not; "New York" is valid, but "New York City" is not.

The `cuisineTypes` parameter must be a string where each word is capitalized (e.g., "Italian", "Seafood", "Freshwater Fish"), and it must be one of the following: 'Ethiopian', 'Freshwater Fish', 'Italian', 'Seafood', 'American', 'Izakaya', 'Parisian', 'Indian', 'Chinese'.

Args:
    location (str): The name of the city to search in. Must not include state, country, or other qualifiers.
    cuisineTypes (str): The cuisine type to search for, with each word capitalized, and it must be one of the following: 'Ethiopian', 'Freshwater Fish', 'Italian', 'Seafood', 'American', 'Izakaya', 'Parisian', 'Indian', 'Chinese'.

Returns:
    str: A formatted string listing matching restaurants, or a message indicating no matches were found.
"""'''
    mock_restaurants = [{'name': 'Ethiopian Delight', 'location': 'Berkeley', 'cuisine': ['Ethiopian'], 'price_level': 2}, {'name': 'Freshwater Fishery', 'location': 'Palo Alto', 'cuisine': ['Freshwater Fish'], 'price_level': 3}, {'name': 'American Bistro', 'location': 'San Jose', 'cuisine': ['American'], 'price_level': 3}, {'name': 'Lobster Shack', 'location': 'San Mateo', 'cuisine': ['Seafood'], 'price_level': 4}, {'name': '2g Japanese Brasserie', 'location': 'San Francisco', 'cuisine': ['Izakaya', 'Japanese'], 'price_level': 3}, {'name': "Akiko's Sushi Bar", 'location': 'San Francisco', 'cuisine': ['Japanese', 'Seafood'], 'price_level': 3}, {'name': 'Marche Aux Fleurs', 'location': 'Ross', 'cuisine': ['Parisian', 'French'], 'price_level': 4}, {'name': 'Spice of India', 'location': 'Livermore', 'cuisine': ['Indian'], 'price_level': 2}, {'name': 'Mei-Don Chinese Cuisine', 'location': 'San Francisco', 'cuisine': ['Chinese'], 'price_level': 1}]
    results = []
    for restaurant in mock_restaurants:
        if cuisineTypes in restaurant['cuisine'] and location and (restaurant['location'].lower() == location.lower()):
            results.append(restaurant)
    if not results:
        return f'No restaurants found for {cuisineTypes} cuisine in {location}.'
    formatted_results = []
    for restaurant in results:
        formatted_results.append(f"Found the following restaurant: Name: {restaurant['name']}, Location: {restaurant['location']}, Cuisine: {', '.join(restaurant['cuisine'])}, Price Level: {restaurant['price_level']}")
    return '\n'.join(formatted_results)
if __name__ == '__main__':
    mcp.run(transport='stdio')