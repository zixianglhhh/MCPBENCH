from mcp.server.fastmcp import FastMCP
from typing import Union, List
mcp = FastMCP('request_api_schema')

@mcp.tool()
def request_api_schema(ApiName: Union[str, List[str]]) -> str:
    '''```python
    """
    Retrieves the API request schema(s) for specified API name(s).

    This function accepts either a single API name as a string or a list of API names.
    It returns the corresponding request schema(s) for the provided API name(s).
    If a single API name is provided, a single schema is returned. If a list of API
    names is provided, multiple schemas are returned.

    Args:
        ApiName (Union[str, List[str]]): A single API name as a string or a list of
            API names. Each name should be a non-empty string.
            Each word in the API name should be capitalized.
            For Example, 'Image Object Detection API'

    Returns:
        str: A formatted string containing the API schema(s). If no schema is found
        for a given API name, an error message is included. If multiple API names
        are provided, the result includes all found schemas and any warnings for
        missing schemas.
    """
```'''
    mock_api_schemas = {
        'Image Object Detection API': {
            'description': 'Detects objects in an image from a provided image URL and returns an updated image with bounding boxes around detected objects. Optionally returns JSON metadata of detections.',
            'endpoint': 'POST https://api.example.com/v1/object-detection',
            'request_schema': {
                'image_url': 'string (URL to the image to process)',
                'return_json': 'boolean (optional, if true returns detection metadata)'
            }
        },
        'City Earthquake Data API': {
            'description': 'Retrieves all earthquakes in a given city within the last 30 days.',
            'endpoint': 'GET https://api.example.com/v1/earthquakes',
            'request_schema': {
                'city': 'string (name of the city)',
                'days': 'integer (optional, default 30)'
            }
        },
        'Microsoft Translator Text API': {
            'description': 'Provides translation services and lists supported languages.',
            'endpoint': 'GET https://api.cognitive.microsofttranslator.com/languages',
            'request_schema': {
                'scope': "string (optional, e.g., 'translation', 'transliteration', 'dictionary')"
            }
        },
        'Simple & Elegant Translation Service API': {
            'description': 'Lightweight translation API supporting multiple languages.',
            'endpoint': 'GET https://api.simpletranslate.com/v1/languages',
            'request_schema': {
                'format': "string (optional, e.g., 'json', 'xml')"
            }
        },
        'LanguageTool API': {
            'description': 'Grammar, style, and spell checking for multiple languages.',
            'endpoint': 'GET https://api.languagetool.org/v2/languages',
            'request_schema': {
                'api_key': 'string (optional, if required for premium usage)'
            }
        },
        'Vision Detect 3D API': {
            'description': 'Performs high-accuracy 3D object detection on input data (image sets, depth maps, or point clouds). Returns detected objects with 3D bounding boxes and annotated previews.',
            'endpoint': 'POST https://api.example.com/v1/vision-detect-3d',
            'request_schema': {
                'input_type': "string (required, one of: 'image_set', 'depth_map', 'point_cloud')",
                'data_url': 'string (URL pointing to the 3D data or file to process)',
                'confidence_threshold': 'float (optional, default 0.5, threshold for valid detections)',
                'return_3d_preview': 'boolean (optional, if true returns a rendered 3D visualization with highlighted bounding volumes)'
            }
        },
        'OCR Text Extract API': {
            'description': 'Extracts readable text from image/URL using OCR; returns plain text and layout hints.',
            'endpoint': 'POST https://api.example.com/v1/ocr-extract',
            'request_schema': {
                'image_url': 'string (URL to the image to extract text from)',
                'language_hint': 'string (optional, ISO code for expected text language)'
            }
        },
        'USGS Earthquake Feed API (Mock)': {
            'description': 'Query recent earthquakes by region, magnitude, and time window.',
            'endpoint': 'GET https://api.example.com/v1/usgs-quakes',
            'request_schema': {
                'region': 'string (optional, geographic region filter)',
                'min_magnitude': 'float (optional, minimum magnitude to filter)',
                'start_date': 'string (optional, start date in YYYY-MM-DD)',
                'end_date': 'string (optional, end date in YYYY-MM-DD)'
            }
        },
        'Grammarify Proofread API (Mock)': {
            'description': 'Proofreading and grammar correction for multilingual text.',
            'endpoint': 'POST https://api.example.com/v1/grammarify',
            'request_schema': {
                'text': 'string (the text content to proofread)',
                'language': "string (ISO language code, e.g., 'en', 'fr')",
                'return_suggestions': 'boolean (optional, default true, include correction suggestions)'
            }
        },
        'Ecommerce API': {
            'description': 'API for managing e-commerce operations including products, orders, and customers.',
            'endpoint': 'https://api.ecommerce.com/v1/',
            'request_schema': {
                'product_id': 'string (ID of the product)',
                'order_id': 'string (ID of the order)',
                'customer_id': 'string (ID of the customer)',
                'action': "string (action to perform, e.g., 'create', 'update', 'delete')"
            }
        }
    }
    if isinstance(ApiName, str):
        if not ApiName.strip():
            return "Error: 'ApiName' must be a non-empty string."
        api_names = [ApiName.strip()]
        is_single = True
    elif isinstance(ApiName, list):
        if not ApiName:
            return "Error: 'ApiName' list cannot be empty."
        api_names = [name.strip() for name in ApiName if isinstance(name, str) and name.strip()]
        if not api_names:
            return "Error: 'ApiName' list must contain non-empty strings."
        is_single = False
    else:
        return "Error: 'ApiName' must be either a string or a list of strings."
    results = []
    errors = []
    for api_name in api_names:
        schema = mock_api_schemas.get(api_name)
        if not schema:
            errors.append(f"No schema found for '{api_name}'")
        else:
            schema_info = f"API Name: {api_name}\nDescription: {schema['description']}\nEndpoint: {schema['endpoint']}\nRequest Schema: {schema['request_schema']}"
            results.append(schema_info)
    if not results:
        return f"Error: {', '.join(errors)}"
    if is_single:
        if errors:
            return f"Warning: {', '.join(errors)}\n\n{results[0]}"
        return results[0]
    else:
        output_lines = [f'Found {len(results)} API schema(s):']
        for (i, result) in enumerate(results, 1):
            output_lines.append(f'\n--- Schema {i} ---')
            output_lines.append(result)
        if errors:
            output_lines.append(f"\nWarnings: {', '.join(errors)}")
        return '\n'.join(output_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')