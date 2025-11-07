from mcp.server.fastmcp import FastMCP
mcp = FastMCP('fetch_terrain_elevation')

@mcp.tool()
def fetch_terrain_elevation(latitude: float, longitude: float, unit: str) -> str:
    '''```python
    """
    Retrieve the elevation above sea level for a specified geographic coordinate.

    This function is useful for applications in geographic analysis, topographical studies,
    agricultural modeling, and city planning. The elevation is returned in either meters 
    (default) or feet, based on the specified unit.

    Args:
        latitude (float): The latitude of the geographic coordinate, must be between -90 and 90 degrees.
        longitude (float): The longitude of the geographic coordinate, must be between -180 and 180 degrees.
        unit (str): The unit of measurement for the elevation. Acceptable values are 'meters' or 'feet'. 
                     Defaults to 'meters' if not specified.

    Returns:
        str: A string indicating the elevation at the given coordinate in the specified unit.
             If the input is invalid, an error message is returned.
    """
```'''
    mock_elevation_db = {(40.7128, -74.006): 10, (39.7392, -104.9903): 1609, (35.6895, 139.6917): 40, (19.4326, -99.1332): 2250, (34.0522, -118.2437): 71, (51.5074, -0.1278): 35, (48.8566, 2.3522): 35, (37.7749, -122.4194): 16}
    if not isinstance(latitude, (int, float)) or not isinstance(longitude, (int, float)):
        return "Error: 'latitude' and 'longitude' must be numbers."
    if latitude < -90 or latitude > 90:
        return "Error: 'latitude' must be between -90 and 90 decimal degrees."
    if longitude < -180 or longitude > 180:
        return "Error: 'longitude' must be between -180 and 180 decimal degrees."
    if unit is not None:
        if not isinstance(unit, str):
            return "Error: 'unit' must be a string."
        if unit.lower() not in ('meters', 'feet'):
            return "Error: 'unit' must be either 'meters' or 'feet'."
    unit_choice = unit.lower() if unit else 'meters'
    elevation_meters = mock_elevation_db.get((round(latitude, 4), round(longitude, 4)))
    if elevation_meters is None:
        elevation_meters = abs(latitude) * 5 + abs(longitude) * 0.1
        if elevation_meters > 4000:
            elevation_meters = 4000
    if unit_choice == 'feet':
        elevation_value = elevation_meters * 3.28084
        return f'Elevation at ({latitude}, {longitude}) is approximately {elevation_value:.2f} feet above sea level.'
    else:
        return f'Elevation at ({latitude}, {longitude}) is approximately {elevation_meters:.2f} meters above sea level.'
if __name__ == '__main__':
    mcp.run(transport='stdio')