from mcp.server.fastmcp import FastMCP
mcp = FastMCP('get_rentalhouse_details')

@mcp.tool()
def get_rentalhouse_details(location, bedrooms, bathrooms) -> str:
    '''"""
    Retrieve details of rental houses based on location, number of bedrooms, and bathrooms.

    This tool connects to the Rental House MCP Server to fetch details such as the landlord's phone number.

    Args:
        location (str): The city or area where the rental house is located.
        bedrooms (int): The number of bedrooms required.
        bathrooms (int): The number of bathrooms required.

    Returns:
        str: Details of the rental house including the landlord's phone number, or an error message if no matching house is found.
    """'''
    rental_houses_db = {
        'Walnut Creek': [
            {'bedrooms': 2, 'bathrooms': 2, 'landlord_phone': '123-456-7890'},
            {'bedrooms': 3, 'bathrooms': 2, 'landlord_phone': '987-654-3210'}
        ],
        'San Francisco': [
            {'bedrooms': 1, 'bathrooms': 1, 'landlord_phone': '555-123-4567'},
            {'bedrooms': 2, 'bathrooms': 1, 'landlord_phone': '555-987-6543'}
        ]
    }

    if not location or not bedrooms or not bathrooms:
        return "Error: 'location', 'bedrooms', and 'bathrooms' are required parameters."

    if location not in rental_houses_db:
        return f"Error: No rental houses found for location '{location}'."

    matching_houses = [house for house in rental_houses_db[location] if house['bedrooms'] == bedrooms and house['bathrooms'] == bathrooms]

    if not matching_houses:
        return f"Error: No rental houses found in {location} with {bedrooms} bedrooms and {bathrooms} bathrooms."

    house = matching_houses[0]
    return f"Rental House Details:\nLocation: {location}\nBedrooms: {bedrooms}\nBathrooms: {bathrooms}\nLandlord Phone: {house['landlord_phone']}"

if __name__ == '__main__':
    mcp.run(transport='stdio')
