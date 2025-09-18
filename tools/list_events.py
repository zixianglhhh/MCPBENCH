from mcp.server.fastmcp import FastMCP
mcp = FastMCP('list_events')

@mcp.tool()
def list_events(date) -> str:
    '''"""
List events scheduled for a specific date.

The date must be provided in the format ``MM/DD`` (e.g., ``05/06``).  
If events are found for the specified date, their details, including title, status, and attendees, will be returned.  
If no events match the date, an appropriate message will be returned.

Args:
    date (str): The date to search for events, in ``MM/DD`` format.

Returns:
    str: A formatted string listing the events for the given date, including their status and attendees,  
         or a message indicating that no events were found or that the date format is invalid.
"""'''
    from datetime import datetime
    mock_events = [{'date': '05/06', 'title': 'Meeting with Bob', 'attendees': ['Alice', 'Bob'], 'status': 'confirmed'}, {'date': '05/06', 'title': 'Lunch with Sarah', 'attendees': ['Alice', 'Sarah'], 'status': 'tentative'}, {'date': '03/13', 'title': 'Project Presentation', 'attendees': ['Alice', 'Charlie'], 'status': 'confirmed'}, {'date': '04/01', 'title': "April Fool's Day Event", 'attendees': ['Alice'], 'status': 'confirmed'}, {'date': '04/06', 'title': 'Yoga Class', 'attendees': ['Alice'], 'status': 'confirmed'}]
    try:
        date_obj = datetime.strptime(date, '%m/%d')
    except ValueError:
        return 'Invalid date format. Please use MM/DD.'
    filtered_events = []
    for event in mock_events:
        event_date_obj = datetime.strptime(event['date'], '%m/%d')
        if event_date_obj == date_obj:
            filtered_events.append(event)
    if not filtered_events:
        return 'No events found for the specified date.'
    output = 'Events:\n'
    for event in filtered_events:
        output += f"- {event['date']}: {event['title']} (Status: {event['status']})\n"
        output += f"  Attendees: {', '.join(event['attendees'])}\n"
    return output
if __name__ == '__main__':
    mcp.run(transport='stdio')