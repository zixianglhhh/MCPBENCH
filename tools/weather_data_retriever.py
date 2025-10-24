from mcp.server.fastmcp import FastMCP
mcp = FastMCP('weather_data_retriever')

@mcp.tool()
def weather_data_retriever(start_date: str, end_date: str, range: str, location: str) -> str:
    '''```python
    """
    Retrieves historical weather data for a specified location, date range, and year range.

    Args:
        start_date (str): The start date in 'MM/DD' format (e.g., '03/01').
        end_date (str): The end date in 'MM/DD' format (e.g., '03/15').
        range (str): The range of years to retrieve data for in 'YYYY-YYYY' format (e.g., '2019-2023').
        location (str): The name of the location (e.g., 'London').

    Returns:
        str: A string containing the weather data for the specified date and year range, including temperature and precipitation details. Returns an error message if the location is not found or if the date/year formats are invalid.
    """
```'''
    mock_weather_data = {'London': {'2019': {'03/01': {'temperature': 9, 'precipitation': 5}, '03/02': {'temperature': 9.5, 'precipitation': 3}, '03/03': {'temperature': 10, 'precipitation': 4}, '03/04': {'temperature': 10.2, 'precipitation': 0}, '03/05': {'temperature': 11, 'precipitation': 2}, '03/06': {'temperature': 11.5, 'precipitation': 1}, '03/07': {'temperature': 12, 'precipitation': 5}, '03/08': {'temperature': 12.2, 'precipitation': 6}, '03/09': {'temperature': 12.5, 'precipitation': 3}, '03/10': {'temperature': 12.8, 'precipitation': 2}, '03/11': {'temperature': 13, 'precipitation': 1}, '03/12': {'temperature': 13.2, 'precipitation': 2}, '03/13': {'temperature': 13.5, 'precipitation': 3}, '03/14': {'temperature': 13.7, 'precipitation': 1}, '03/15': {'temperature': 14, 'precipitation': 0}}, '2020': {'03/01': {'temperature': 9.3, 'precipitation': 5}, '03/02': {'temperature': 9.8, 'precipitation': 3}, '03/03': {'temperature': 10.3, 'precipitation': 4}, '03/04': {'temperature': 10.5, 'precipitation': 0}, '03/05': {'temperature': 11.2, 'precipitation': 2}, '03/06': {'temperature': 11.7, 'precipitation': 1}, '03/07': {'temperature': 12.1, 'precipitation': 5}, '03/08': {'temperature': 12.3, 'precipitation': 6}, '03/09': {'temperature': 12.6, 'precipitation': 3}, '03/10': {'temperature': 12.9, 'precipitation': 2}, '03/11': {'temperature': 13.1, 'precipitation': 1}, '03/12': {'temperature': 13.3, 'precipitation': 2}, '03/13': {'temperature': 13.6, 'precipitation': 3}, '03/14': {'temperature': 13.8, 'precipitation': 1}, '03/15': {'temperature': 14.1, 'precipitation': 0}}, '2021': {'03/01': {'temperature': 9.1, 'precipitation': 5}, '03/02': {'temperature': 9.6, 'precipitation': 3}, '03/03': {'temperature': 10.1, 'precipitation': 4}, '03/04': {'temperature': 10.3, 'precipitation': 0}, '03/05': {'temperature': 11, 'precipitation': 2}, '03/06': {'temperature': 11.4, 'precipitation': 1}, '03/07': {'temperature': 11.9, 'precipitation': 5}, '03/08': {'temperature': 12.1, 'precipitation': 6}, '03/09': {'temperature': 12.4, 'precipitation': 3}, '03/10': {'temperature': 12.7, 'precipitation': 2}, '03/11': {'temperature': 12.9, 'precipitation': 1}, '03/12': {'temperature': 13.1, 'precipitation': 2}, '03/13': {'temperature': 13.4, 'precipitation': 3}, '03/14': {'temperature': 13.6, 'precipitation': 1}, '03/15': {'temperature': 13.9, 'precipitation': 0}}, '2022': {'03/01': {'temperature': 9.2, 'precipitation': 5}, '03/02': {'temperature': 9.7, 'precipitation': 3}, '03/03': {'temperature': 10.2, 'precipitation': 4}, '03/04': {'temperature': 10.4, 'precipitation': 0}, '03/05': {'temperature': 11.1, 'precipitation': 2}, '03/06': {'temperature': 11.6, 'precipitation': 1}, '03/07': {'temperature': 12, 'precipitation': 5}, '03/08': {'temperature': 12.2, 'precipitation': 6}, '03/09': {'temperature': 12.5, 'precipitation': 3}, '03/10': {'temperature': 12.8, 'precipitation': 2}, '03/11': {'temperature': 13, 'precipitation': 1}, '03/12': {'temperature': 13.2, 'precipitation': 2}, '03/13': {'temperature': 13.5, 'precipitation': 3}, '03/14': {'temperature': 13.7, 'precipitation': 1}, '03/15': {'temperature': 14, 'precipitation': 0}}, '2023': {'03/01': {'temperature': 9, 'precipitation': 5}, '03/02': {'temperature': 9.5, 'precipitation': 3}, '03/03': {'temperature': 10, 'precipitation': 4}, '03/04': {'temperature': 10.2, 'precipitation': 0}, '03/05': {'temperature': 11, 'precipitation': 2}, '03/06': {'temperature': 11.5, 'precipitation': 1}, '03/07': {'temperature': 12, 'precipitation': 5}, '03/08': {'temperature': 12.2, 'precipitation': 6}, '03/09': {'temperature': 12.5, 'precipitation': 3}, '03/10': {'temperature': 12.8, 'precipitation': 2}, '03/11': {'temperature': 13, 'precipitation': 1}, '03/12': {'temperature': 13.2, 'precipitation': 2}, '03/13': {'temperature': 13.5, 'precipitation': 3}, '03/14': {'temperature': 13.7, 'precipitation': 1}, '03/15': {'temperature': 14, 'precipitation': 0}}}}
    if location not in mock_weather_data:
        return 'Error: City not found in database.'
    try:
        (start_month, start_day) = map(int, start_date.split('/'))
        (end_month, end_day) = map(int, end_date.split('/'))
    except ValueError:
        return "Error: Invalid date format. Please use 'MM/DD'."
    try:
        (start_year, end_year) = map(int, range.split('-'))
        if start_year > end_year:
            return 'Error: Start year cannot be greater than end year.'
    except ValueError:
        return "Error: Invalid year range format. Please use 'YYYY-YYYY'."
    weather_data = []
    for year in range(start_year, end_year + 1):
        year_data = mock_weather_data.get(location, {}).get(str(year), {})
        for date in year_data:
            (month, day) = map(int, date.split('/'))
            if (month > start_month or (month == start_month and day >= start_day)) and (month < end_month or (month == end_month and day <= end_day)):
                weather_data.append(f"Year: {year}, Date: {date}, Temperature: {year_data[date]['temperature']}°C, Precipitation: {year_data[date]['precipitation']}mm")
    if not weather_data:
        return 'Error: No data found for the specified date range.'
    return '\n'.join(weather_data)
if __name__ == '__main__':
    mcp.run(transport='stdio')