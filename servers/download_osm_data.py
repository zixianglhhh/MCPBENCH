from mcp.server.fastmcp import FastMCP
mcp = FastMCP('download_osm_data')

@mcp.tool()
def download_osm_data(city: str, output_path: str, format: str) -> str:
    '''```python
    """
    Downloads raw OpenStreetMap (OSM) data for a specified city and saves it to a file.

    This function fetches OSM data for a given city and stores it in the specified 
    output format. The data can be saved in one of the following formats: JSON, XML, or PBF.

    Args:
        city (str): The name of the city for which to download OSM data (e.g., "New York", "London").
        output_path (str): The file path where the downloaded OSM data will be saved. Should be in the format of /cityname.
        format (str): The format in which to save the OSM data. Must be one of "json", "xml", or "pbf".

    Returns:
        str: A success message confirming the download and the location where the OSM data is saved.

    Raises:
        ValueError: If any of the input parameters are invalid or the city is not supported.
        IOError: If there is an error saving the OSM data to the specified path.
    """
```'''
    mock_osm_data = {'Berlin': {'cities': ['Berlin-Mitte', 'Berlin-Kreuzberg', 'Berlin-Charlottenburg', 'Berlin-Spandau'], 'boundaries': {'postal_codes': ['10115', '10117', '10119', '10178', '10179', '10243', '10245', '10247', '10249', '10315'], 'state': 'Berlin', 'city': 'Berlin', 'total_area': 891.8, 'area_unit': 'km²'}}, 'Karlsruhe': {'cities': ['Karlsruhe'], 'boundaries': {'postal_codes': ['76131', '76133', '76135', '76137', '76139', '76149', '76185', '76187', '76189', '76199'], 'state': 'Baden-Württemberg', 'city': 'Karlsruhe', 'total_area': 173.46, 'area_unit': 'km²'}}}
    if not isinstance(city, str) or not city.strip():
        raise ValueError("Parameter 'city' must be a non-empty string.")
    if not isinstance(output_path, str) or not output_path.strip():
        raise ValueError("Parameter 'output_path' must be a non-empty string.")
    if not isinstance(format, str) or format.lower() not in ['json', 'xml', 'pbf']:
        raise ValueError("Parameter 'format' must be one of: 'json', 'xml', 'pbf'.")
    city_clean = city.strip()
    result_data = None
    if 'Berlin' in city_clean:
        result_data = {'city': city_clean, 'cities': mock_osm_data['Berlin']['cities'], 'boundaries': mock_osm_data['Berlin']['boundaries']}
    elif 'Karlsruhe' in city_clean:
        result_data = {'city': city_clean, 'cities': mock_osm_data['Karlsruhe']['cities'], 'boundaries': mock_osm_data['Karlsruhe']['boundaries']}
    else:
        raise ValueError(f'No mock OSM data found for city: {city_clean}')
    try:
        simulated_saved_content = {'format': format.lower(), 'data': result_data}
        saved_str = str(simulated_saved_content)
    except Exception as e:
        raise IOError(f'Failed to save OSM data to {output_path}: {e}')
    return f"OSM data for city '{city_clean}' downloaded in {format.upper()} format and saved to {output_path}."
if __name__ == '__main__':
    mcp.run(transport='stdio')