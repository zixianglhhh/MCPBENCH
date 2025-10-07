from mcp.server.fastmcp import FastMCP
mcp = FastMCP('fetch_terrain_elevation')

@mcp.tool()
def fetch_terrain_elevation(lat: float, lon: float, units: str) -> str:
    '''```python
    """
    Retrieve the elevation above sea level for a specified geographic coordinate.

    This function is useful for applications in geographic analysis, topographical studies,
    agricultural modeling, and city planning. The elevation is returned in either meters 
    (default) or feet, based on the specified units.

    Args:
        lat (float): The latitude of the geographic coordinate, must be between -90 and 90 degrees.
        lon (float): The longitude of the geographic coordinate, must be between -180 and 180 degrees.
        units (str): The unit of measurement for the elevation. Acceptable values are 'meters' or 'feet'. 
                     Defaults to 'meters' if not specified.

    Returns:
        str: A string indicating the elevation at the given coordinate in the specified units.
             If the input is invalid, an error message is returned.
    """
```'''
    mock_elevation_db = {(40.7128, -74.006): 10, (39.7392, -104.9903): 1609, (35.6895, 139.6917): 40, (19.4326, -99.1332): 2250, (34.0522, -118.2437): 71, (51.5074, -0.1278): 35, (48.8566, 2.3522): 35, (37.7749, -122.4194): 16}
    if not isinstance(lat, (int, float)) or not isinstance(lon, (int, float)):
        return "Error: 'lat' and 'lon' must be numbers."
    if lat < -90 or lat > 90:
        return "Error: 'lat' must be between -90 and 90 decimal degrees."
    if lon < -180 or lon > 180:
        return "Error: 'lon' must be between -180 and 180 decimal degrees."
    if units is not None:
        if not isinstance(units, str):
            return "Error: 'units' must be a string."
        if units.lower() not in ('meters', 'feet'):
            return "Error: 'units' must be either 'meters' or 'feet'."
    unit_choice = units.lower() if units else 'meters'
    elevation_meters = mock_elevation_db.get((round(lat, 4), round(lon, 4)))
    if elevation_meters is None:
        elevation_meters = abs(lat) * 5 + abs(lon) * 0.1
        if elevation_meters > 4000:
            elevation_meters = 4000
    if unit_choice == 'feet':
        elevation_value = elevation_meters * 3.28084
        return f'Elevation at ({lat}, {lon}) is approximately {elevation_value:.2f} feet above sea level.'
    else:
        return f'Elevation at ({lat}, {lon}) is approximately {elevation_meters:.2f} meters above sea level.'
if __name__ == '__main__':
    mcp.run(transport='stdio')