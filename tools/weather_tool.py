from mcp.server.fastmcp import FastMCP
mcp = FastMCP('weather_tool')

@mcp.tool()
def weather_tool(city, date) -> str:
    '''"""
Queries a WeatherService for the weather in a specified city on a given date.

The `city` parameter must contain only the name of the city without additional
qualifiers such as state, country, or descriptors. For example, "Portland" is
valid, but "Portland, OR" is not; "New York" is valid, but "New York City" is not.
The `date` parameter must be a string in the format "MM/DD".

Args:
    city (str): The name of the city to query (e.g., "London", "Chicago").
    date (str): The date to query in "MM/DD" format (e.g., "03/12").

Returns:
    str: A formatted string describing the temperature, humidity, and wind
        conditions for the specified city and date, or a message indicating
        that the requested weather data is not available.
"""'''
    mock_weather_data = {'Chicago': {'03/01': {'temperature': '5°C', 'humidity': '60%', 'wind': '15 km/h'}}, 'London': {'03/11': {'temperature': '12°C', 'humidity': '75%', 'wind': '20 km/h'}, '03/12': {'temperature': '11°C', 'humidity': '80%', 'wind': '18 km/h'}, '03/01': {'temperature': '8°C', 'humidity': '70%', 'wind': '22 km/h'}}, 'New York': {'03/12': {'temperature': '10°C', 'humidity': '65%', 'wind': '12 km/h'}, '03/13': {'temperature': '9°C', 'humidity': '68%', 'wind': '14 km/h'}}, 'San Jose': {'03/07': {'temperature': '18°C', 'humidity': '50%', 'wind': '10 km/h'}}}
    if city not in mock_weather_data:
        return f'Weather data for {city} is not available.'
    if date not in mock_weather_data[city]:
        return f'Weather data for {city} on {date} is not available.'
    weather_info = mock_weather_data[city][date]
    temperature = weather_info['temperature']
    humidity = weather_info['humidity']
    wind = weather_info['wind']
    return f'The weather in {city} on {date} is as follows:\nTemperature: {temperature}\nHumidity: {humidity}\nWind: {wind}'
if __name__ == '__main__':
    mcp.run(transport='stdio')