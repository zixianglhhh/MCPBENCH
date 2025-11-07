from mcp.server.fastmcp import FastMCP
mcp = FastMCP('AudioEditor_process_cut_audio')

@mcp.tool()
def AudioEditor_process_cut_audio(audio_file: str, start_time: str, end_time: str) -> str:
    '''```python
"""
Cuts an audio file to extract a segment from a specified start time to end time.

This function takes an audio file along with start and end times in seconds, then extracts the
segment beginning at the start time and ending at the end time. The output is saved as a new
audio file.

Args:
    audio_file (str): The file path to the audio file to be processed. It must be a non-empty string.
    start_time (str): The start time for the audio cut in seconds, represented as a string
                      (e.g., "10.5" for 10.5 seconds). It must be a non-negative numeric value.
    end_time (str):   The end time for the audio cut in seconds, represented as a string. It must be
                      a numeric value greater than the start time.

Returns:
    str: A success message confirming the completion of the audio cutting operation, including
         the start and end time of the extracted segment and the path to the newly created audio file.
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
    try:
        end_time_val = float(end_time)
    except ValueError:
        return 'Error: End time must be a numeric value.'
    if end_time_val < 0:
        return 'Error: End time cannot be negative.'
    if end_time_val <= start_time_val:
        return 'Error: End time must be greater than start time.'
    import os
    base_name = os.path.splitext(os.path.basename(audio_file))[0]
    output_path = f'./outputs/audio_processed/{base_name}_from_{start_time_val:.2f}s_to_{end_time_val:.2f}s.mp3'
    return (
        f'Audio cutting operation completed successfully. Extracted segment from '
        f'{start_time_val:.2f}s to {end_time_val:.2f}s. File created at: {output_path}'
    )
if __name__ == '__main__':
    mcp.run(transport='stdio')