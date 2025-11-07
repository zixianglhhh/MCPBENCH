from mcp.server.fastmcp import FastMCP
mcp = FastMCP('figma_export_code')

@mcp.tool()
def figma_export_code(fileKey: str, nodeId: str) -> str:
    '''```python
    """
    Converts Figma design files into production-ready code snippets.

    This function facilitates the design-to-development workflow by allowing 
    developers to fetch entire Figma files or specific nodes and export them 
    as code. It is particularly useful for building UI components, prototyping 
    applications, and accelerating product development.

    Args:
        fileKey (str): The unique identifier for the Figma file to be exported. 
                       Must be a non-empty string.
        nodeId (str): The unique identifier for a specific node within the Figma 
                      file. If provided, must be a non-empty string.

    Returns:
        str: A message indicating the success of the export operation, along with 
             the corresponding code snippet. If a nodeId is specified, the code 
             for that node and its parameters are returned. Otherwise, the full 
             file code and parameters for all nodes are returned.
    """
```'''
    mock_figma_db = {'UI123VOCABAPP': {'full_file_code': "<App>\n  <Header title='Vocab Memorizer'/>\n  <WordCard word='example' />\n  <CountdownTimer duration='60' />\n</App>", 'nodes': {'NODE_HEADER': {'code': "<Header title='Vocab Memorizer' style={{ backgroundColor: '#4CAF50', color: 'white' }}/>", 'params': {'title': 'Vocab Memorizer', 'backgroundColor': '#4CAF50', 'color': 'white'}}, 'NODE_CARD': {'code': "<WordCard word='example' definition='A representative form or pattern'/>", 'params': {'word': 'example', 'definition': 'A representative form or pattern', 'cardId': 'card_001'}}, 'NODE_TIMER': {'code': "<CountdownTimer start={Date.now()} duration={60000} onComplete={alert('Time up!')}/>", 'params': {'Ele': 'vocab_timer_user001', 'StartDate': '2025-07-15T09:00:00', 'EndDate': '20245-08-15T09:30:00'}}}}}
    if not isinstance(fileKey, str) or not fileKey.strip():
        raise ValueError('Invalid fileKey: must be a non-empty string.')
    if fileKey not in mock_figma_db:
        raise ValueError(f"Figma file with key '{fileKey}' not found in the mock database.")
    if nodeId:
        if not isinstance(nodeId, str) or not nodeId.strip():
            raise ValueError('Invalid nodeId: must be a non-empty string when provided.')
        if nodeId not in mock_figma_db[fileKey]['nodes']:
            raise ValueError(f"Node '{nodeId}' not found in file '{fileKey}'.")
        node_data = mock_figma_db[fileKey]['nodes'][nodeId]
        if isinstance(node_data, dict) and 'code' in node_data:
            result = f"Export successful: Code for node '{nodeId}'\n{node_data['code']}"
            if 'params' in node_data and node_data['params']:
                params = node_data['params']
                result += f'\n\nParameters for {nodeId}:\n'
                for (param_name, param_value) in params.items():
                    result += f'{param_name}: {param_value}\n'
            return result
        else:
            return f"Export successful: Code for node '{nodeId}'\n{node_data}"
    file_data = mock_figma_db[fileKey]
    result = f"Export successful: Full file code for '{fileKey}'\n{file_data['full_file_code']}"
    if 'nodes' in file_data:
        result += f'\n\nNode Parameters:\n'
        for (node_name, node_data) in file_data['nodes'].items():
            if isinstance(node_data, dict) and 'params' in node_data and node_data['params']:
                result += f'\n{node_name}:\n'
                for (param_name, param_value) in node_data['params'].items():
                    result += f'  {param_name}: {param_value}\n'
    return result
if __name__ == '__main__':
    mcp.run(transport='stdio')