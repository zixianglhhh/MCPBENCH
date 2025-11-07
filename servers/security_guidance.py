from mcp.server.fastmcp import FastMCP
mcp = FastMCP('security_guidance')

@mcp.tool()
def security_guidance(query: str) -> str:
    '''```python
    """
    Provides actionable, non-sensitive security recommendations for applications 
    and data systems based on a given query. The function returns best-practice 
    checklists, minimal configuration or code snippets (e.g., MySQL TLS, 
    least-privilege GRANTs, parameterized queries), data protection advice 
    (e.g., PII handling, encryption at rest/in transit), access control/RBAC 
    patterns, logging and monitoring strategies, and compliance pointers 
    (e.g., GDPR, FERPA). It ensures no secrets are requested or returned, 
    using placeholders in examples.

    Args:
        query (str): A non-empty string representing the security-related 
        question or topic for which guidance is sought.

    Returns:
        str: A string containing security recommendations and best practices 
        tailored to the query, formatted as checklists, code snippets, or 
        advisory notes.
    """
```'''
    if not isinstance(query, str) or not query.strip():
        raise ValueError("Parameter 'query' must be a non-empty string.")
    mock_guidance_db = {'protect data from cyberattacks': 'Security Best Practices for Protecting Data from Cyberattacks:\n1. Implement strong authentication (MFA) for all user accounts.\n2. Enforce least privilege access controls and role-based access control (RBAC).\n3. Keep systems, libraries, and dependencies up-to-date with security patches.\n4. Use encryption at rest (AES-256) and in transit (TLS 1.2+).\n5. Regularly back up data and store backups in a secure, isolated environment.\n6. Monitor logs for suspicious activity and set up automated alerts.\n7. Perform regular security audits and penetration testing.\n8. Train employees on security awareness and phishing prevention.', 'secure mysql connection': "Checklist for Securing a MySQL Connection:\n1. Enable TLS/SSL in MySQL:\n   ```\n   # In my.cnf\n   [mysqld]\n   require_secure_transport = ON\n   ssl_cert = /path/to/server-cert.pem\n   ssl_key = /path/to/server-key.pem\n   ssl_ca = /path/to/ca-cert.pem\n   ```\n2. Create a least-privilege user:\n   ```\n   CREATE USER 'app_user'@'%' IDENTIFIED BY 'PLACEHOLDER_PASSWORD';\n   GRANT SELECT, INSERT, UPDATE, DELETE ON moviedb.* TO 'app_user'@'%';\n   FLUSH PRIVILEGES;\n   ```\n3. Store credentials securely (e.g., environment variables, secrets manager).\n4. Use parameterized queries to prevent SQL injection.\n5. Regularly rotate database credentials.\n6. Restrict network access to trusted IPs only.\n7. Enable query logging and monitor for anomalies.", 'online learning platform privacy': 'Security and Privacy Guidance for an Online Learning Platform:\n1. Collect only the minimum necessary personal data from students.\n2. Encrypt sensitive data at rest using AES-256.\n3. Use HTTPS/TLS for all data in transit.\n4. Implement RBAC: separate roles for students, teachers, and admins with appropriate permissions.\n5. Store credentials in a secure secrets manager — never in source code.\n6. Comply with relevant privacy regulations (e.g., FERPA, GDPR).\n7. Log all access to student records and review logs regularly.\n8. Implement account lockout after repeated failed login attempts.\n9. Provide users with clear privacy policies and obtain consent where required.'}
    normalized_query = query.strip().lower()
    if 'cyberattack' in normalized_query or 'protect data' in normalized_query:
        return mock_guidance_db['protect data from cyberattacks']
    elif 'mysql' in normalized_query or 'secure connection' in normalized_query:
        return mock_guidance_db['secure mysql connection']
    elif 'online learning' in normalized_query or 'student information' in normalized_query or 'privacy' in normalized_query:
        return mock_guidance_db['online learning platform privacy']
    else:
        return 'General Application Security Guidelines:\n1. Apply the principle of least privilege to all systems and services.\n2. Keep all software dependencies updated and patched.\n3. Enforce strong authentication and use MFA where possible.\n4. Encrypt sensitive data both at rest and in transit.\n5. Validate and sanitize all user inputs to prevent injection attacks.\n6. Monitor system logs and set up alerts for suspicious activity.\n7. Back up data regularly and test restoration procedures.\n8. Stay informed about relevant compliance requirements.'
if __name__ == '__main__':
    mcp.run(transport='stdio')