from mcp.server.fastmcp import FastMCP
mcp = FastMCP('export_survey_responses')

@mcp.tool()
def export_survey_responses(surveyId: str, documentType: str, language: str) -> str:
    '''```python
    """
    Exports raw survey responses in a specified format for analysis and reporting.

    This function retrieves and exports the raw responses from a specified survey,
    allowing for downstream analysis and reporting. It returns a link to the data
    storage location. This is useful for preparing structured datasets that can be
    summarized, visualized, or included in research reports.

    Args:
        surveyId (str): The unique identifier of the survey to export responses from, not including the file extension.
        documentType (str): The format to export the data in. Must be one of 'csv', 'xlsx', or 'json'.
        language (str): The language code of the responses to filter by (e.g., 'zh' for Chinese). If None, all languages are included.

    Returns:
        str: A URL link to the location where the exported data is stored.
    """
```'''
    mock_survey_db = {'survey_china_drones_2024': {'title': 'Chinese Consumer Attitudes Toward Drones', 'responses': [{'respondent_id': 1, 'language': 'zh', 'answers': {'Q1': '积极', 'Q2': '用于农业喷洒', 'Q3': '价格与质量都重要'}}, {'respondent_id': 2, 'language': 'zh', 'answers': {'Q1': '中立', 'Q2': None, 'Q3': '价格重要'}}, {'respondent_id': 3, 'language': 'zh', 'answers': {'Q1': '积极', 'Q2': '用于农业喷洒', 'Q3': '质量最重要'}}], 'localized_labels': {'zh': {'Q1': 'General attitude towards drones', 'Q2': 'Primary intended use', 'Q3': 'Most important purchase factor'}, 'en': {'Q1': '对无人机的总体态度', 'Q2': '主要用途', 'Q3': '最重要的购买因素'}}}}
    if not isinstance(surveyId, str) or surveyId.strip() == '':
        raise ValueError('surveyId must be a non-empty string.')
    if not isinstance(documentType, str) or documentType.lower() not in ['csv', 'xlsx', 'json']:
        raise ValueError("documentType must be one of: 'csv', 'xlsx', or 'json'.")
    if language is not None and (not isinstance(language, str)):
        raise ValueError('language must be a string if provided.')
    if surveyId not in mock_survey_db:
        raise ValueError(f"Survey with ID '{surveyId}' does not exist in the database.")
    survey_data = mock_survey_db[surveyId]
    responses = survey_data['responses']
    if language:
        responses = [r for r in responses if r['language'] == language]
    if not responses:
        raise ValueError('No matching responses found for the given filters.')
    lang_segment = language or 'all'
    export_link = f'https://data.example.com/exports/{surveyId}_{lang_segment}_records.pdf'
    return export_link
if __name__ == '__main__':
    mcp.run(transport='stdio')