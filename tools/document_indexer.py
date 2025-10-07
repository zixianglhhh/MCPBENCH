from mcp.server.fastmcp import FastMCP
mcp = FastMCP('document_indexer')

@mcp.tool()
def document_indexer(document: str, metadata: str, metrics: str, curves: str) -> str:
    '''```python
    """
    Indexes a document with its associated metadata, metrics, and curves.

    This function takes a document and its related information, validates the inputs,
    and stores them in an internal data structure. It also parses specific hyperparameters
    from the metadata if present.

    Args:
        document (str): The document content to be indexed. Must be a non-empty string.
        metadata (str): Metadata associated with the document. Must be a non-empty string.
        metrics (str): Performance metrics related to the document. Must be a non-empty string.
        curves (str): Curve data associated with the document. Must be a non-empty string.

    Returns:
        str: A success message indicating the document has been indexed, including the unique ID.
    """
```'''
    if not hasattr(document_indexer, '_mock_db'):
        document_indexer._mock_db = {'entries': []}
    if not isinstance(document, str) or not document.strip():
        raise ValueError("Invalid 'document' parameter: must be a non-empty string.")
    if not isinstance(metadata, str) or not metadata.strip():
        raise ValueError("Invalid 'metadata' parameter: must be a non-empty string.")
    if not isinstance(metrics, str) or not metrics.strip():
        raise ValueError("Invalid 'metrics' parameter: must be a non-empty string.")
    if not isinstance(curves, str) or not curves.strip():
        raise ValueError("Invalid 'curves' parameter: must be a non-empty string.")
    entry_id = len(document_indexer._mock_db['entries']) + 1
    new_entry = {'id': entry_id, 'document': document, 'metadata': metadata, 'metrics': metrics, 'curves': curves, 'indexed_at': '2024-06-15T12:00:00Z'}
    document_indexer._mock_db['entries'].append(new_entry)
    if 'learning_rate' in metadata and 'l1_ratio' in metadata:
        import re
        lr_match = re.search('learning_rate\\s*=\\s*([0-9\\.]+)', metadata)
        l1_match = re.search('l1_ratio\\s*=\\s*([0-9\\.]+)', metadata)
        if lr_match and l1_match:
            new_entry['parsed_hyperparams'] = {'learning_rate': float(lr_match.group(1)), 'l1_ratio': float(l1_match.group(1))}
    return f'Document indexed successfully with ID {entry_id}.'
if __name__ == '__main__':
    mcp.run(transport='stdio')