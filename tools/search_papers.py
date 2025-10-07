from mcp.server.fastmcp import FastMCP
mcp = FastMCP('search_papers')

@mcp.tool()
def search_papers(query: str, sources: str, max_results: str, sort_by: str) -> str:
    '''```python
    """
    Searches scholarly sources for academic papers that match a given query.

    This function queries multiple scholarly sources to find papers that match
    the specified search query. It allows filtering by source, limiting the
    number of results, and sorting the results by specified criteria.

    Args:
        query (str): The search term used to find relevant papers. Must be a
            non-empty string.
        sources (str): A string specifying the source(s) to filter the search
            results. If empty, all sources are considered.
        max_results (str): A string representing the maximum number of results
            to return. Must be convertible to a positive integer.
        sort_by (str): The criterion by which to sort the results. Acceptable
            values are 'year', 'citations', or 'title'. Sorting is in descending
            order for 'year' and 'citations', and ascending order for 'title'.

    Returns:
        str: A formatted string containing the details of the matching papers,
        including title, authors, year, source, citations, and abstract. If no
        papers are found, returns a message indicating no matches. If input
        parameters are invalid, returns an error message.
    """
```'''
    mock_papers_db = [{'title': 'Global Climate Change Trends: A Decade of Earth Science Observations', 'authors': ['Dr. Jane Smith', 'Dr. Robert Lee'], 'year': 2022, 'source': 'Nature Climate Change', 'abstract': 'This paper reviews global climate change trends from 2012 to 2022, synthesizing data from multiple Earth observation systems.', 'citations': 523}, {'title': 'Earth System Models and Climate Projections for the Next Century', 'authors': ['Prof. Alan White', 'Dr. Maria Gonzalez'], 'year': 2021, 'source': 'Journal of Earth Sciences', 'abstract': 'We present an analysis of Earth system models in predicting climate change impacts over the next 100 years.', 'citations': 412}, {'title': 'Satellite-Derived Temperature Trends in the Last Decade', 'authors': ['Dr. Huan Liu', 'Dr. Michael Brown'], 'year': 2020, 'source': 'Geophysical Research Letters', 'abstract': 'Satellite data was used to identify and analyze global temperature changes from 2010 to 2020.', 'citations': 298}, {'title': 'Impacts of Climate Change on Coastal Ecosystems', 'authors': ['Dr. Emily Carter'], 'year': 2019, 'source': 'Marine Ecology Progress Series', 'abstract': 'An examination of the effects of global climate change on marine and coastal ecosystems, focusing on the last decade.', 'citations': 187}]
    if not query or not isinstance(query, str) or query.strip() == '':
        return "Error: 'query' parameter is required and must be a non-empty string."
    filtered_papers = mock_papers_db
    if sources and isinstance(sources, str) and sources.strip():
        filtered_papers = [p for p in filtered_papers if sources.lower() in p['source'].lower()]
    filtered_papers = [p for p in filtered_papers if query.lower() in p['title'].lower() or query.lower() in p['abstract'].lower()]
    if sort_by and isinstance(sort_by, str):
        if sort_by.lower() == 'year':
            filtered_papers.sort(key=lambda x: x['year'], reverse=True)
        elif sort_by.lower() == 'citations':
            filtered_papers.sort(key=lambda x: x['citations'], reverse=True)
        elif sort_by.lower() == 'title':
            filtered_papers.sort(key=lambda x: x['title'])
    if max_results:
        try:
            max_results_int = int(max_results)
            if max_results_int > 0:
                filtered_papers = filtered_papers[:max_results_int]
        except ValueError:
            return "Error: 'max_results' must be a valid integer."
    if not filtered_papers:
        return f"No papers found matching query '{query}'."
    output_lines = []
    for paper in filtered_papers:
        output_lines.append(f"Title: {paper['title']}\nAuthors: {', '.join(paper['authors'])}\nYear: {paper['year']}\nSource: {paper['source']}\nCitations: {paper['citations']}\nAbstract: {paper['abstract']}\n----------------------------------------")
    return '\n'.join(output_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')