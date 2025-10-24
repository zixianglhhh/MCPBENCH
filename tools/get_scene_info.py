from mcp.server.fastmcp import FastMCP
mcp = FastMCP('get_scene_info')

@mcp.tool()
def get_scene_info(scene_name: str) -> str:
    '''```python
    """
    Retrieve information about a specified SketchUp scene.

    This function fetches details about a given scene within a SketchUp project.
    The scene information includes environment settings, lighting conditions,
    weather, objects present in the scene, and camera configuration.

    Args:
        scene_name (str): The name of the scene to retrieve information for. 
                          Must be a non-empty string.

    Returns:
        str: A formatted string containing the scene information in JSON format.
             If the scene is not found or an error occurs, an error message is returned.
    """
```'''
    mock_scenes_db = {'SkyView': {'environment': 'outdoor', 'sun_position': {'azimuth': 135.0, 'altitude': 45.0}, 'lighting': 'daylight', 'weather': 'clear', 'objects': [{'name': 'bird_01', 'type': 'animal', 'appearance': {'body_color': 'brown', 'wing_color': 'blue'}, 'behavior': {'flight_pattern': 'random', 'interaction': 'avoids_sun', 'speed_mode': 'dynamic'}}, {'name': 'tree_cluster', 'type': 'vegetation', 'species': 'oak', 'count': 12}], 'camera': {'position': [0, 0, 10], 'target': [50, 50, 0], 'fov': 60}}, 'InteriorRoom': {'environment': 'indoor', 'lighting': 'artificial', 'weather': None, 'objects': [{'name': 'desk', 'type': 'furniture', 'material': 'wood'}], 'camera': {'position': [2, 1.5, 1.7], 'target': [0, 0, 0], 'fov': 45}}}
    if not isinstance(scene_name, str) or not scene_name.strip():
        return "Error: 'scene_name' must be a non-empty string."
    scene_data = mock_scenes_db.get(scene_name)
    if not scene_data:
        return f"Error: Scene '{scene_name}' not found in the SketchUp project."
    import json
    try:
        scene_info_str = json.dumps(scene_data, indent=2)
    except (TypeError, ValueError) as e:
        return f'Error: Failed to serialize scene data. Details: {str(e)}'
    return f"Scene Information for '{scene_name}':\n{scene_info_str}"
if __name__ == '__main__':
    mcp.run(transport='stdio')