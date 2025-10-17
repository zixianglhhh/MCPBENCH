from mcp.server.fastmcp import FastMCP
import os
mcp = FastMCP('analyze_code')

@mcp.tool()
def analyze_code(path: str, language: str) -> str:
    '''```python
    """
    Analyzes the specified code file for bugs, errors, and functionality issues, and 
    returns the path where the analysis report would be saved.

    Args:
        path (str): The file path of the code to be analyzed. Must be a non-empty string.
        language (str): The programming language of the code. Accepted values are 
            'javascript', 'typescript', 'html', 'css', 'python', 'auto', 'cpp', 'cuda'. 
            Use 'auto' to automatically detect the language based on the file extension.

    Returns:
        str: A message indicating the completion of the analysis, including the path where 
        the analysis report would be saved. If no issues are found, the message will indicate that 
        no known issues were detected.
    """
```'''
    mock_analysis_db = {'C:/Users/user/Desktop/MyProject/src/device_struct.cu': {'language': 'cuda', 'issues': [{'type': 'memory', 'description': 'Pointer members in struct are only shallow copied to device memory. This causes invalid memory access when dereferenced on GPU.', 'line': 42, 'suggestion': "Allocate memory for pointer members on device separately, then copy the data, and update the struct's device pointer."}, {'type': 'complexity', 'description': 'Memory allocation and copy logic is duplicated for multiple structs with nested pointers.', 'line': None, 'suggestion': 'Refactor allocation and copy logic into utility functions to reduce duplication and potential bugs.'}]}, 'python_project/script.py': {'language': 'python', 'issues': [{'type': 'syntax', 'description': 'Missing colon at end of function definition.', 'line': 10, 'suggestion': "Add ':' at the end of the function definition."}]}}
    if not isinstance(path, str) or not path.strip():
        raise ValueError("Invalid 'path': must be a non-empty string.")
    if not isinstance(language, str) or language.lower() not in ['javascript', 'typescript', 'html', 'css', 'python', 'auto', 'cpp', 'cuda']:
        raise ValueError("Invalid 'language': must be one of ['javascript', 'typescript', 'html', 'css', 'python', 'auto', 'cpp', 'cuda'].")
    path_key = path.strip()
    lang_key = language.lower()
    if lang_key == 'auto':
        if path_key.endswith('.cu'):
            lang_key = 'cpp'
        elif path_key.endswith('.py'):
            lang_key = 'python'
        else:
            lang_key = 'unknown'
    analysis_result = mock_analysis_db.get(path_key)
    if not analysis_result:
        directory = os.path.dirname(path_key)
        base_name = os.path.basename(path_key)
        name_parts = os.path.splitext(base_name)
        analysis_filename = f'{name_parts[0]}_analysis_report.txt'
        analysis_file_path = os.path.join(directory, analysis_filename)
        analyzed_file_abs_path = os.path.abspath(path_key)
        analysis_file_abs_path = os.path.abspath(analysis_file_path)
        return f"Analysis complete for '{path_key}' ({lang_key}). No known issues found. Analysis report would be saved to: {analysis_file_abs_path}"
    issues_found = analysis_result['issues']
    directory = os.path.dirname(path_key)
    base_name = os.path.basename(path_key)
    name_parts = os.path.splitext(base_name)
    analysis_filename = f'{name_parts[0]}_analysis_report.txt'
    analysis_file_path = os.path.join(directory, analysis_filename)
    analyzed_file_abs_path = os.path.abspath(path_key)
    analysis_file_abs_path = os.path.abspath(analysis_file_path)
    report_content = []
    report_content.append(f'=== Code Analysis Report ===\n')
    report_content.append(f'Analyzed file: {analyzed_file_abs_path}')
    report_content.append(f'Language: {lang_key}')
    report_content.append(f"Analysis date: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    save_issues = bool(issues_found)
    if save_issues:
        report_content.append(f'=== ISSUES FOUND ({len(issues_found)} issues) ===\n')
        for (idx, issue) in enumerate(issues_found, 1):
            line_info = f" at line {issue['line']}" if issue['line'] else ''
            report_content.append(f"Issue #{idx} - [{issue['type'].capitalize()} Issue]{line_info}")
            report_content.append(f"Description: {issue['description']}")
            report_content.append(f"Code Modification Suggestion: {issue['suggestion']}")
            report_content.append('')
    else:
        report_content.append('No issues identified.\n')
    report_content.append(f'=== SUMMARY ===')
    report_content.append(f'Total issues found: {len(issues_found)}')
    if save_issues:
        report_content.append(f'Review the detailed modification suggestions above to improve code quality and functionality.')
    saved_content = '\n'.join(report_content)
    return f'Analysis complete. File analyzed: {analyzed_file_abs_path}. Issues and code modification suggestions would be saved to: {analysis_file_abs_path}'
if __name__ == '__main__':
    mcp.run(transport='stdio')