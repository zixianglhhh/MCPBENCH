from mcp.server.fastmcp import FastMCP
mcp = FastMCP('vector_search')

@mcp.tool()
def vector_search(query: str, limit: int) -> str:
    '''```python
    """
    Perform semantic search across stored documents.

    This function executes a semantic search based on a given query string,
    retrieving and ranking stored documents according to their relevance.
    The relevance is determined using cosine similarity between the query
    embedding and document embeddings. The top results are returned up to
    the specified limit.

    Args:
        query (str): A non-empty string representing the search query.
        limit (int): A positive integer specifying the maximum number of
            top results to return.

    Returns:
        str: A formatted string containing the top matching documents'
        metadata, including model details, learning rate, l1 ratio,
        convergence speed, final error, and notes, along with their
        similarity scores. If no similar documents are found, returns
        'No similar experiments found.'
    """
```'''
    mock_vector_db = [{'id': 'exp001', 'embedding': [0.12, 0.56, 0.33, 0.89], 'metadata': {'model': 'SGDRegressor', 'regularization': 'ElasticNet', 'learning_rate': 0.01, 'l1_ratio': 0.2, 'convergence_speed': 'fast', 'final_error': 0.045, 'notes': 'Performed well on small dataset of US city housing prices.'}}, {'id': 'exp002', 'embedding': [0.14, 0.54, 0.31, 0.87], 'metadata': {'model': 'SGDRegressor', 'regularization': 'ElasticNet', 'learning_rate': 0.005, 'l1_ratio': 0.5, 'convergence_speed': 'medium', 'final_error': 0.052, 'notes': 'Balanced l1/l2 penalty improved stability but slower convergence.'}}, {'id': 'exp003', 'embedding': [0.85, 0.12, 0.65, 0.24], 'metadata': {'model': 'SGDRegressor', 'regularization': 'ElasticNet', 'learning_rate': 0.02, 'l1_ratio': 0.8, 'convergence_speed': 'very fast', 'final_error': 0.06, 'notes': 'High l1_ratio led to sparse weights, but slightly higher error.'}}, {'id': 'exp004', 'embedding': [0.11, 0.53, 0.34, 0.88], 'metadata': {'model': 'SGDRegressor', 'regularization': 'ElasticNet', 'learning_rate': 0.01, 'l1_ratio': 0.3, 'convergence_speed': 'fast', 'final_error': 0.046, 'notes': 'Similar to exp001 with marginally different l1_ratio.'}}]
    if not isinstance(query, str) or not query.strip():
        raise ValueError("Parameter 'query' must be a non-empty string.")
    if not isinstance(limit, int) or limit <= 0:
        raise ValueError("Parameter 'limit' must be a positive integer.")
    import random
    random.seed(abs(hash(query)) % 10 ** 6)
    query_embedding = [random.random() for _ in range(4)]

    def cosine_similarity(vec1, vec2):
        import math
        dot_prod = sum((a * b for (a, b) in zip(vec1, vec2)))
        norm1 = math.sqrt(sum((a * a for a in vec1)))
        norm2 = math.sqrt(sum((b * b for b in vec2)))
        if norm1 == 0 or norm2 == 0:
            return 0
        return dot_prod / (norm1 * norm2)
    scored_results = []
    for record in mock_vector_db:
        score = cosine_similarity(query_embedding, record['embedding'])
        scored_results.append((score, record))
    scored_results.sort(key=lambda x: x[0], reverse=True)
    top_results = scored_results[:limit]
    output_lines = []
    for (score, rec) in top_results:
        meta = rec['metadata']
        output_lines.append(f"ID: {rec['id']}, Model: {meta['model']}, LR: {meta['learning_rate']}, l1_ratio: {meta['l1_ratio']}, Convergence: {meta['convergence_speed']}, Final Error: {meta['final_error']}, Notes: {meta['notes']} (Similarity: {score:.3f})")
    return '\n'.join(output_lines) if output_lines else 'No similar experiments found.'
if __name__ == '__main__':
    mcp.run(transport='stdio')