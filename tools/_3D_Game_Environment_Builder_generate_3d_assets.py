from mcp.server.fastmcp import FastMCP
mcp = FastMCP('_3D_Game_Environment_Builder_generate_3d_assets')

@mcp.tool()
def _3D_Game_Environment_Builder_generate_3d_assets(player_bio: str, num_assets: str) -> str:
    '''```python
    """
    Generates 3D assets for video game scene composition based on a player's bio.

    This function creates a collection of 3D assets tailored to the player's 
    specified bio, which can be used for enhancing video game environments. 
    The assets are returned as a JSON string containing prompts and GLB file data.

    Args:
        player_bio (str): A non-empty string representing the player's bio, 
            which influences the type of 3D assets generated. Should be in the form of xxx style.
        num_assets (str): A string representing a positive integer that specifies 
            the number of 3D assets to generate.

    Returns:
        str: A JSON string containing the player's bio, the number of requested 
        assets, and a list of generated assets with their prompts and GLB file data.

    Raises:
        ValueError: If `player_bio` is not a non-empty string.
        ValueError: If `num_assets` is not a string representing a positive integer.
    """
```'''
    mock_asset_db = {'battle_royal': [{'prompt': 'Generate a ruined cityscape with destructible buildings for intense battle scenes', 'glb_data': '<GLB_FILE_DATA_RUINED_CITY_BASE64>'}, {'prompt': 'Create a dense jungle arena with hidden bunkers and sniper towers', 'glb_data': '<GLB_FILE_DATA_JUNGLE_ARENA_BASE64>'}, {'prompt': 'Design a futuristic battle arena with forcefields and holographic billboards', 'glb_data': '<GLB_FILE_DATA_FUTURISTIC_ARENA_BASE64>'}, {'prompt': 'Produce an abandoned industrial complex with multiple entry points and cover spots', 'glb_data': '<GLB_FILE_DATA_INDUSTRIAL_COMPLEX_BASE64>'}], 'fantasy_warrior': [{'prompt': 'Generate a medieval castle courtyard with armory and training grounds', 'glb_data': '<GLB_FILE_DATA_CASTLE_COURTYARD_BASE64>'}, {'prompt': 'Create an enchanted forest battleground with mystical lighting', 'glb_data': '<GLB_FILE_DATA_ENCHANTED_FOREST_BASE64>'}], 'space_marine': [{'prompt': 'Generate a space station docking bay with battle damage', 'glb_data': '<GLB_FILE_DATA_SPACE_STATION_BASE64>'}, {'prompt': 'Create an alien planet surface with volcanic terrain and hostile structures', 'glb_data': '<GLB_FILE_DATA_ALIEN_PLANET_BASE64>'}]}
    import json
    if not isinstance(player_bio, str) or not player_bio.strip():
        raise ValueError('player_bio must be a non-empty string.')
    if not isinstance(num_assets, str) or not num_assets.isdigit():
        raise ValueError('num_assets must be a string representing a positive integer.')
    num_assets_int = int(num_assets)
    if num_assets_int <= 0:
        raise ValueError('num_assets must be greater than 0.')
    bio_key = player_bio.strip().lower().replace(' ', '_')
    if bio_key not in mock_asset_db:
        mock_assets = [{'prompt': f'Generate a generic open field battleground for {player_bio}', 'glb_data': '<GLB_FILE_DATA_GENERIC_FIELD_BASE64>'}, {'prompt': f'Create a small urban combat zone adapted to {player_bio} style', 'glb_data': '<GLB_FILE_DATA_GENERIC_URBAN_BASE64>'}]
    else:
        mock_assets = mock_asset_db[bio_key]
    generated_assets = []
    while len(generated_assets) < num_assets_int:
        generated_assets.extend(mock_assets)
    generated_assets = generated_assets[:num_assets_int]
    response = {'player_bio': player_bio, 'requested_assets': num_assets_int, 'generated_assets': generated_assets}
    return json.dumps(response)
if __name__ == '__main__':
    mcp.run(transport='stdio')