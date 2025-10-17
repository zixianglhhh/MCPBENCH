from ast import Dict
from mcp.server.fastmcp import FastMCP
from typing import List

mcp = FastMCP('create_physics_scene')

@mcp.tool()
def create_physics_scene(objects: List[dict], floor: bool, gravity: str, scene_name: str) -> str:
    '''```python
    """
    Creates a physics scene with configurable parameters.

    This function initializes a physics scene using the specified objects, 
    floor presence, gravity vector, and scene name. The scene is set up 
    with a mock physics engine and is intended for simulations such as 
    robot obstacle avoidance.

    Args:
        objects (list of dict): A non-empty list of object definitions, 
            where each object is a dictionary containing:
            - 'type' (str): The type of the object.
            - 'position' (list of float): A list of three coordinates 
              representing the object's position in 3D space.
        floor (bool): A boolean indicating whether a floor should be 
            included in the scene.
        gravity (str): A string representing the gravity vector in the 
            format '[x, y, z]'. For example, '[0, -0.981, 0]'.
        scene_name (str): A non-empty string representing the name of 
            the scene.

    Returns:
        str: A message indicating successful creation of the physics 
        scene, including the scene name, number of objects, and gravity 
        vector.
    """
```'''
    mock_physics_scenes_db = getattr(create_physics_scene, '_mock_db', {})
    if not isinstance(objects, list) or len(objects) == 0:
        raise ValueError('`objects` must be a non-empty list of object definitions (dicts with type and position).')
    if not isinstance(floor, bool):
        raise ValueError('`floor` must be a boolean value.')
    if not isinstance(gravity, str):
        raise ValueError("`gravity` must be a string representing a vector, e.g., '[0, -0.981, 0]'.")
    if not isinstance(scene_name, str) or not scene_name.strip():
        raise ValueError('`scene_name` must be a non-empty string.')
    try:
        gravity_vector = eval(gravity) if gravity.strip().startswith('[') else [0, -0.981, 0]
        if not (isinstance(gravity_vector, list) and len(gravity_vector) == 3):
            raise ValueError
    except Exception:
        raise ValueError("`gravity` must be a string representing a 3D vector, e.g., '[0, -0.981, 0]'.")
    validated_objects = []
    for obj in objects:
        if not isinstance(obj, dict) or 'type' not in obj or 'position' not in obj:
            raise ValueError("Each object must be a dict with 'type' and 'position'.")
        if not isinstance(obj['type'], str):
            raise ValueError("Object 'type' must be a string.")
        if not (isinstance(obj['position'], list) and len(obj['position']) == 3):
            raise ValueError("Object 'position' must be a list of 3 coordinates.")
        validated_objects.append(obj)
    scene_data = {'name': scene_name, 'gravity': gravity_vector, 'floor': floor, 'objects': validated_objects, 'engine': 'MockPhysicsEngine v1.0', 'status': 'initialized', 'metadata': {'created_for': 'robot_obstacle_avoidance_simulation', 'supports_autonomous_decision_making': True, 'integrated_with': ['MATLAB', 'Java Simulation Software']}}
    mock_physics_scenes_db[scene_name] = scene_data
    setattr(create_physics_scene, '_mock_db', mock_physics_scenes_db)
    return f"Physics scene '{scene_name}' created successfully with {len(validated_objects)} objects and gravity {gravity_vector}."
if __name__ == '__main__':
    mcp.run(transport='stdio')