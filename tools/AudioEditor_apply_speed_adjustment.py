from mcp.server.fastmcp import FastMCP
mcp = FastMCP('AudioEditor_apply_speed_adjustment')

@mcp.tool()
def AudioEditor_apply_speed_adjustment(audio_file: str, speed_factor: str) -> str:
    '''```python
    """
    Adjusts the playback speed and pitch of an audio file.

    This function loads an audio file and modifies its playback speed based on
    the specified speed factor. The speed adjustment affects both the duration
    and pitch of the audio: increasing the speed raises the pitch and shortens
    the duration, while decreasing the speed lowers the pitch and lengthens the
    duration.

    Args:
        audio_file (str): The path to the audio file to be processed.
        speed_factor (str): The factor by which to adjust the speed. Values greater
            than 1.0 increase speed and pitch, reducing duration; values less than
            1.0 decrease speed and pitch, increasing duration. Common values include
            0.5 (half speed), 1.25 (25% faster), and 2.0 (double speed). Extreme values
            (< 0.25 or > 4.0) may result in poor audio quality.

    Returns:
        tuple: A tuple containing:
            - (sample_rate: int, speed_adjusted_audio_data: array): The sample rate and
              adjusted audio data, or None if an error occurred.
            - str: A status message indicating the speed factor applied, the change in
              duration, or error information.

    Note:
        For pitch-preserving speed changes, consider using time-stretching techniques.
        The function preserves the original sample rate but alters the audio duration.
    """
```'''
    mock_audio_db = {'url/to/audio.mp3': {'title': 'Dance Song Original', 'sample_rate': 44100, 'duration_seconds': 240, 'data': [0.1, 0.2, -0.1, -0.2] * 1000}, 'url/to/demo_song.mp3': {'title': 'Producer Demo Track', 'sample_rate': 48000, 'duration_seconds': 180, 'data': [0.05, 0.1, -0.05, -0.1] * 1200}}
    try:
        if not isinstance(audio_file, str) or audio_file.strip() == '':
            return (None, 'Error: Invalid audio_file path.')
        try:
            speed_factor_val = float(speed_factor)
        except ValueError:
            return (None, 'Error: speed_factor must be a numeric value.')
        if speed_factor_val <= 0:
            return (None, 'Error: speed_factor must be greater than 0.')
        if audio_file not in mock_audio_db:
            return (None, f"Error: Audio file '{audio_file}' not found in the system.")
        audio_info = mock_audio_db[audio_file]
        original_duration = audio_info['duration_seconds']
        sample_rate = audio_info['sample_rate']
        audio_data = audio_info['data']
        new_duration = original_duration / speed_factor_val
        adjusted_length = max(1, int(len(audio_data) / speed_factor_val))
        adjusted_audio_data = audio_data[:adjusted_length]
        if speed_factor_val > 1.0:
            effect_desc = 'increased speed and pitch (shorter duration)'
        elif speed_factor_val < 1.0:
            effect_desc = 'decreased speed and pitch (longer duration)'
        else:
            effect_desc = 'no change in speed or pitch'
        status_msg = f"Applied speed factor {speed_factor_val:.2f} to '{audio_info['title']}'. Original duration: {original_duration:.2f} sec, New duration: {new_duration:.2f} sec. Effect: {effect_desc}."
        return ((sample_rate, adjusted_audio_data), status_msg)
    except Exception as e:
        return (None, f'Unexpected error occurred: {str(e)}')
if __name__ == '__main__':
    mcp.run(transport='stdio')