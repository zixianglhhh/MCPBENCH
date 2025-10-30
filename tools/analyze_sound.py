from mcp.server.fastmcp import FastMCP

mcp = FastMCP("analyze_sound")

@mcp.tool()
def analyze_sound(filepath: str) -> str:
    '''```python
    """
    Return basic properties for a given sound file key from a mock database.

    This tool simulates audio metadata lookup (duration, sample rate, channels, genre) using an in-memory
    example dataset. It validates the provided key and returns a formatted response if found.

    Args:
        filepath (str): Identifier or filename key to look up (e.g., "song1.mp3").

    Returns:
        str: A formatted block including duration, sample rate, channels, and genre. Returns an error message if
        the key is empty or not found in the mock database.
    """
    ```'''
    # Mock database simulating the sound file properties
    mock_sound_database = {
        "song1.mp3": {
            "duration": "3:45",
            "sample_rate": "44100 Hz",
            "channels": "2 (Stereo)",
            "genre": "Rock"
        },
        "song2.wav": {
            "duration": "5:12",
            "sample_rate": "48000 Hz",
            "channels": "2 (Stereo)",
            "genre": "Jazz"
        },
        "song3.aac": {
            "duration": "4:01",
            "sample_rate": "44100 Hz",
            "channels": "1 (Mono)",
            "genre": "Classical"
        }
    }
    
    # Check if filepath is provided
    if not filepath:
        return "Error: No filepath provided."

    # Check if the provided file is in the mock database
    if filepath not in mock_sound_database:
        return f"Error: File '{filepath}' not found in the database."

    # Retrieve the sound properties from the mock database
    sound_properties = mock_sound_database[filepath]

    # Constructing the output string with sound properties
    output = (f"File: {filepath}\n"
              f"Duration: {sound_properties['duration']}\n"
              f"Sample Rate: {sound_properties['sample_rate']}\n"
              f"Channels: {sound_properties['channels']}\n"
              f"Genre: {sound_properties['genre']}")

    return output

if __name__ == "__main__":
    mcp.run(transport='stdio')
