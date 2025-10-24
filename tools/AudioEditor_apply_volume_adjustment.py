from mcp.server.fastmcp import FastMCP
mcp = FastMCP('AudioEditor_apply_volume_adjustment')

@mcp.tool()
def AudioEditor_apply_volume_adjustment(audio_file: str, volume_adjustment: str) -> str:
    '''```python
    """
    Adjusts the volume of an audio file by applying a specified gain in decibels.

    This function modifies the audio file's volume based on the provided gain value,
    which is specified in decibels. Positive values increase the volume, while negative
    values decrease it.

    Args:
        audio_file (str): The file path to the audio file that will be processed. 
                          Must be a non-empty string.
        volume_adjustment (str): The gain adjustment in decibels. This should be a 
                                 string representing a numeric value (e.g., "3.0" for 
                                 +3dB, "-2.0" for -2dB).

    Returns:
        str: A success message indicating the completion of the volume adjustment 
             operation, including the applied gain value.
    """
```'''
    if not isinstance(audio_file, str) or not audio_file.strip():
        return "Error: 'audio_file' must be a non-empty string."
    try:
        volume_adjustment_val = float(volume_adjustment)
    except ValueError:
        return "Error: 'volume_adjustment' must be a numeric value."
    return f'Volume adjustment operation completed successfully. Applied {volume_adjustment_val:+.1f} dB gain to audio file.'
if __name__ == '__main__':
    mcp.run(transport='stdio')