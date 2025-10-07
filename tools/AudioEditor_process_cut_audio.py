from mcp.server.fastmcp import FastMCP
mcp = FastMCP('AudioEditor_process_cut_audio')

@mcp.tool()
def AudioEditor_process_cut_audio(audio_file: str, start_time: str) -> str:
    '''```python
"""
Processes the cutting of an audio file to extract a segment starting from a specified time.

This function takes an audio file and a start time in seconds, then extracts a segment 
beginning at the specified start time. The output is saved as a new audio file.

Args:
    audio_file (str): The file path to the audio file to be processed. It must be a non-empty string.
    start_time (str): The start time for the audio cut in seconds, represented as a string 
                      (e.g., "10.5" for 10.5 seconds). It must be a non-negative numeric value.

Returns:
    str: A success message confirming the completion of the audio cutting operation, including 
         the start time of the extracted segment and the path to the newly created audio file.
"""
```'''
    if not isinstance(audio_file, str) or not audio_file.strip():
        return "Error: 'audio_file' must be a non-empty string."
    try:
        start_time_val = float(start_time)
    except ValueError:
        return 'Error: Start time must be a numeric value.'
    if start_time_val < 0:
        return 'Error: Start time cannot be negative.'
    import os
    base_name = os.path.splitext(os.path.basename(audio_file))[0]
    output_path = f'./outputs/audio_processed/{base_name}_from_{start_time_val:.2f}s.mp3'
    return f'Audio cutting operation completed successfully. Extracted segment starting from {start_time_val:.2f}s. File created at: {output_path}'
if __name__ == '__main__':
    mcp.run(transport='stdio')