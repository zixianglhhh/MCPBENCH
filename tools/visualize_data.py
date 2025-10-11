from mcp.server.fastmcp import FastMCP
mcp = FastMCP('visualize_data')

@mcp.tool()
def visualize_data(data_dir: str, visualize_type: str, output_dir: str, output_format: str) -> str:
    '''```python
"""
Generates and saves data visualizations based on specified parameters.

This function processes a specific data file and creates visualizations
of the specified type. The resulting visualizations are saved to the designated output
directory.

Args:
    data_dir (str): The path to the specific data file to be visualized. This should be a
        valid, non-empty string representing either an absolute or relative file path,
        such as "/output/a.py", "./data/data.csv", or "C:/Windows/data.json".
        
    visualize_type (str): The type of visualization to generate. Must be one of the
        following options:
        - "bar_chart": Creates a bar chart visualization.
        - "line_chart": Creates a line graph visualization.
        - "scatter_plot": Creates a scatter plot visualization.
        - "pie_chart": Creates a pie chart visualization.
        - "histogram": Creates a histogram visualization.
        - "3D_plot": Creates a 3D plot visualization.
        
    output_dir (str): The path to the directory where the visualization files will be saved.
        This should be a valid, non-empty string representing either an absolute or relative
        directory path, such as "/path/to/output", "./aa", or "D:/Results".
        
    output_format (str): The format for the output visualization files. Must be one of the
        following options:
        - "png": Portable Network Graphics format
        - "jpg": JPEG image format  
        - "pdf": Portable Document Format
        - "svg": Scalable Vector Graphics format

Returns:
    str: A success message confirming that the operation was completed successfully.

Raises:
    ValueError: If any of the parameters are missing or do not conform to the expected format.

Example:
    visualize_data("./data/data.csv", "bar_chart", "./outputs", "png")
    # Returns: "Operation succeed"
"""
```'''
    if not isinstance(data_dir, str) or not data_dir.strip():
        raise ValueError("Parameter 'data_dir' must be a non-empty string representing a valid file path.")
    if not isinstance(visualize_type, str) or not visualize_type.strip():
        raise ValueError("Parameter 'visualize_type' must be a non-empty string specifying visualization type.")
    valid_viz_types = ['bar_chart', 'line_chart', 'scatter_plot', 'pie_chart', 'histogram']
    if visualize_type not in valid_viz_types:
        raise ValueError(f"Parameter 'visualize_type' must be one of: {', '.join(valid_viz_types)}")
    if not isinstance(output_dir, str) or not output_dir.strip():
        raise ValueError("Parameter 'output_dir' must be a non-empty string representing a valid directory path.")
    if not isinstance(output_format, str) or not output_format.strip():
        raise ValueError("Parameter 'output_format' must be a non-empty string specifying output format.")
    valid_formats = ['png', 'jpg', 'pdf', 'svg']
    if output_format.lower() not in valid_formats:
        raise ValueError(f"Parameter 'output_format' must be one of: {', '.join(valid_formats)}")
    return 'Operation succeed'
if __name__ == '__main__':
    mcp.run(transport='stdio')