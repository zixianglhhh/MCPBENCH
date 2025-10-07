from mcp.server.fastmcp import FastMCP
mcp = FastMCP('modify_object')

@mcp.tool()
def modify_object(target_object: str, location: str, rotation: str, scale: str, visible: str) -> str:
    '''```python
    """
    Modifies the properties of a specified object within a scene.

    This function updates the location, rotation, scale, and visibility attributes
    of the given object. If the object is a 'bird', additional adjustments are made
    to its location to ensure it maintains a safe distance from the 'sun' object.

    Args:
        target_object (str): The name of the object to be modified.
        location (str): The new location of the object in the format 'x,y,z'.
        rotation (str): The new rotation of the object in the format 'x,y,z'.
        scale (str): The new scale of the object in the format 'x,y,z'.
        visible (str): The visibility status of the object, either 'true' or 'false'.

    Returns:
        str: A message indicating the success of the modification, with additional
        notes if natural flight adjustments were applied to a 'bird' object.
    """
```'''
    mock_scene_objects = {'bird': {'location': '0,0,10', 'rotation': '0,0,0', 'scale': '1,1,1', 'visible': 'true'}, 'sun': {'location': '50,200,300', 'rotation': '0,45,0', 'scale': '10,10,10', 'visible': 'true'}, 'tree': {'location': '10,20,0', 'rotation': '0,0,0', 'scale': '3,3,3', 'visible': 'true'}}
    for (param_target_object, param_value) in {'target_object': target_object, 'location': location, 'rotation': rotation, 'scale': scale, 'visible': visible}.items():
        if not isinstance(param_value, str) or not param_value.strip():
            raise ValueError(f"Invalid value for '{param_target_object}': must be a non-empty string.")
    if target_object not in mock_scene_objects:
        raise ValueError(f"Object '{target_object}' not found in the scene.")
    mock_scene_objects[target_object]['location'] = location
    mock_scene_objects[target_object]['rotation'] = rotation
    mock_scene_objects[target_object]['scale'] = scale
    mock_scene_objects[target_object]['visible'] = visible
    if target_object == 'bird':
        sun_loc = [float(c) for c in mock_scene_objects['sun']['location'].split(',')]
        bird_loc = [float(c) for c in location.split(',')]
        distance_to_sun = ((bird_loc[0] - sun_loc[0]) ** 2 + (bird_loc[1] - sun_loc[1]) ** 2) ** 0.5
        if distance_to_sun < 50:
            bird_loc[0] += 10
            location = ','.join(map(str, bird_loc))
            mock_scene_objects[target_object]['location'] = location
        adaptation_note = " Bird's flight speed adapted to avoid sun proximity."
        return f"Object '{target_object}' modified successfully with natural flight adjustments.{adaptation_note}"
    return f"Object '{target_object}' modified successfully."

if __name__ == '__main__':
    mcp.run(transport='stdio')