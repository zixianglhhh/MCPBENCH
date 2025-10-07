from mcp.server.fastmcp import FastMCP
mcp = FastMCP('AudioEditor_apply_fades')

@mcp.tool()
def AudioEditor_apply_fades(audio_file: str, fade_in_ms: str, fade_out_ms: str) -> str:
    '''```python
    """
    Applies fade-in and fade-out effects to an audio file and saves the processed file.

    This function processes an audio file by applying specified fade-in and fade-out 
    effects, measured in milliseconds. The processed audio file is saved in the 
    './outputs/audio_processed/' directory with a modified filename indicating the 
    applied effects.

    Args:
        audio_file (str): The path to the audio file to be processed. Must be a 
            non-empty string.
        fade_in_ms (str): The duration of the fade-in effect in milliseconds. Must 
            be a non-negative integer represented as a string.
        fade_out_ms (str): The duration of the fade-out effect in milliseconds. Must 
            be a non-negative integer represented as a string.

    Returns:
        str: A success message confirming the applied fade effects and the location 
        where the processed audio file is saved. If input validation fails, an error 
        message is returned.
    """
```'''
    if not isinstance(audio_file, str) or not audio_file.strip():
        return "Error: 'audio_file' must be a non-empty string."
    try:
        fade_in_ms_val = int(fade_in_ms)
        fade_out_ms_val = int(fade_out_ms)
    except ValueError:
        return "Error: 'fade_in_ms' and 'fade_out_ms' must be integers (milliseconds)."
    if fade_in_ms_val < 0 or fade_out_ms_val < 0:
        return 'Error: Fade durations cannot be negative.'
    import os
    base_name = os.path.splitext(os.path.basename(audio_file))[0]
    output_path = f'./outputs/audio_processed/{base_name}_faded.mp3'
    fade_effects = []
    if fade_in_ms_val > 0:
        fade_effects.append(f'fade-in: {fade_in_ms_val}ms')
    if fade_out_ms_val > 0:
        fade_effects.append(f'fade-out: {fade_out_ms_val}ms')
    if not fade_effects:
        fade_description = 'No fade effects applied'
    else:
        fade_description = 'Applied ' + ' and '.join(fade_effects)
    return f'Audio fade effects applied successfully. {fade_description}. Processed audio saved to: {output_path}'
if __name__ == '__main__':
    mcp.run(transport='stdio')