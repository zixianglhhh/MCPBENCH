from mcp.server.fastmcp import FastMCP
mcp = FastMCP('search_ticketmaster')

@mcp.tool()
def search_ticketmaster(type, city) -> str:
    '''```python
"""
Search for events based on event type and city location.

The `type` parameter must be formatted with each word capitalized and the word
"Event" appended at the end. For example: "Concert Event".
The `city` parameter should contain only the city name without state or country
information. For example: "Portland" is valid, but "Portland, OR" is not.

Args:
    type (str): The event type to search for, with each word capitalized and
        ending with "Event" (e.g., "Concert Event").
    city (str): The name of the city where the event is located, without state
        or country (e.g., "Seattle").

Returns:
    str: A formatted string listing the matching events, including event type,
    location, and date range.
"""
```'''
    mock_db = [{'event type': 'Concert Event', 'event location': 'San Francisco', 'start date': '03/01', 'end date': '03/02'}, {'event type': 'American Football Event', 'event location': 'Boston', 'start date': '04/06', 'end date': '04/06'}, {'event type': 'Concert Event', 'event location': 'Rohnert Park', 'start date': '03/11', 'end date': '03/11'}, {'event type': 'Country Show Event', 'event location': 'Seattle', 'start date': '04/10', 'end date': '04/10'}, {'event type': 'Pop Music Event', 'event location': 'London', 'start date': '05/09', 'end date': '05/09'}, {'event type': 'Basketball Event', 'event location': 'Atlanta', 'start date': '03/05', 'end date': '03/05'}, {'event type': 'Football Event', 'event location': 'Atlanta', 'start date': '03/13', 'end date': '03/13'}, {'event type': 'Rock Concert Event', 'event location': 'New York', 'start date': '03/11', 'end date': '03/11'}, {'event type': 'Match Event', 'event location': 'Portland', 'start date': '03/06', 'end date': '03/06'}, {'event type': 'Baseball Event', 'event location': 'New York', 'start date': '03/13', 'end date': '03/13'}, {'event type': 'Concert Event', 'event location': 'Washington', 'start date': '03/07', 'end date': '03/07'}]
    results = [event for event in mock_db if type in event['event type'] and city.lower() == event['event location'].lower()]
    return 'Found the following events: ' + '\n'.join([event['event type'] + ' in ' + event['event location'] + ' on ' + event['start date'] + ' to ' + event['end date'] for event in results])
if __name__ == '__main__':
    mcp.run(transport='stdio')