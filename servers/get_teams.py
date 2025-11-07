from mcp.server.fastmcp import FastMCP
mcp = FastMCP('get_teams')

@mcp.tool()
def get_teams(nameFilter: str) -> str:
    '''```python
    """
    Retrieves a list of teams and their members for specified sports leagues.

    This function returns detailed information about teams and their members
    for various sports leagues, including NBA, NFL, MLB, NHL, CBB, CFC, and NCAA.
    The information includes team names and member details such as name and position.

    Args:
        nameFilter (str): The name of the league to filter teams by. Must be one of
            'NBA', 'NFL', 'MLB', 'NHL', 'CBB', 'CFC', or 'NCAA'.

    Returns:
        str: A formatted string containing the list of teams and their members for
        the specified league. If the league name is invalid or the input type is incorrect,
        an error message is returned.
    """
```'''
    mock_teams_db = {'NBA': [{'team_name': 'Los Angeles Lakers', 'members': [{'name': 'LeBron James', 'position': 'Forward'}, {'name': 'Anthony Davis', 'position': 'Forward-Center'}, {'name': "D'Angelo Russell", 'position': 'Guard'}, {'name': 'Russell Westbrook', 'position': 'Guard'}, {'name': 'Thomas Bryant', 'position': 'Center'}, {'name': 'Troy Brown Jr.', 'position': 'Forward'}, {'name': 'Austin Reaves', 'position': 'Guard'}, {'name': 'Lonnie Walker IV', 'position': 'Guard'}, {'name': 'Patrick Beverley', 'position': 'Guard'}, {'name': 'Wenyen Gabriel', 'position': 'Forward'}]}, {'team_name': 'Golden State Warriors', 'members': [{'name': 'Stephen Curry', 'position': 'Guard'}, {'name': 'Klay Thompson', 'position': 'Guard'}, {'name': 'Draymond Green', 'position': 'Forward'}, {'name': 'Jordan Poole', 'position': 'Guard'}, {'name': 'Kevon Looney', 'position': 'Center'}, {'name': 'Andrew Wiggins', 'position': 'Forward'}, {'name': 'Moses Moody', 'position': 'Guard'}, {'name': 'Jonathan Kuminga', 'position': 'Forward'}, {'name': 'JaMychal Green', 'position': 'Forward'}, {'name': 'Donte DiVincenzo', 'position': 'Guard'}]}], 'NFL': [{'team_name': 'New England Patriots', 'members': [{'name': 'Mac Jones', 'position': 'Quarterback'}, {'name': 'Matthew Judon', 'position': 'Linebacker'}, {'name': 'Jakobi Meyers', 'position': 'Wide Receiver'}]}, {'team_name': 'Dallas Cowboys', 'members': [{'name': 'Dak Prescott', 'position': 'Quarterback'}, {'name': 'Micah Parsons', 'position': 'Linebacker'}, {'name': 'CeeDee Lamb', 'position': 'Wide Receiver'}]}], 'MLB': [{'team_name': 'New York Yankees', 'members': [{'name': 'Aaron Judge', 'position': 'Outfielder'}, {'name': 'Gerrit Cole', 'position': 'Pitcher'}, {'name': 'Giancarlo Stanton', 'position': 'Outfielder'}]}], 'NHL': [{'team_name': 'Chicago Blackhawks', 'members': [{'name': 'Jonathan Toews', 'position': 'Center'}, {'name': 'Patrick Kane', 'position': 'Right Wing'}, {'name': 'Seth Jones', 'position': 'Defenseman'}]}], 'CBB': [{'team_name': 'Duke Blue Devils', 'members': [{'name': 'Jeremy Roach', 'position': 'Guard'}, {'name': 'Kyle Filipowski', 'position': 'Forward'}, {'name': 'Tyrese Proctor', 'position': 'Guard'}]}], 'CFC': [{'team_name': 'Clemson Tigers Football', 'members': [{'name': 'Cade Klubnik', 'position': 'Quarterback'}, {'name': 'Will Shipley', 'position': 'Running Back'}, {'name': 'Barrett Carter', 'position': 'Linebacker'}]}], 'NCAA': [{'team_name': 'Alabama Crimson Tide', 'members': [{'name': 'Bryce Young', 'position': 'Quarterback'}, {'name': 'Will Anderson Jr.', 'position': 'Linebacker'}, {'name': 'Brian Robinson Jr.', 'position': 'Running Back'}]}]}
    if not isinstance(nameFilter, str):
        return 'Error: nameFilter must be a string.'
    nameFilter_upper = nameFilter.strip().upper()
    if nameFilter_upper not in mock_teams_db:
        valid_keys = ', '.join(mock_teams_db.keys())
        return f"Error: Invalid league filter '{nameFilter}'. Valid options are: {valid_keys}."
    teams_list = mock_teams_db[nameFilter_upper]
    output_lines = [f'Teams in {nameFilter_upper}:']
    for team in teams_list:
        output_lines.append(f"- {team['team_name']}")
        for member in team['members']:
            output_lines.append(f"   • {member['name']} ({member['position']})")
    return '\n'.join(output_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')