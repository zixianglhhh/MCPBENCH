from mcp.server.fastmcp import FastMCP
mcp = FastMCP('dmagent_ask_narrative')

@mcp.tool()
def dmagent_ask_narrative(question: str, theme_hint: str, tone: str, focus_element: str) -> str:
    '''```python
    """
    Provides an interactive assistant for Dungeon Masters in Dungeons & Dragons 5e, 
    focusing on narrative development. This tool poses targeted questions to help 
    shape the adventure's theme, setting, and mood, aiding in defining story elements 
    such as environment, villain style, puzzle flavor, traps, and rewards. The responses 
    assist the DM in crafting immersive read-aloud text, narrative hooks, and maintaining 
    thematic consistency. This function emphasizes worldbuilding and storytelling, 
    complementing other tools that handle rules or dice mechanics.

    Args:
        question (str): The initial narrative question posed by the DM.
        theme_hint (str): An optional hint to guide the thematic direction of the narrative.
        tone (str): An optional descriptor to set the tone of the adventure, such as 
            'serious' or 'lighthearted'.
        focus_element (str): An optional focus area for the narrative, such as 'boss design' 
            or 'trap'.

    Returns:
        str: A follow-up narrative question tailored to the provided inputs, aiding in 
        the development of the adventure's theme and story elements.
    """
```'''
    mock_db = {'default': ['What overall theme should the one-shot have—dark horror, epic fantasy, or whimsical adventure?', 'What sort of environment will the party begin in—forest, dungeon, city, or something else?', "Describe the villain's personality—cunning mastermind, brute force, tragic figure?"], 'undead horror': {'serious': {'boss design': ['Should the undead boss be a cunning necromancer or a mindless horde leader?', "What cursed artifact fuels the villain's dark magic?"], 'trap': ['Should the traps be bone-crushing mechanical devices or necrotic wards that drain life?', 'What eerie signs warn of the traps ahead?'], 'puzzle': ["What kind of riddle could be carved into the crypt walls to seal the villain's chamber?", 'Should the puzzle require interpreting ancient runes or aligning skeletal remains?'], 'reward': ['What holy relic could banish undead from the realm as a final reward?', 'Should the reward be a weapon, armor, or magical trinket imbued with radiant energy?']}}, 'jungle exploration': {'lighthearted': {'boss design': ['Should the jungle boss be a mischievous trickster spirit or a territorial beast?', "What unusual weakness does the boss have tied to the jungle's flora?"]}}, 'arcane mystery': {'gritty': {'puzzle': ['Should the puzzle involve rearranging arcane sigils or deciphering a forbidden incantation?', 'What is at stake if the puzzle is solved incorrectly?']}}}
    if not isinstance(question, str) or not question.strip():
        raise ValueError("Parameter 'question' must be a non-empty string.")
    if theme_hint is not None and (not isinstance(theme_hint, str)):
        raise ValueError("Parameter 'theme_hint' must be a string if provided.")
    if tone is not None and (not isinstance(tone, str)):
        raise ValueError("Parameter 'tone' must be a string if provided.")
    if focus_element is not None and (not isinstance(focus_element, str)):
        raise ValueError("Parameter 'focus_element' must be a string if provided.")
    theme_key = theme_hint.strip().lower() if theme_hint else None
    tone_key = tone.strip().lower() if tone else None
    focus_key = focus_element.strip().lower() if focus_element else None
    matched_prompts = None
    if theme_key and theme_key in mock_db:
        theme_data = mock_db[theme_key]
        if isinstance(theme_data, dict) and tone_key and (tone_key in theme_data):
            tone_data = theme_data[tone_key]
            if focus_key and focus_key in tone_data:
                matched_prompts = tone_data[focus_key]
        elif isinstance(theme_data, list):
            matched_prompts = theme_data
    if not matched_prompts:
        matched_prompts = mock_db['default']
    import random
    follow_up_question = random.choice(matched_prompts)
    return f'Narrative question based on your input: {follow_up_question}\n(Original question: {question})'
if __name__ == '__main__':
    mcp.run(transport='stdio')