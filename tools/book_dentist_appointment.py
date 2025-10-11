from mcp.server.fastmcp import FastMCP
mcp = FastMCP('booking_tool')
@mcp.tool()
def book_dentist_appointment(location, date, time, dentist_type) -> str:
    '''"""
Book an appointment with a dentist of a specified type at a given location, date, and time.
Args:
    location(str): The city or area where the dentist is located. Must be a plain city name without additional location qualifiers.
    dentist_type(str): The type of dental service required (e.g., "general", "cosmetic", "orthodontic").
    date (str): The date of the appointment in a MM/DD format.
    time (str): The time of the appointment in a standard format (i.e., "HH:MM AM/PM").
Returns:
    str: A confirmation message indicating that the appointment has been successfully booked.
"""'''
    return f'Appointment booked with a {dentist_type} dentist in {location} on {date} at {time}.'
if __name__ == '__main__':
    mcp.run(transport='stdio')