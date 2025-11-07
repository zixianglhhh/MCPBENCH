from mcp.server.fastmcp import FastMCP
mcp = FastMCP('booking_tool')

@mcp.tool()
def booking_tool(city, checkinDate, checkoutDate) -> str:
    '''"""
Books hotels in a specified city for given check-in and check-out dates.

This tool connects to the Booking MCP Server to reserve accommodations.
The `checkinDate` and `checkoutDate` must be provided in the format `MM/DD`.
Do not fabricate dates if they are not provided. The `city` parameter must
contain only the city name without state, province, or country information.
For example, "Portland" is valid, but "Portland, OR" is not; "New York" is
valid, but "New York City" is not.

Args:
    city (str): Name of the city where the hotel should be booked. Must be a
        plain city name without additional location qualifiers.
    checkinDate (str): Check-in date in `MM/DD` format.
    checkoutDate (str): Check-out date in `MM/DD` format.

Returns:
    str: A confirmation message with booking details if successful, or an
    error message if the booking could not be completed.
"""'''
    hotels_db = {'Chicago': [{'name': 'Chicago Grand Hotel', 'address': '123 Grand Ave, Chicago, IL', 'phone': '123-456-7890'}, {'name': 'Windy City Inn', 'address': '456 Windy St, Chicago, IL', 'phone': '987-654-3210'}], 'London': [{'name': 'London Bridge Hotel', 'address': 'London Bridge St, London', 'phone': '020-7946-0958'}, {'name': 'The Royal London', 'address': '123 Royal Rd, London', 'phone': '020-7946-0959'}], 'New York': [{'name': 'NYC Central Hotel', 'address': '789 Broadway, New York, NY', 'phone': '212-555-0198'}, {'name': 'Times Square Suites', 'address': '456 Seventh Ave, New York, NY', 'phone': '212-555-0199'}], 'Vancouver': [{'name': 'Vancouver Harbor Hotel', 'address': '789 Harbor St, Vancouver, BC', 'phone': '604-123-4567'}, {'name': 'Downtown Vancouver Inn', 'address': '321 Downtown Rd, Vancouver, BC', 'phone': '604-765-4321'}], 'Los Angeles': [{'name': 'LA Sunset Hotel', 'address': '123 Sunset Blvd, Los Angeles, CA', 'phone': '310-555-0101'}, {'name': 'Hollywood Inn', 'address': '456 Hollywood Rd, Los Angeles, CA', 'phone': '310-555-0102'}], 'Seattle': [{'name': 'Seattle Sky Hotel', 'address': '789 Rainy Ave, Seattle, WA', 'phone': '206-555-0145'}, {'name': 'Emerald City Inn', 'address': '321 Emerald St, Seattle, WA', 'phone': '206-555-0146'}]}
    if not city or not checkinDate or (not checkoutDate):
        return "Error: 'city', 'checkinDate', and 'checkoutDate' are required parameters."
    if city not in hotels_db:
        return f"Error: No hotels found for city '{city}'."
    hotel = hotels_db[city][0]
    booking_info = f"Booking successful!\nHotel: {hotel['name']}\nAddress: {hotel['address']}\nPhone: {hotel['phone']}\nCheck-in Date: {checkinDate}\nCheck-out Date: {checkoutDate}"
    return booking_info
if __name__ == '__main__':
    mcp.run(transport='stdio')