from mcp.server.fastmcp import FastMCP

mcp = FastMCP("find_earthquakes")

@mcp.tool()
def find_earthquakes(endTime: str, startTime: str, minLatitude: str, maxLatitude: str, minLongitude: str, maxLongitude: str, minmagnitude: str) -> str:
    '''```python
    """
    Search for earthquakes in a mock dataset by time range, bounding box, and minimum magnitude.

    This tool demonstrates typical geo-temporal filtering: date-time window, latitude/longitude bounding box, and
    minimum magnitude threshold. Inputs are provided as strings and parsed to appropriate numeric/time types.

    Args:
        endTime (str): End of time range in ISO-like format "YYYY-MM-DDTHH:MM:SS".
        startTime (str): Start of time range in ISO-like format "YYYY-MM-DDTHH:MM:SS".
        minLatitude (str): Minimum latitude of the earthquake.
        maxLatitude (str): Maximum latitude of the earthquake.
        minLongitude (str): Minimum longitude of the earthquake.
        maxLongitude (str): Maximum longitude of the earthquake.
        minmagnitude (str): Minimum magnitude of the earthquake.

    Returns:
        str: A formatted list of matching earthquakes or a message indicating no results or input errors.

    Raises:
        ValueError: If date parsing fails; other parsing issues are returned as error strings.
    """
    ```'''
    # Mock database with earthquake data
    earthquakes = [
        {
            "id": "eq1",
            "location": "Los Angeles, USA",
            "latitude": 34.0522,
            "longitude": -118.2437,
            "magnitude": 4.5,
            "date": "2023-09-15T14:30:00"
        },
        {
            "id": "eq2",
            "location": "San Francisco, USA",
            "latitude": 37.7749,
            "longitude": -122.4194,
            "magnitude": 5.0,
            "date": "2023-09-10T11:00:00"
        },
        {
            "id": "eq3",
            "location": "Tokyo, Japan",
            "latitude": 35.6895,
            "longitude": 139.6917,
            "magnitude": 6.3,
            "date": "2023-08-25T09:45:00"
        },
        {
            "id": "eq4",
            "location": "Mexico City, Mexico",
            "latitude": 19.4326,
            "longitude": -99.1332,
            "magnitude": 4.8,
            "date": "2023-09-20T19:00:00"
        }
    ]
    
    from datetime import datetime

    # Helper function to parse a string date into a datetime object
    def parse_date(date_string):
        try:
            return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DDTHH:MM:SS'.")

    # Parse input parameters and handle errors
    try:
        start_time = parse_date(startTime)
        end_time = parse_date(endTime)
        max_latitude = float(maxLatitude)
        min_latitude = float(minLatitude)
        max_longitude = float(maxLongitude)
        min_longitude = float(minLongitude)
        min_magnitude = float(minmagnitude)
    except ValueError as e:
        return str(e)

    # Filter earthquakes based on the provided criteria
    filtered_earthquakes = []
    for eq in earthquakes:
        eq_date = parse_date(eq["date"])
        if (min_latitude <= eq["latitude"] <= max_latitude and
            min_longitude <= eq["longitude"] <= max_longitude and
            eq_date >= start_time and eq_date <= end_time and
            eq["magnitude"] >= min_magnitude):
            filtered_earthquakes.append(eq)

    # Generate output string
    if filtered_earthquakes:
        result = "Found the following earthquakes:\n"
        for eq in filtered_earthquakes:
            result += (f"ID: {eq['id']}, Location: {eq['location']}, "
                       f"Latitude: {eq['latitude']}, Longitude: {eq['longitude']}, "
                       f"Magnitude: {eq['magnitude']}, Date: {eq['date']}\n")
    else:
        result = "No earthquakes found matching the criteria."

    return result

if __name__ == "__main__":
    mcp.run(transport='stdio')
