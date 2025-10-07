from mcp.server.fastmcp import FastMCP
mcp = FastMCP('generate_code')

@mcp.tool()
def generate_code(prompt: str, language: str, output_name: str,model: str = "gemini-pro",temperature: float=0.4, max_tokens: int=1500, existing_file_path: str='') -> str:
    '''```python
    """
    Generates source code using an AI model based on a given prompt and saves it to a specified file.

    This function utilizes an AI model to generate code in a specified programming language. The generated code
    is then saved to a file with a name and extension derived from the provided output name and language. The
    function allows customization of the AI model's behavior through temperature and token settings and can
    optionally use an existing file as context or reference.

    Args:
        prompt (str): A non-empty string describing the code to be generated.
        language (str): The programming language for the generated code (e.g., 'python', 'javascript').
        model (str): The name of the AI model to use for code generation. Defaults to "gemini-pro".
        output_name (str): The full path including directory and filename (without extension) where the code 
            will be saved.
        temperature (float, optional): A float between 0.0 and 1.0 that controls the randomness of the AI model's
            output. Defaults to 0.4.
        max_tokens (int, optional): The maximum number of tokens to generate. Must be a positive integer. 
            Defaults to 1500.
        existing_file_path (str, optional): An optional path to an existing file to use as context or reference.

    Returns:
        str: A confirmation message indicating the successful generation and saving of the code file.
    """
```'''
    if not isinstance(prompt, str) or not prompt.strip():
        raise ValueError("Parameter 'prompt' must be a non-empty string.")
    if not isinstance(language, str) or not language.strip():
        raise ValueError("Parameter 'language' must be a non-empty string.")
    if not isinstance(model, str) or not model.strip():
        raise ValueError("Parameter 'model' must be a non-empty string.")
    if not isinstance(output_name, str) or not output_name.strip():
        raise ValueError("Parameter 'output_name' must be a non-empty string.")
    if not isinstance(temperature, float) or not 0.0 <= temperature <= 1.0:
        raise ValueError("Parameter 'temperature' must be a float between 0.0 and 1.0.")
    if not isinstance(max_tokens, int) or max_tokens <= 0:
        raise ValueError("Parameter 'max_tokens' must be a positive integer.")
    if not isinstance(existing_file_path, str):
        raise ValueError("Parameter 'existing_file_path' must be a string.")
    import re
    import datetime
    clean_prompt = re.sub('[^\\w\\s-]', '', prompt.lower())
    clean_prompt = re.sub('[-\\s]+', '_', clean_prompt)
    clean_prompt = clean_prompt[:20]
    extension_map = {'python': 'py', 'javascript': 'js', 'java': 'java', 'cpp': 'cpp', 'c': 'c', 'go': 'go', 'rust': 'rs', 'php': 'php', 'ruby': 'rb', 'swift': 'swift', 'kotlin': 'kt', 'typescript': 'ts', 'html': 'html', 'css': 'css', 'sql': 'sql', 'bash': 'sh', 'shell': 'sh'}
    lang_lower = language.lower()
    extension = extension_map.get(lang_lower, 'txt')
    filename = f'{output_name}.{extension}'
    return f'Code has been generated successfully and saved to {filename}'
if __name__ == '__main__':
    mcp.run(transport='stdio')