from mcp.server.fastmcp import FastMCP
from typing import List
mcp = FastMCP('get_time')

@mcp.tool()
def get_time(timezone: List[str]) -> str:
    '''```python
"""
Retrieve current time information for specified timezones.

This function returns the current time for each timezone provided in the input list.
The time information is formatted as a string for each requested timezone.

Args:
    timezone (List[str]): A list of timezone strings in the 'Continent/City' format 
        (e.g., ['America/New_York', 'Europe/London']). Each string must represent a valid 
        timezone.

Returns:
    str: A string containing the current time information for each timezone, 
    separated by double newlines. Each entry is formatted as:
    "The current time in {timezone} is {current_time}."
"""
```'''
    mock_timezone_to_time = {'America/New_York': {'time': '18:00'}, 'America/Los_Angeles': {'time': '15:00'}, 'Europe/London': {'time': '23:00'}, 'Asia/Tokyo': {'time': '08:00'}, 'Europe/Paris': {'time': '00:00'}, 'Europe/Berlin': {'time': '00:00'}, 'Australia/Sydney': {'time': '09:00'}, 'America/Chicago': {'time': '17:00'}}
    if not timezone or not isinstance(timezone, list):
        return "Error: 'timezone' parameter must be a non-empty list of strings."
    invalid_timezones = []
    for tz in timezone:
        if not isinstance(tz, str) or '/' not in tz:
            invalid_timezones.append(tz)
    if invalid_timezones:
        return f"Error: Invalid timezone formats found: {', '.join(invalid_timezones)}. Timezones must be in 'Region/City' format."
    results = []
    for tz in timezone:
        timezone_info = mock_timezone_to_time.get(tz, {'time': '00:00'})
        example_time = timezone_info['time']
        mock_current_time = f'{example_time}:00'
        result = f'The current time in {tz} is {mock_current_time}.'
        results.append(result)
    return '\n\n'.join(results)
if __name__ == '__main__':
    mcp.run(transport='stdio')