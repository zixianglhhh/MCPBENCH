from mcp.server.fastmcp import FastMCP
mcp = FastMCP('AudioEditor_transcribe_audio_sync')

@mcp.tool()
def AudioEditor_transcribe_audio_sync(audio_file: str) -> str:
    '''```python
    """
    Synchronously transcribe an audio file using AI-powered speech recognition.

    This function serves as a synchronous wrapper around the asynchronous transcription process,
    converting audio files to text using advanced speech recognition technology. It manages the 
    async/await complexity internally and returns detailed transcription results, including the 
    full text, timestamped segments, language detection, and processing statistics.

    Args:
        audio_file (str): The path to the audio file to be transcribed. Must be a non-empty string.

    Returns:
        tuple: A tuple containing four elements:
            - status (str): A status message indicating success with language and processing time,
              or error information if transcription failed.
            - full_text (str): The complete transcription as plain text, or an empty string on error.
            - segments_formatted (str): Formatted text showing timestamped segments with start/end 
              times and confidence scores, or an empty string on error.
            - json_formatted (str): A pretty-formatted JSON string containing complete transcription 
              data, including word-level timestamps and metadata, or an empty string on error.

    Notes:
        - Automatically detects the language in the audio file.
        - Provides word-level and segment-level timestamps for precise audio editing.
        - Returns confidence scores for quality assessment.
        - Handles various audio formats and sample rates automatically.
        - Processing time depends on audio length and complexity.
        - All timestamps are provided in seconds with decimal precision.
        - Function blocks until transcription is complete (synchronous).
        - For asynchronous usage, use process_transcription() directly instead.
    """
```'''
    mock_audio_db = {'url/to/audio.mp3': {'filename': 'demo_song.mp3', 'language': 'en', 'duration_sec': 185.4, 'full_text': "Walking down the midnight road, chasing dreams I've never known.\nEvery step a story told, in the rhythm of my own.", 'segments': [{'start': 0.0, 'end': 9.5, 'text': "Walking down the midnight road, chasing dreams I've never known.", 'confidence': 0.96, 'words': [{'word': 'Walking', 'start': 0.0, 'end': 0.6, 'confidence': 0.98}, {'word': 'down', 'start': 0.61, 'end': 0.85, 'confidence': 0.97}, {'word': 'the', 'start': 0.86, 'end': 0.95, 'confidence': 0.99}, {'word': 'midnight', 'start': 0.96, 'end': 1.32, 'confidence': 0.94}, {'word': 'road,', 'start': 1.33, 'end': 1.62, 'confidence': 0.95}, {'word': 'chasing', 'start': 1.63, 'end': 1.92, 'confidence': 0.93}, {'word': 'dreams', 'start': 1.93, 'end': 2.22, 'confidence': 0.92}, {'word': "I've", 'start': 2.23, 'end': 2.35, 'confidence': 0.97}, {'word': 'never', 'start': 2.36, 'end': 2.55, 'confidence': 0.96}, {'word': 'known.', 'start': 2.56, 'end': 2.84, 'confidence': 0.94}]}, {'start': 9.6, 'end': 18.3, 'text': 'Every step a story told, in the rhythm of my own.', 'confidence': 0.95, 'words': [{'word': 'Every', 'start': 9.6, 'end': 9.8, 'confidence': 0.96}, {'word': 'step', 'start': 9.81, 'end': 10.0, 'confidence': 0.95}, {'word': 'a', 'start': 10.01, 'end': 10.05, 'confidence': 0.99}, {'word': 'story', 'start': 10.06, 'end': 10.34, 'confidence': 0.94}, {'word': 'told,', 'start': 10.35, 'end': 10.6, 'confidence': 0.93}, {'word': 'in', 'start': 10.61, 'end': 10.7, 'confidence': 0.97}, {'word': 'the', 'start': 10.71, 'end': 10.8, 'confidence': 0.98}, {'word': 'rhythm', 'start': 10.81, 'end': 11.15, 'confidence': 0.92}, {'word': 'of', 'start': 11.16, 'end': 11.25, 'confidence': 0.98}, {'word': 'my', 'start': 11.26, 'end': 11.35, 'confidence': 0.96}, {'word': 'own.', 'start': 11.36, 'end': 11.58, 'confidence': 0.94}]}], 'processing_time_sec': 3.45}}
    if not isinstance(audio_file, str) or not audio_file.strip():
        return ('Error: Invalid audio_file parameter. Must be a non-empty string.', '', '', '')
    if audio_file not in mock_audio_db:
        return (f"Error: Audio file '{audio_file}' not found in transcription database.", '', '', '')
    data = mock_audio_db[audio_file]
    segments_formatted = ''
    for seg in data['segments']:
        segments_formatted += f"[{seg['start']:.2f}s - {seg['end']:.2f}s] (conf: {seg['confidence']:.2f}): {seg['text']}\n"
    import json
    json_formatted = json.dumps({'filename': data['filename'], 'language': data['language'], 'duration_sec': data['duration_sec'], 'full_text': data['full_text'], 'segments': data['segments'], 'processing_time_sec': data['processing_time_sec']}, indent=2)
    status = f"Success: Transcription completed in {data['processing_time_sec']:.2f}s (Language detected: {data['language']})"
    return (status, data['full_text'], segments_formatted.strip(), json_formatted)
if __name__ == '__main__':
    mcp.run(transport='stdio')