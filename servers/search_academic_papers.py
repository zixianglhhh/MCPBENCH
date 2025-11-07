from mcp.server.fastmcp import FastMCP
mcp = FastMCP('search_academic_papers')

@mcp.tool()
def search_academic_papers(query: str, subject: str, max_results: int) -> str:
    '''```python
    """
    Searches for academic papers with subject filtering.

    This function performs a search on academic papers based on a specified query
    and subject, returning a list of papers that match the criteria up to a
    specified maximum number of results.

    Args:
        query (str): The search term used to filter papers by title or abstract.
                     Must be a non-empty string.
        subject (str): The subject area to filter papers by. Must be a non-empty string.
        max_results (int): The maximum number of results to return. Must be a positive integer.

    Returns:
        str: A formatted string listing the academic papers that match the search criteria.
             Each entry includes the paper's title, publication year, source, and abstract.
             If no papers are found, a message indicating no matches is returned.
    """
```'''
    mock_papers_db = [{'title': 'Seat Reservation Behaviors among University Students: A Social Norms Perspective', 'abstract': 'This paper investigates the cultural and behavioral aspects of seat reservation in university libraries.', 'subject': 'sociology', 'source': 'Journal of Higher Education Behavior Studies', 'year': 2021}, {'title': 'Analyzing Space Utilization in Academic Libraries: Case Study of Seat Reservation Practices', 'abstract': 'We analyze data on seat reservation patterns in academic libraries and propose management strategies.', 'subject': 'library science', 'source': 'Library Management Review', 'year': 2020}, {'title': 'Arxiv Preprint: Machine Learning Approaches for Classroom Occupancy Prediction', 'abstract': 'This paper presents machine learning models for predicting class attendance using arxiv datasets.', 'subject': 'computer science', 'source': 'arXiv', 'year': 2022}, {'title': 'Educational Technology in Secondary Schools: A Systematic Review', 'abstract': 'Systematic review of educational technology adoption in high schools.', 'subject': 'education', 'source': 'Educational Technology Today', 'year': 2019}, {'title': 'Arxiv Preprint: Advances in Natural Language Processing for Education', 'abstract': 'Overview of recent advancements in NLP with applications in educational contexts.', 'subject': 'computer science', 'source': 'arXiv', 'year': 2021}, {'title': 'Mixture-of-Experts: A Survey and Open Problems', 'abstract': 'A comprehensive survey of Mixture-of-Experts (MoE) architectures, routing strategies, training stability, and applications.', 'subject': 'computer science', 'source': 'arXiv', 'year': 2023}, {'title': 'Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity', 'abstract': 'Introduces Switch Transformers, a sparse MoE architecture enabling efficient scaling with expert routing.', 'subject': 'computer science', 'source': 'arXiv', 'year': 2021}, {'title': 'GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding', 'abstract': 'Presents GShard with MoE layers and automatic sharding for large-scale training.', 'subject': 'computer science', 'source': 'NeurIPS', 'year': 2021}, {'title': 'Sparse Mixture-of-Experts are Domain General Learners', 'abstract': 'Shows that sparse MoE Transformers generalize across domains with efficient routing.', 'subject': 'computer science', 'source': 'ICML', 'year': 2022}, {'title': 'Stabilizing MoE Training: Load Balancing and Expert Dropout', 'abstract': 'Analyzes instability in MoE training and proposes load balancing losses and expert dropout.', 'subject': 'computer science', 'source': 'arXiv', 'year': 2022}, {'title': 'DeepSeekMoE: Towards Efficient and Stable Mixture-of-Experts LLMs', 'abstract': 'Reports engineering techniques for efficient, stable MoE training in large language models.', 'subject': 'computer science', 'source': 'arXiv', 'year': 2024}]
    if not isinstance(query, str) or not query.strip():
        return "Error: 'query' must be a non-empty string."
    if not isinstance(subject, str) or not subject.strip():
        return "Error: 'subject' must be a non-empty string."
    if not isinstance(max_results, int) or max_results <= 0:
        return "Error: 'max_results' must be a positive integer."
    query_lower = query.lower()
    subject_lower = subject.lower()
    filtered_results = []
    for paper in mock_papers_db:
        if subject_lower in paper['subject'].lower() and (query_lower in paper['title'].lower() or query_lower in paper['abstract'].lower()):
            filtered_results.append(paper)
    filtered_results = filtered_results[:max_results]
    if not filtered_results:
        return f"No academic papers found matching query '{query}' for subject '{subject}'."
    output_lines = []
    for (idx, paper) in enumerate(filtered_results, start=1):
        output_lines.append(f"{idx}. {paper['title']} ({paper['year']}) - Source: {paper['source']}")
        output_lines.append(f"   Abstract: {paper['abstract']}")
    output_lines.append("Note: All the papers (PDF) will be saved under the folder /research/document/results/.")
    return '\n'.join(output_lines)
    
if __name__ == '__main__':
    mcp.run(transport='stdio')