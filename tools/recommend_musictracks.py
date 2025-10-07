from mcp.server.fastmcp import FastMCP
from typing import List
mcp = FastMCP('recommend_musictracks')

@mcp.tool()
def recommend_musictracks(music_name: List[str], result_num: int) -> str:
    '''```python
"""
Generates music track recommendations based on provided seed identifiers, returning up to a specified number
of tracks per seed with complete metadata.

This function searches for tracks using seed identifiers and retrieves track metadata for each seed. 
Music names should be provided exactly as specified with proper capitalization. The number
of tracks returned per seed is limited by the `result_num` parameter.

Args:
    music_name (List[str]): A list of seed identifiers to look up, such as album keys. 
        Music names should be exactly as specified with capital letters, for example "Love Youselves".
    result_num (int): The maximum number of tracks to return for each seed identifier.

Returns:
    str: A string representation of a list containing dictionaries of track metadata. Each dictionary includes
    details such as title, artist, album, genre, release date, and a preview URL.

Raises:
    ValueError: If `music_name` is not a list of strings or if `result_num` is not a positive integer.
"""
```'''
    mock_tracks_db = {'billboard_2023_album1_track1': {'title': 'Electric Horizon', 'artist': 'Neon Pulse', 'album': 'Skyline Dreams', 'genre': 'Synthpop', 'release_date': '2023-05-14', 'preview_url': 'https://mockstreaming.com/preview/electric_horizon'}, 'billboard_2023_album1_track3': {'title': 'Golden Rivers', 'artist': 'Aurora Fields', 'album': "Nature's Echo", 'genre': 'Folk Pop', 'release_date': '2023-07-22', 'preview_url': 'https://mockstreaming.com/preview/golden_rivers'}, 'deezer_similar_style_1': {'title': 'Skybound Love', 'artist': 'Crystal Waves', 'album': 'Blue Horizons', 'genre': 'Synthpop', 'release_date': '2022-11-02', 'preview_url': 'https://mockstreaming.com/preview/skybound_love'}, 'deezer_similar_style_2': {'title': 'Meadow Lullaby', 'artist': 'Willow Whisper', 'album': 'Evening Glow', 'genre': 'Folk Pop', 'release_date': '2022-09-15', 'preview_url': 'https://mockstreaming.com/preview/meadow_lullaby'}, 'jazz_inspired_1': {'title': 'Midnight Groove', 'artist': 'The Blue Tones', 'album': 'City Lights', 'genre': 'Jazz', 'release_date': '2021-04-09', 'preview_url': 'https://mockstreaming.com/preview/midnight_groove'}, 'jazz_inspired_2': {'title': 'Sax & The City', 'artist': 'Urban Quartet', 'album': 'Metropolitan Nights', 'genre': 'Jazz Fusion', 'release_date': '2020-08-21', 'preview_url': 'https://mockstreaming.com/preview/sax_and_the_city'}, 'upbeat_track_1': {'title': 'Dance Until Dawn', 'artist': 'Rhythm Rush', 'album': 'Night Fever', 'genre': 'Dance Pop', 'release_date': '2023-03-18', 'preview_url': 'https://mockstreaming.com/preview/dance_until_dawn'}, 'guts_vampire': {'title': 'vampire', 'artist': 'Olivia Rodrigo', 'album': 'GUTS', 'genre': 'Pop Rock', 'release_date': '2023-06-30', 'preview_url': 'https://mockstreaming.com/preview/olivia_rodrigo_vampire'}, 'guts_bad_idea_right': {'title': 'bad idea right?', 'artist': 'Olivia Rodrigo', 'album': 'GUTS', 'genre': 'Pop Punk', 'release_date': '2023-08-11', 'preview_url': 'https://mockstreaming.com/preview/olivia_rodrigo_bad_idea_right'}, 'guts_get_him_back': {'title': 'get him back!', 'artist': 'Olivia Rodrigo', 'album': 'GUTS', 'genre': 'Pop Rock', 'release_date': '2023-09-08', 'preview_url': 'https://mockstreaming.com/preview/olivia_rodrigo_get_him_back'}, 'guts_ballad_of_a_homeschooled_girl': {'title': 'ballad of a homeschooled girl', 'artist': 'Olivia Rodrigo', 'album': 'GUTS', 'genre': 'Pop Punk', 'release_date': '2023-09-08', 'preview_url': 'https://mockstreaming.com/preview/olivia_rodrigo_ballad_of_a_homeschooled_girl'}, 'guts_logical': {'title': 'logical', 'artist': 'Olivia Rodrigo', 'album': 'GUTS', 'genre': 'Pop', 'release_date': '2023-09-08', 'preview_url': 'https://mockstreaming.com/preview/olivia_rodrigo_logical'}, 'guts_lacy': {'title': 'lacy', 'artist': 'Olivia Rodrigo', 'album': 'GUTS', 'genre': 'Indie Pop', 'release_date': '2023-09-08', 'preview_url': 'https://mockstreaming.com/preview/olivia_rodrigo_lacy'}}
    mock_music_db = {'guts': ['guts_vampire', 'guts_bad_idea_right', 'guts_get_him_back', 'guts_ballad_of_a_homeschooled_girl', 'guts_logical', 'guts_lacy'], 'jazz_inspired': ['jazz_inspired_1', 'jazz_inspired_2'], 'deezer_similar': ['deezer_similar_style_1', 'deezer_similar_style_2'], 'billboard_2023_album1': ['billboard_2023_album1_track1', 'billboard_2023_album1_track3']}
    if not isinstance(music_name, list) or not all((isinstance(tid, str) for tid in music_name)):
        return "Error: 'music_name' must be a list of strings representing track IDs."
    if not isinstance(result_num, int) or result_num <= 0:
        return "Error: 'result_num' must be a positive integer."
    recommendations = []
    seen_track_ids = set()
    for seed in music_name:
        track_ids = mock_music_db.get(seed.lower()) if isinstance(seed, str) else None
        if not track_ids:
            continue
        for track_id in track_ids[:result_num]:
            if track_id in seen_track_ids:
                continue
            seen_track_ids.add(track_id)
            track_meta = mock_tracks_db.get(track_id)
            if track_meta:
                recommendations.append(track_meta)
    if not recommendations:
        return 'No recommendations found for the given track IDs and filter criteria.'
    return str(recommendations)
if __name__ == '__main__':
    mcp.run(transport='stdio')