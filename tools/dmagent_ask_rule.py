from mcp.server.fastmcp import FastMCP
mcp = FastMCP('dmagent_ask_rule')

@mcp.tool()
def dmagent_ask_rule(question: str, rule_category: str, complexity_level: str, edition: str) -> str:
    '''```python
"""
An interactive Dungeon Master assistant for Dungeons & Dragons rules. This function helps clarify mechanical or rules-related questions to ensure encounters, abilities, traps, puzzles, or combat are resolved correctly. It aims to ensure that generated adventures adhere to system mechanics, including stat blocks, challenge ratings, saving throw mechanics, and item properties. The focus is on mechanics and system compliance, complementing narrative aspects handled by other tools.

Args:
    question (str): The specific rules-related question to be addressed.
    rule_category (str): The category of rules to query, such as 'combat', 'traps', 'items', 'monsters', or 'spellcasting'.
    complexity_level (str): The complexity level of the rules, which can be 'basic', 'standard', or 'advanced'.
    edition (str): The edition of the game rules to use, such as '5e', '3.5e', or 'Pathfinder'.

Returns:
    str: A formatted string containing the edition, rule category, complexity level, and guidance for the given question.
"""
```'''
    mock_rules_db = {'combat': {'basic': 'In D&D 5e, combat is turn-based. Each creature gets movement, one action, and possibly a bonus action.', 'standard': 'For a CR 5 boss, typical AC ranges from 15-17, HP around 150, and attack bonus +6 to +8. CR 10 bosses often have legendary actions, while CR 15 bosses may have lair actions.', 'advanced': 'CR calculation considers HP, AC, damage per round, save DCs, resistances, and immunities according to DMG p. 274-281.'}, 'traps': {'basic': 'Traps usually require a Perception check to detect and a Dexterity saving throw to avoid damage.', 'standard': 'A medium-difficulty trap may have a DC 15 Perception check to detect and DC 15 Dexterity save to avoid 4d10 damage.', 'advanced': "Complex traps may involve multiple mechanisms, requiring multiple ability checks or saving throws over several rounds. Consult Xanathar's Guide for examples."}, 'items': {'basic': 'Magic items are ranked: common, uncommon, rare, very rare, legendary.', 'standard': 'An uncommon item might give +1 AC or +1 to attack rolls; a rare item could grant resistance to a damage type or 1/day spell use.', 'advanced': 'Determine rarity by comparing bonuses, charges, and game-breaking potential. See DMG p. 285 for guidelines.'}, 'monsters': {'basic': 'Monsters have stat blocks including HP, AC, attacks, and abilities.', 'standard': 'A CR 5 monster is a serious threat to a party of level 5 characters, while CR 10 is deadly for level 10 parties.', 'advanced': 'Adjust monster CR based on environment, lair actions, legendary actions, and party composition.'}, 'spellcasting': {'basic': 'Spellcasters have spell slots per level and known/prepared spells.', 'standard': 'Saving throws vs. spells use DC = 8 + proficiency bonus + spellcasting ability modifier.', 'advanced': 'Consider concentration rules, counterspells, spell components, and upcasting effects.'}}
    supported_editions = ['5e', '3.5e', 'Pathfinder']
    if edition and edition not in supported_editions:
        return f"Error: Unsupported edition '{edition}'. Supported editions: {', '.join(supported_editions)}."
    selected_edition = edition if edition else '5e'
    selected_category = (rule_category or 'combat').lower()
    selected_complexity = (complexity_level or 'standard').lower()
    if selected_category not in mock_rules_db:
        return f"Error: Unknown rule category '{selected_category}'. Available categories: {', '.join(mock_rules_db.keys())}."
    if selected_complexity not in mock_rules_db[selected_category]:
        return f"Error: Unknown complexity level '{selected_complexity}'. Available levels: {', '.join(mock_rules_db[selected_category].keys())}."
    base_guidance = mock_rules_db[selected_category][selected_complexity]
    if question:
        q_lower = question.lower()
        if 'cr' in q_lower:
            answer = 'For balance, a boss CR should match the average party level +2 for a challenging fight.'
        elif 'saving throw' in q_lower:
            answer = 'Dexterity saves are common for traps; Constitution or Wisdom saves may apply for magical effects.'
        elif 'magical reward' in q_lower or 'item' in q_lower:
            answer = "Theme-appropriate reward: For a desert adventure, a 'Ring of Sandstride' (uncommon) allows movement through sand without penalty."
        else:
            answer = "The rule depends on context; refer to the Dungeon Master's Guide for detailed guidance."
        return f'[Edition: {selected_edition.upper()} | Category: {selected_category} | Complexity: {selected_complexity}]\nBase Guidance: {base_guidance}\nQ: {question}\nA: {answer}'
    else:
        return f'[Edition: {selected_edition.upper()} | Category: {selected_category} | Complexity: {selected_complexity}]\nGuidance: {base_guidance}'
if __name__ == '__main__':
    mcp.run(transport='stdio')