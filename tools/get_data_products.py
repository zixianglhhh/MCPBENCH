from mcp.server.fastmcp import FastMCP
from typing import List
mcp = FastMCP('get_data_products')

@mcp.tool()
def get_data_products(coordinates: List[float], data_type: str, start_date: str, end_date: str) -> str:
    '''```python
"""
Retrieves satellite data products based on specified geographical coordinates, data type, 
and date range.

This function filters satellite data products according to the provided latitude and 
longitude coordinates, the type of data requested, and the specified start and end dates. 
The dates must be in ISO 8601 format (YYYY-MM-DD). The function returns the formatted 
satellite data products that match the criteria.

Args:
    coordinates (List[float]): A list containing latitude and longitude in the format [lat, lon].
    data_type (str): The type of satellite data to retrieve (e.g., 'soil').
    start_date (str): The start date for the data retrieval in ISO 8601 format (YYYY-MM-DD).
    end_date (str): The end date for the data retrieval in ISO 8601 format (YYYY-MM-DD).

Returns:
    str: A formatted string containing the satellite data products that match the specified 
    criteria, including coordinates and data filtered within the date range. Returns an 
    error message if input validation fails or no matching data is found.
"""
```'''
    mock_db = [{'coordinates': [51.5074, -0.1278], 'data_type': 'soil', 'data': [{'date': '2025-09-25', 'soil_moisture': 0.32, 'soil_temperature': 15.2}, {'date': '2025-09-26', 'soil_moisture': 0.28, 'soil_temperature': 16.8}, {'date': '2025-09-27', 'soil_moisture': 0.35, 'soil_temperature': 14.5}, {'date': '2025-09-28', 'soil_moisture': 0.31, 'soil_temperature': 17.1}]}, {'coordinates': [60.5074, -1.1278], 'data_type': 'soil', 'data': [{'date': '2025-09-01', 'soil_moisture': 0.4, 'soil_temperature': 8.2}, {'date': '2025-09-02', 'soil_moisture': 0.38, 'soil_temperature': 9.1}, {'date': '2025-09-03', 'soil_moisture': 0.42, 'soil_temperature': 7.8}, {'date': '2025-09-04', 'soil_moisture': 0.36, 'soil_temperature': 10.3}, {'date': '2025-09-05', 'soil_moisture': 0.39, 'soil_temperature': 8.9}, {'date': '2025-09-06', 'soil_moisture': 0.41, 'soil_temperature': 9.5}, {'date': '2025-09-07', 'soil_moisture': 0.37, 'soil_temperature': 11.2}, {'date': '2025-09-08', 'soil_moisture': 0.43, 'soil_temperature': 7.6}, {'date': '2025-09-09', 'soil_moisture': 0.35, 'soil_temperature': 12.1}, {'date': '2025-09-10', 'soil_moisture': 0.38, 'soil_temperature': 9.8}, {'date': '2025-09-11', 'soil_moisture': 0.4, 'soil_temperature': 8.4}, {'date': '2025-09-12', 'soil_moisture': 0.36, 'soil_temperature': 10.7}, {'date': '2025-09-13', 'soil_moisture': 0.42, 'soil_temperature': 7.9}, {'date': '2025-09-14', 'soil_moisture': 0.39, 'soil_temperature': 9.3}, {'date': '2025-09-15', 'soil_moisture': 0.37, 'soil_temperature': 11.5}, {'date': '2025-09-16', 'soil_moisture': 0.41, 'soil_temperature': 8.7}, {'date': '2025-09-17', 'soil_moisture': 0.35, 'soil_temperature': 12.8}, {'date': '2025-09-18', 'soil_moisture': 0.38, 'soil_temperature': 9.6}, {'date': '2025-09-19', 'soil_moisture': 0.4, 'soil_temperature': 8.1}, {'date': '2025-09-20', 'soil_moisture': 0.36, 'soil_temperature': 10.9}, {'date': '2025-09-21', 'soil_moisture': 0.43, 'soil_temperature': 7.3}, {'date': '2025-09-22', 'soil_moisture': 0.37, 'soil_temperature': 11.8}, {'date': '2025-09-23', 'soil_moisture': 0.39, 'soil_temperature': 9.2}, {'date': '2025-09-24', 'soil_moisture': 0.41, 'soil_temperature': 8.6}, {'date': '2025-09-25', 'soil_moisture': 0.35, 'soil_temperature': 12.4}, {'date': '2025-09-26', 'soil_moisture': 0.38, 'soil_temperature': 9.7}, {'date': '2025-09-27', 'soil_moisture': 0.4, 'soil_temperature': 8.3}, {'date': '2025-09-28', 'soil_moisture': 0.36, 'soil_temperature': 10.5}]}]
    from datetime import datetime
    if not start_date or not end_date:
        return "Error: 'start_date' and 'end_date' are required parameters."
    try:
        start_dt = datetime.fromisoformat(start_date)
        end_dt = datetime.fromisoformat(end_date)
    except ValueError:
        return 'Error: Dates must be in ISO 8601 format (YYYY-MM-DD).'
    if start_dt > end_dt:
        return "Error: 'start_date' cannot be after 'end_date'."
    if coordinates:
        if not isinstance(coordinates, (list, tuple)) or len(coordinates) != 2 or (not all((isinstance(c, (int, float)) for c in coordinates))):
            return "Error: 'coordinates' must be an array of two numbers [latitude, longitude]."
    results = []
    for entry in mock_db:
        coords_match = True
        if coordinates:
            coords_match = abs(entry['coordinates'][0] - coordinates[0]) < 0.0001 and abs(entry['coordinates'][1] - coordinates[1]) < 0.0001
        type_match = True
        if data_type:
            type_match = entry['data_type'].lower() == data_type.lower()
        date_match = True
        if coords_match and type_match and date_match:
            filtered_data = [d for d in entry['data'] if start_dt <= datetime.fromisoformat(d['date']) <= end_dt]
            if filtered_data:
                results.append({'coordinates': entry['coordinates'], 'data_type': entry['data_type'], 'data': filtered_data})
    if not results:
        return 'No matching satellite data products found for the given criteria.'
    output_lines = ['Satellite Data Products:']
    for res in results:
        output_lines.append(f"Location: {res['coordinates']}, Data Type: {res['data_type']}")
        for record in res['data']:
            output_lines.append(f"  Date: {record['date']}, Soil Moisture: {record['soil_moisture']}, Soil Temperature: {record['soil_temperature']}°C")
    return '\n'.join(output_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')