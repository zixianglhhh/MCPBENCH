from mcp.server.fastmcp import FastMCP
mcp = FastMCP('detect_objects')

@mcp.tool()
def detect_objects(image_path: str) -> str:
    '''```python
    """
    Performs object detection on a given image to identify and localize objects of interest.

    This function processes an input image specified by its file path, detecting objects such as 
    people, vehicles, or items. It returns details including bounding boxes, object classes, and 
    confidence scores for each detected object. These outputs can be used for further analysis, 
    such as cropping regions of interest.

    Args:
        image_path (str): The file path to the input image. Must be a non-empty string.

    Returns:
        str: A formatted string listing detected objects with their bounding boxes, classes, 
        and confidence scores. The bounding box coordinates are provided as [x_left, y_top, x_right, y_bottom]
        where (x_left, y_top) is the top-left corner and (x_right, y_bottom) is the bottom-right corner.
        If no objects are detected or the image path is unknown, an appropriate message is returned.
    """
```'''
    mock_detection_db = {'street_scene_people.jpg': [{'bbox': [50, 80, 180, 400], 'class': 'person', 'confidence': 0.95}, {'bbox': [220, 60, 350, 390], 'class': 'person', 'confidence': 0.92}, {'bbox': [400, 100, 520, 420], 'class': 'person', 'confidence': 0.88}]}
    if not isinstance(image_path, str) or not image_path.strip():
        return "Error: 'image_path' must be a non-empty string."
    detections = mock_detection_db.get(image_path)
    if detections is None:
        return f"No objects detected or unknown image for path '{image_path}'."
    output_lines = ['Detected objects:']
    for det in detections:
        bbox_str = f"bbox={det['bbox']}"
        class_str = f"class='{det['class']}'"
        conf_str = f"confidence={det['confidence']:.2f}"
        output_lines.append(f' - {class_str}, {bbox_str}, {conf_str}')
    return '\n'.join(output_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')