from mcp.server.fastmcp import FastMCP
mcp = FastMCP('get_restaurant_details')

@mcp.tool()
def get_restaurant_details(restaurant_name) -> str:
    '''"""
Get detailed information about a specific restaurant using its name.

Args:
    restaurant_name (str): The exact name of the restaurant to retrieve details for.

Returns:
    str: A formatted string containing the restaurant's name, address, phone number, 
        liquor service availability, cuisine type, and live music availability.
        Returns an error message if the restaurant name is not found.
"""'''
    mock_restaurant_db = {'American Bistro': {'name': 'American Bistro', 'address': '1234 San Jose Ave, San Jose, CA', 'phone_number': '(408) 555-1234', 'serves_liquor': True, 'cuisine': 'American', 'live_music': False}, 'Lobster Shack': {'name': 'Lobster Shack', 'address': '5678 Ocean Blvd, San Mateo, CA', 'phone_number': '(650) 555-5678', 'serves_liquor': True, 'cuisine': 'Seafood', 'live_music': True}, 'Aato': {'name': 'Aato', 'address': '7890 Bay St, San Francisco, CA', 'phone_number': '(415) 555-7890', 'serves_liquor': True, 'cuisine': 'Japanese', 'live_music': False}, 'Union': {'name': 'Union', 'address': '1357 Market St, Santa Rosa, CA', 'phone_number': '(707) 555-1357', 'serves_liquor': True, 'cuisine': 'Italian', 'live_music': False}}
    if restaurant_name not in mock_restaurant_db:
        return 'Error: Invalid restaurant name. The restaurant details could not be found.'
    restaurant_details = mock_restaurant_db[restaurant_name]
    details = f"Restaurant Name: {restaurant_details['name']}\nAddress: {restaurant_details['address']}\nPhone Number: {restaurant_details['phone_number']}\nServes Liquor: {('Yes' if restaurant_details['serves_liquor'] else 'No')}\nCuisine: {restaurant_details['cuisine']}\nLive Music: {('Yes' if restaurant_details['live_music'] else 'No')}"
    return details
if __name__ == '__main__':
    mcp.run(transport='stdio')