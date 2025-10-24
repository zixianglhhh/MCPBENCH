from mcp.server.fastmcp import FastMCP
mcp = FastMCP('diceRoll')

@mcp.tool()
def diceRoll(sides: int, count: int, modifier: int, roll_type: str) -> str:
    '''```python
    """
    Roll D&D dice with customizable options.

    This function simulates rolling dice commonly used in Dungeons & Dragons
    games, allowing for various roll types and modifiers. It supports different
    contexts such as attack rolls, saving throws, skill checks, and more.

    Args:
        sides (int): The number of sides on each die. Must be greater than 1.
        count (int): The number of dice to roll. Must be a positive integer.
        modifier (int): A numerical modifier to be added to the total roll.
        roll_type (str): The type of roll being performed, such as 'attack',
            'saving throw', or 'skill check'. Must be a non-empty string.

    Returns:
        str: A formatted string describing the roll context, individual dice
        results, the modifier applied, and the total result.
    """
```'''
    import random
    mock_roll_contexts = {'attack': {'default_sides': 20, 'description': 'You swing your weapon in an attack roll.'}, 'saving throw': {'default_sides': 20, 'description': 'You attempt to resist a harmful effect with a saving throw.'}, 'skill check': {'default_sides': 20, 'description': 'You test your skills in a tense moment.'}, 'trap disarm': {'default_sides': 20, 'description': 'You attempt to disarm a hidden trap.'}, 'puzzle solve': {'default_sides': 20, 'description': 'You try to solve the puzzle under time pressure.'}, 'boss battle': {'default_sides': 20, 'description': 'You face the boss in a climactic roll.'}}
    if not isinstance(count, int) or count <= 0:
        return "Error: 'count' must be a positive integer."
    if not isinstance(modifier, int):
        return "Error: 'modifier' must be an integer."
    if not isinstance(roll_type, str) or roll_type.strip() == '':
        return "Error: 'roll_type' must be a non-empty string."
    if sides is not None and (not isinstance(sides, int) or sides <= 1):
        return "Error: 'sides' must be an integer greater than 1."
    context = mock_roll_contexts.get(roll_type.lower())
    dice_sides = sides
    if dice_sides is None:
        dice_sides = context['default_sides'] if context else 20
    rolls = [random.randint(1, dice_sides) for _ in range(count)]
    total = sum(rolls) + modifier
    description = context['description'] if context else f'You roll {count}d{dice_sides}.'
    result_str = f'{description}\nRolls: {rolls} (d{dice_sides})\nModifier: {modifier:+}\nTotal: {total}'
    return result_str
if __name__ == '__main__':
    mcp.run(transport='stdio')