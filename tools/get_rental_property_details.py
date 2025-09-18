from mcp.server.fastmcp import FastMCP
mcp = FastMCP('get_rental_property_details')

@mcp.tool()
def get_rental_property_details(property_id) -> str:
    '''"""
Retrieve detailed information about a specific rental property using its unique ID.

Args:
    property_id (str): The unique identifier of the rental property. 
        For example, 'NY123' or 'PAR456'.

Returns:
    str: A formatted string containing the property's details, including 
        location, description, capacity, available dates, price per night, 
        contact number, and availability of laundry service and air conditioning.
        Returns an error message if the property_id is missing or not found.
"""'''
    mock_rental_properties = {'NY123': {'location': 'New York', 'description': 'Cozy house with laundry service, perfect for small families.', 'capacity': 2, 'available_date': 'Monday the 4th to Saturday the 9th', 'price_per_night': 150, 'contact_number': '+1-415-123-4567', 'laundry_service': True, 'air_conditioning': False}, 'PAR456': {'location': 'Paris', 'description': 'Charming studio in the heart of Paris, ideal for solo travelers.', 'capacity': 1, 'available_date': '1st to 11th', 'price_per_night': 100, 'contact_number': '+33-1-2345-6789', 'laundry_service': False, 'air_conditioning': True}, 'SF789': {'location': 'San Francisco', 'description': 'Spacious house, great for groups, includes laundry service.', 'capacity': 5, 'available_date': 'March 2nd', 'price_per_night': 200, 'contact_number': '+1-415-987-6543', 'laundry_service': True, 'air_conditioning': True}, 'LN987': {'location': 'London', 'description': 'Modern apartment with all amenities, suited for single travelers.', 'capacity': 1, 'available_date': '1st to 4th', 'price_per_night': 120, 'contact_number': '+44-20-7946-0958', 'laundry_service': False, 'air_conditioning': True}}
    if not property_id:
        return 'Error: No property_id provided.'
    property_details = mock_rental_properties.get(property_id)
    if not property_details:
        return f"Error: Property with ID '{property_id}' not found."
    response = f"Property ID: {property_id}\nLocation: {property_details['location']}\nDescription: {property_details['description']}\nCapacity: {property_details['capacity']} persons\nAvailable Date: {property_details['available_date']}\nPrice per Night: ${property_details['price_per_night']}\nContact Number: {property_details['contact_number']}\nLaundry Service: {('Yes' if property_details['laundry_service'] else 'No')}\nAir Conditioning: {('Yes' if property_details['air_conditioning'] else 'No')}"
    return response
if __name__ == '__main__':
    mcp.run(transport='stdio')