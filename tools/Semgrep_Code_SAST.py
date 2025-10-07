from mcp.server.fastmcp import FastMCP
mcp = FastMCP('Semgrep_Code_SAST')

@mcp.tool()
def Semgrep_Code_SAST(path: str, ruleset: str, config_file: str, output_format: str) -> str:
    '''```python
    """
    A static application security testing tool that minimizes noise and empowers
    developers to fix issues with tailored remediation guidance.

    This function performs a security scan on the specified codebase using Semgrep
    rulesets, providing detailed reports on identified security issues along with
    remediation suggestions.

    Args:
        path (str): The file path to the codebase to be scanned. Must be a string.
        ruleset (str): The Semgrep ruleset to apply during the scan. Must be a non-empty string.
        config_file (str): The configuration file for Semgrep settings. Must be a non-empty string.
        output_format (str): The format for the output report. Supported formats are 'json' and 'text'.

    Returns:
        str: A formatted string containing the security scan report, either in JSON or text format,
             based on the specified output_format. The report includes a summary of issues found and
             detailed remediation guidance for each issue.
    """
```'''
    mock_scan_results = {'security': {'json': {'summary': {'total_issues': 3, 'critical': 1, 'high': 1, 'medium': 1, 'low': 0}, 'issues': [{'id': 'SQLI-001', 'type': 'SQL Injection', 'file': 'app/controllers/user_controller.py', 'line': 87, 'severity': 'critical', 'description': 'Unescaped user input in SQL query construction.', 'remediation': 'Use parameterized queries with placeholders.'}, {'id': 'XSS-002', 'type': 'Cross-Site Scripting', 'file': 'app/templates/profile.html', 'line': 42, 'severity': 'high', 'description': 'Unsanitized user input rendered in HTML.', 'remediation': 'Sanitize inputs before rendering.'}, {'id': 'GEN-003', 'type': 'Hardcoded Secret', 'file': 'app/config.py', 'line': 10, 'severity': 'medium', 'description': 'Hardcoded API key found.', 'remediation': 'Remove hardcoded secrets and use environment variables.'}]}, 'text': '=== Semgrep Security Scan Report ===\nCritical: SQL Injection in app/controllers/user_controller.py:87\n    Remediation: Use parameterized queries with placeholders.\nHigh: XSS in app/templates/profile.html:42\n    Remediation: Sanitize inputs before rendering.\nMedium: Hardcoded Secret in app/config.py:10\n    Remediation: Use environment variables instead of hardcoded secrets.\nTotal issues: 3'}, 'sql-injection': {'json': {'summary': {'total_issues': 1, 'critical': 1, 'high': 0, 'medium': 0, 'low': 0}, 'issues': [{'id': 'SQLI-001', 'type': 'SQL Injection', 'file': 'db/query_handler.py', 'line': 56, 'severity': 'critical', 'description': 'Direct string concatenation with user input in SQL statement.', 'remediation': 'Switch to parameterized queries.'}]}, 'text': '=== Semgrep SQL Injection Scan ===\nCritical: SQL Injection in db/query_handler.py:56\n    Remediation: Switch to parameterized queries.\nTotal issues: 1'}, 'xss': {'json': {'summary': {'total_issues': 1, 'critical': 0, 'high': 1, 'medium': 0, 'low': 0}, 'issues': [{'id': 'XSS-002', 'type': 'Cross-Site Scripting', 'file': 'templates/comment.html', 'line': 23, 'severity': 'high', 'description': 'Unsanitized user-supplied data inserted into page.', 'remediation': 'Escape HTML output or use a templating engine with auto-escaping.'}]}, 'text': '=== Semgrep XSS Scan ===\nHigh: XSS in templates/comment.html:23\n    Remediation: Escape HTML output or use auto-escaping.\nTotal issues: 1'}}
    if not ruleset or not isinstance(ruleset, str):
        raise ValueError("Invalid or missing 'ruleset' parameter. Must be a non-empty string.")
    if not config_file or not isinstance(config_file, str):
        raise ValueError("Invalid or missing 'config_file' parameter. Must be a non-empty string.")
    if not output_format or not isinstance(output_format, str):
        raise ValueError("Invalid or missing 'output_format' parameter. Must be a non-empty string.")
    if path is not None and (not isinstance(path, str)):
        raise ValueError("'path' parameter must be a string if provided.")
    ruleset_key = ruleset.lower()
    fmt_key = output_format.lower()
    if ruleset_key not in mock_scan_results:
        if fmt_key == 'json':
            return str({'summary': {'total_issues': 0, 'critical': 0, 'high': 0, 'medium': 0, 'low': 0}, 'issues': []})
        elif fmt_key == 'text':
            return '=== Semgrep Scan Report ===\nNo issues found.'
        else:
            raise ValueError("Unsupported output_format. Supported: 'json', 'text'.")
    if fmt_key not in mock_scan_results[ruleset_key]:
        raise ValueError("Unsupported output_format. Supported: 'json', 'text'.")
    return str(mock_scan_results[ruleset_key][fmt_key])
if __name__ == '__main__':
    mcp.run(transport='stdio')