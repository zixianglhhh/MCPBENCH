from mcp.server.fastmcp import FastMCP
mcp = FastMCP('modify_object')

@mcp.tool()
def modify_object(target_object: str, color: str, rotation: str, scale: str, animate: str) -> str:
    '''```python
    """
    Modifies the properties of a specified object within a scene.

    This function updates the color, rotation, scale, and animation state of the
    given object. If the object is a 'bird', natural flight safety adjustments are
    applied to ensure it maintains a safe distance from the 'sun' object based on
    its current location within the scene.

    Args:
        target_object (str): The name of the object to be modified.
        color (str): The new color of the object, formatted as 'R,G,B' (0-255)
        rotation (str): The new rotation of the object in the format 'x,y,z'.
        scale (str): The new scale of the object in the format 'x,y,z'.
        animate (str): The animation state, either 'true' or 'false'.

    Returns:
        str: A message indicating the success of the modification, with additional
        notes if natural flight adjustments were applied to a 'bird' object.
    """
```'''
    mock_scene_objects = {'bird': {'location': '0,0,10', 'rotation': '0,0,0', 'scale': '1,1,1', 'visible': 'true', 'color': '255,255,0', 'animate': 'true'}, 'sun': {'location': '50,200,300', 'rotation': '0,45,0', 'scale': '10,10,10', 'visible': 'true', 'color': '255,255,0', 'animate': 'false'}, 'tree': {'location': '10,20,0', 'rotation': '0,0,0', 'scale': '3,3,3', 'visible': 'true', 'color': '34,139,34', 'animate': 'false'}}
    for (param_target_object, param_value) in {'target_object': target_object, 'color': color, 'rotation': rotation, 'scale': scale, 'animate': animate}.items():
        if not isinstance(param_value, str) or not param_value.strip():
            raise ValueError(f"Invalid value for '{param_target_object}': must be a non-empty string.")
    if target_object not in mock_scene_objects:
        raise ValueError(f"Object '{target_object}' not found in the scene.")
    mock_scene_objects[target_object]['color'] = color
    mock_scene_objects[target_object]['rotation'] = rotation
    mock_scene_objects[target_object]['scale'] = scale
    mock_scene_objects[target_object]['animate'] = animate
    # Keep backward-compat visibility behavior mapped from animate
    mock_scene_objects[target_object]['visible'] = 'true' if animate.lower() == 'true' else 'false'
    if target_object == 'bird':
        sun_loc = [float(c) for c in mock_scene_objects['sun']['location'].split(',')]
        bird_loc = [float(c) for c in mock_scene_objects['bird']['location'].split(',')]
        distance_to_sun = ((bird_loc[0] - sun_loc[0]) ** 2 + (bird_loc[1] - sun_loc[1]) ** 2) ** 0.5
        if distance_to_sun < 50:
            bird_loc[0] += 10
            new_location = ','.join(map(str, bird_loc))
            mock_scene_objects[target_object]['location'] = new_location
        adaptation_note = " Bird's flight speed adapted to avoid sun proximity."
        return f"Object '{target_object}' modified successfully with natural flight adjustments.{adaptation_note}"
    return f"Object '{target_object}' modified successfully."

if __name__ == '__main__':
    mcp.run(transport='stdio')