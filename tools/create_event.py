from mcp.server.fastmcp import FastMCP
mcp = FastMCP('create_event')

@mcp.tool()
def create_event(subject, startDate=None, startTime=None, endDate=None, endTime=None, location=None, body=None, isMeeting=False, attendees=None, calendar=None) -> str:
    '''"""
Create a new calendar event or meeting with specified details.

This function allows you to create an event by providing information such as 
subject, start and end times, location, description, and attendees. It supports 
both all-day events and timed meetings, and can add the event to a specified calendar.

Args:
    subject (str): The title or subject of the event.
    startDate (str, optional): Start date in 'MM/DD' format. Required if startTime is provided.
    startTime (str, optional): Start time in 'HH:MM AM/PM' format. Required if startDate is provided.
    endDate (str, optional): End date in 'MM/DD' format. Required if endTime is provided.
    endTime (str, optional): End time in 'HH:MM AM/PM' format. Required if endDate is provided.
    location (str, optional): The location where the event will take place.
    body (str, optional): A description or body text for the event.
    isMeeting (bool, optional): Whether the event is a meeting. Defaults to False.
    attendees (str, optional): A semicolon-separated list of attendee email addresses. Required if isMeeting is True.
    calendar (str, optional): The name of the calendar to add the event to. Defaults to 'default'.

Returns:
    str: A confirmation message if the event is created successfully, or an error message if validation fails.
"""'''
    import datetime
    mock_calendar_db = {'default': [], 'personal': [], 'work': []}
    try:
        start_datetime = datetime.datetime.strptime(f'{startDate} {startTime}', '%m/%d %I:%M %p') if startDate and startTime else None
    except ValueError:
        return 'Error: Invalid start date or time format. Please use MM/DD for dates and HH:MM AM/PM for times.'
    if endDate and endTime:
        try:
            end_datetime = datetime.datetime.strptime(f'{endDate} {endTime}', '%m/%d %I:%M %p')
            if end_datetime <= start_datetime:
                return 'Error: End date and time must be after start date and time.'
        except ValueError:
            return 'Error: Invalid end date or time format. Please use MM/DD for dates and HH:MM AM/PM for times.'
    else:
        end_datetime = None
    if not calendar:
        calendar = 'default'
    if calendar not in mock_calendar_db:
        return 'Error: Specified calendar does not exist.'
    event = {'subject': subject, 'start': start_datetime, 'end': end_datetime, 'location': location, 'body': body, 'isMeeting': isMeeting, 'attendees': attendees.split(';') if attendees else []}
    mock_calendar_db[calendar].append(event)
    confirmation_message = f"Event '{subject}' has been created on the {calendar} calendar.\n"
    if start_datetime:
        confirmation_message += f"Start: {start_datetime.strftime('%m/%d %H:%M')}\n"
    if end_datetime:
        confirmation_message += f"End: {end_datetime.strftime('%m/%d %H:%M')}\n"
    if location:
        confirmation_message += f'Location: {location}\n'
    if body:
        confirmation_message += f'Description: {body}\n'
    if isMeeting and attendees:
        confirmation_message += f"Attendees: {', '.join(event['attendees'])}\n"
    return confirmation_message
if __name__ == '__main__':
    mcp.run(transport='stdio')