from mcp.server.fastmcp import FastMCP
mcp = FastMCP('create_event')

@mcp.tool()
def create_event(subject, startDate=None, startTime=None, endDate=None, endTime=None, location=None, isMeeting=False, attendees=None) -> str:
    '''"""
Create a new calendar event or meeting with specified details.

This function allows you to create an event by providing information such as 
subject, start and end times, location, description, and attendees. It supports 
both all-day events and timed meetings, and can add the event to a specified calendar.

Args:
    subject (str, required): The title or subject of the event.
    startDate (str, required): Start date in 'MM/DD' format.
    startTime (str, optional): Start time in 'HH:MM' format, where the hour is in 24-hour format.
    endDate (str, required): End date in 'MM/DD' format.
    endTime (str, optional): End time in 'HH:MM' format, where the hour is in 24-hour format.
    location (str, required): The location where the event will take place.
    isMeeting (bool, optional): Whether the event is a meeting. Defaults to False.
    attendees (str, optional): A semicolon-separated list of attendee email addresses. Required if isMeeting is True.

Returns:
    str: A confirmation message if the event is created successfully, or an error message if validation fails.
"""'''
    import datetime
    mock_calendar_db = {'default': [], 'personal': [], 'work': []}
    try:
        start_datetime = datetime.datetime.strptime(f'{startDate} {startTime}', '%m/%d %H:%M') if startDate and startTime else None
    except ValueError:
        return 'Error: Invalid start date or time format. Please use MM/DD for dates and HH:MM for times.'
    if endDate and endTime:
        try:
            end_datetime = datetime.datetime.strptime(f'{endDate} {endTime}', '%m/%d %H:%M')
            if end_datetime <= start_datetime:
                return 'Error: End date and time must be after start date and time.'
        except ValueError:
            return 'Error: Invalid end date or time format. Please use MM/DD for dates and HH:MM for times.'
    else:
        end_datetime = None
    event = {'subject': subject, 'start': start_datetime, 'end': end_datetime, 'location': location, 'isMeeting': isMeeting, 'attendees': attendees.split(';') if attendees else []}
    mock_calendar_db['default'].append(event)
    confirmation_message = f"Event '{subject}' has been created on the default calendar.\n"
    if start_datetime:
        confirmation_message += f"Start: {start_datetime.strftime('%m/%d %H:%M')}\n"
    if end_datetime:
        confirmation_message += f"End: {end_datetime.strftime('%m/%d %H:%M')}\n"
    if location:
        confirmation_message += f'Location: {location}\n'
    if isMeeting and attendees:
        confirmation_message += f"Attendees: {', '.join(event['attendees'])}\n"
    return confirmation_message
if __name__ == '__main__':
    mcp.run(transport='stdio')