from mcp.server.fastmcp import FastMCP
mcp = FastMCP('create_object')

@mcp.tool()
def create_object(object_type: str, name: str, location: list, size: list) -> str:
    '''```python
    """
    Creates a 3D object of specified type with given attributes.

    This function supports creating various types of 3D objects, including 
    cubes, spheres, planes, birds, and custom objects. Each object is 
    characterized by its type, name, location, and size, and may have 
    additional properties based on its type.

    Args:
        object_type (str): The type of the 3D object to create. Must be one of 
            'cube', 'sphere', 'plane', 'bird', or 'custom'.
        name (str): The name of the 3D object. Must be a non-empty string and 
            unique among existing objects.
        location (list or tuple): The (x, y, z) coordinates specifying the 
            object's location. Must be a list or tuple of three numbers.
        size (int, float, list, or tuple): The size of the object. Can be a 
            single number or a list/tuple of dimensions.

    Returns:
        str: A confirmation message indicating successful creation of the 3D 
        object with its name, type, location, and size.
    """
```'''
    if not hasattr(create_object, 'mock_db'):
        create_object.mock_db = {'objects': []}
    valid_types = {'cube', 'sphere', 'plane', 'bird', 'custom'}
    if not isinstance(object_type, str) or object_type.lower() not in valid_types:
        raise ValueError(f"Invalid object_type '{object_type}'. Must be one of {valid_types}.")
    if not isinstance(name, str) or not name.strip():
        raise ValueError('Invalid name. Name must be a non-empty string.')
    if not isinstance(location, (list, tuple)) or len(location) != 3 or (not all((isinstance(coord, (int, float)) for coord in location))):
        raise ValueError('Invalid location. Must be a list/tuple of three numbers (x, y, z).')
    if not isinstance(size, (int, float, list, tuple)):
        raise ValueError('Invalid size. Must be a number or list/tuple of dimensions.')
    if isinstance(size, (list, tuple)) and (not all((isinstance(s, (int, float)) for s in size))):
        raise ValueError('Invalid size dimensions. All elements must be numbers.')
    for obj in create_object.mock_db['objects']:
        if obj['name'].lower() == name.lower():
            raise ValueError(f"An object named '{name}' already exists.")
    obj_data = {'type': object_type.lower(), 'name': name, 'location': tuple(location), 'size': size, 'properties': {}}
    if object_type.lower() == 'bird':
        obj_data['properties'] = {'color': {'body': 'brown', 'wings': 'blue'}, 'behavior': {'flight_pattern': 'natural random', 'avoids_sun': True, 'speed_dynamic': True, 'sun_interaction': 'adjust trajectory to avoid sun proximity'}}
    elif object_type.lower() == 'cube':
        obj_data['properties'] = {'material': 'default', 'shading': 'smooth'}
    elif object_type.lower() == 'sphere':
        obj_data['properties'] = {'material': 'glossy', 'segments': 32}
    elif object_type.lower() == 'plane':
        obj_data['properties'] = {'material': 'matte', 'subdivisions': 1}
    else:
        obj_data['properties'] = {'material': 'custom', 'notes': 'Custom object created for special use'}
    create_object.mock_db['objects'].append(obj_data)
    return f"3D object '{name}' of type '{object_type}' created successfully at {location} with size {size}."
if __name__ == '__main__':
    mcp.run(transport='stdio')