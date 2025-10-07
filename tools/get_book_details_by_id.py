from mcp.server.fastmcp import FastMCP
from typing import List
mcp = FastMCP('get_book_details_by_id')

@mcp.tool()
def get_book_details_by_id(id: List[int]) -> str:
    '''```python
"""
Get book details by ID.

This function retrieves details of books based on their unique identifiers (IDs). 
It accepts a list of integer IDs and returns a formatted string containing the 
details of each book, including title, authors, publisher, year, edition, and ID. 
If an ID does not correspond to any book, a message indicating no details found 
is included for that ID.

Args:
    id (List[int]): A list of integers representing the unique identifiers of the books.

Returns:
    str: A formatted string with the details of the books corresponding to the provided IDs. 
         If an ID is not found, the string will include a message indicating no details found 
         for that particular ID.
"""
```'''
    mock_book_db = {1: {'title': 'The C Programming Language', 'authors': ['Brian W. Kernighan', 'Dennis M. Ritchie'], 'publisher': 'Prentice Hall', 'year': 1988, 'edition': '2nd', 'id': 1}, 2: {'title': 'Introduction to Algorithms', 'authors': ['Thomas H. Cormen', 'Charles E. Leiserson', 'Ronald L. Rivest', 'Clifford Stein'], 'publisher': 'MIT Press', 'year': 2009, 'edition': '3rd', 'id': 2}, 3: {'title': 'Design Patterns: Elements of Reusable Object-Oriented Software', 'authors': ['Erich Gamma', 'Richard Helm', 'Ralph Johnson', 'John Vlissides'], 'publisher': 'Addison-Wesley', 'year': 1994, 'edition': '1st', 'id': 3}, 4: {'title': 'Fluent Python', 'authors': ['Luciano Ramalho'], 'publisher': "O'Reilly Media", 'year': 2015, 'edition': '1st', 'id': 4}, 5: {'title': 'Head First Design Patterns', 'authors': ['Eric Freeman', 'Bert Bates', 'Kathy Sierra', 'Elisabeth Robson'], 'publisher': "O'Reilly Media", 'year': 2004, 'edition': '1st', 'id': 5}}
    if not isinstance(id, list) or not all((isinstance(i, int) for i in id)):
        return "Error: 'id' parameter must be a list of integers."
    if not id:
        return 'Error: No ID numbers provided.'
    results = []
    for code in id:
        if code in mock_book_db:
            book = mock_book_db[code]
            results.append(f"Title: {book['title']}\nAuthors: {', '.join(book['authors'])}\nPublisher: {book['publisher']}\nYear: {book['year']}\nEdition: {book['edition']}\nID: {book['id']}\n")
        else:
            results.append(f'ID: {code} - No details found in database.')
    return '\n'.join(results)
if __name__ == '__main__':
    mcp.run(transport='stdio')