from mcp.server.fastmcp import FastMCP
from typing import List
mcp = FastMCP('get_players')

@mcp.tool()
def get_players(target_players: List[str]) -> str:
    '''```python
    """
    Retrieves detailed information about specified players from a sports team.

    This function accepts a list of player names and returns a formatted string
    containing comprehensive details about each player, including their team
    affiliations, positions, contact information, career achievements, and fun
    facts.

    Args:
        target_players (List[str]): A list of player names for which information
            is to be retrieved. Each name should be a string.

    Returns:
        str: A formatted string with detailed information about the requested
        players. If no matching players are found, an error message is returned.
    """
```'''
    mock_player_db = {'LeBron James': {'team': 'Los Angeles Lakers', 'position': 'Forward', 'contact': 'lebron.james@nba.com', 'career_achievements': ['4× NBA champion', '4× NBA Most Valuable Player', 'NBA All-Star 19 times'], 'fun_fact': 'LeBron James is the youngest player to score 30,000 career points in NBA history.'}, 'Stephen Curry': {'team': 'Golden State Warriors', 'position': 'Guard', 'contact': 'stephen.curry@nba.com', 'career_achievements': ['4× NBA champion', '2× NBA Most Valuable Player', 'NBA all-time leader in three-pointers made'], 'fun_fact': 'Stephen Curry is credited with revolutionizing the game with his exceptional three-point shooting.'}, 'Anthony Davis': {'team': 'Los Angeles Lakers', 'position': 'Forward-Center', 'contact': 'anthony.davis@nba.com', 'career_achievements': ['NBA champion (2020)', '8× NBA All-Star', '4× NBA All-Defensive First Team', 'NBA All-Star Game MVP (2017)'], 'fun_fact': "Anthony Davis is known for his exceptional defensive skills and was nicknamed 'The Brow' due to his distinctive unibrow."}, 'Donte DiVincenzo': {'team': 'Golden State Warriors', 'position': 'Guard', 'contact': 'donte.divincenzo@nba.com', 'career_achievements': ['NBA champion (2021)', 'NCAA champion (2018)', 'NCAA Final Four Most Outstanding Player (2018)'], 'fun_fact': "Donte DiVincenzo was a key player in Villanova's 2018 NCAA championship run and is known for his clutch performances."}}
    if not isinstance(target_players, list) or not all((isinstance(p, str) for p in target_players)):
        return "Error: 'target_players' must be a list of player names (strings)."
    available_players = {name: mock_player_db[name] for name in target_players if name in mock_player_db}
    if not available_players:
        return 'Error: No matching players found in the database for the given target_players list.'
    result_lines = []
    for (name, info) in available_players.items():
        result_lines.append(f"Player: {name}\nTeam: {info['team']}\nPosition: {info['position']}\nContact: {info['contact']}\nCareer Achievements: {', '.join(info['career_achievements'])}\nFun Fact: {info['fun_fact']}\n")
    return '\n'.join(result_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')