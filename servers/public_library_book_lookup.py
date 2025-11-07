from mcp.server.fastmcp import FastMCP
from typing import List
mcp = FastMCP('public_library_book_lookup')

@mcp.tool()
def public_library_book_lookup(title: str, branches: List[str]) -> str:
    '''"""
Check which local library branches have a specific title available for checkout.

The lookup supports partial, case-insensitive matches on book titles. When multiple
entries match the query, all exact branch availability results are returned. The
`branches` parameter should contain at least one branch code to narrow the search.

Args:
    title (str): Full or partial book title to search for.
    branches (List[str]): Preferred branch codes (e.g., ["CEN", "NBE"]).

Returns:
    str: Formatted availability summary or an error message when no copies are found.
"""'''
    catalog = [
        {
            'title': 'Atomic Habits',
            'author': 'James Clear',
            'availability': {'CEN': 4, 'NBE': 1, 'WES': 0}
        },
        {
            'title': 'Project Hail Mary',
            'author': 'Andy Weir',
            'availability': {'CEN': 0, 'NBE': 2, 'EST': 1}
        },
        {
            'title': 'Deep Work',
            'author': 'Cal Newport',
            'availability': {'CEN': 3, 'EST': 1, 'SOU': 2}
        },
        {
            'title': 'The Midnight Library',
            'author': 'Matt Haig',
            'availability': {'NBE': 0, 'WES': 1, 'SOU': 1}
        },
        {
            'title': 'Kitchen Confidential',
            'author': 'Anthony Bourdain',
            'availability': {'CEN': 1, 'EST': 0, 'SOU': 0}
        },
    ]
    if not title:
        return "Error: 'title' is required."
    if not branches:
        return "Error: At least one branch code must be provided."
    normalized_branches = [branch.strip().upper() for branch in branches if branch]
    if not normalized_branches:
        return "Error: Branch list cannot be empty."
    matches = [book for book in catalog if title.lower() in book['title'].lower()]
    if not matches:
        return f"No books found matching '{title}'."
    lines = []
    for book in matches:
        branch_lines = []
        for branch_code in normalized_branches:
            copies = book['availability'].get(branch_code)
            if copies is None:
                branch_lines.append(f"- {branch_code}: not cataloged")
            elif copies == 0:
                branch_lines.append(f"- {branch_code}: all copies checked out")
            else:
                branch_lines.append(f"- {branch_code}: {copies} copy/copies available")
        lines.append(
            f"Title: {book['title']}\n"
            f"Author: {book['author']}\n"
            + '\n'.join(branch_lines)
        )
    return '\n\n'.join(lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')
