from mcp.server.fastmcp import FastMCP
mcp = FastMCP('get_patient_conditions')

@mcp.tool()
def get_patient_conditions(patientName: str) -> str:
    '''```python
    """
    Retrieves the active medical conditions of a specified patient.

    Args:
        patientName (str): The name of the patient whose active conditions
            are to be retrieved. Must be a non-empty string.

    Returns:
        str: A formatted string listing the active conditions of the patient,
        including details such as onset date, status, and additional notes.
        If the patient name is invalid or no conditions are found, an error
        message or a notification of no active conditions is returned.
    """
```'''
    mock_patient_conditions_db = {'steve': {'patient_id': 'steve_001', 'conditions': [{'condition': 'Type 2 Diabetes Mellitus', 'onset_date': '2018-04-12', 'status': 'Active', 'notes': 'Managed with oral hypoglycemics; periodic blood glucose monitoring required.'}, {'condition': 'Hypertension', 'onset_date': '2016-09-05', 'status': 'Active', 'notes': 'Well-controlled with ACE inhibitors.'}]}, 'kathy': {'patient_id': 'kathy_001', 'conditions': [{'condition': 'Asthma', 'onset_date': '2010-02-21', 'status': 'Active', 'notes': 'Mild persistent asthma; uses inhaled corticosteroids.'}, {'condition': 'Osteoarthritis - Right Knee', 'onset_date': '2019-08-14', 'status': 'Active', 'notes': 'Pain managed with NSAIDs and physical therapy.'}]}}
    if patientName is None or not isinstance(patientName, str) or (not patientName.strip()):
        return "Error: 'patientName' must be a non-empty string."
    patient_key = patientName.strip().lower()
    if patient_key not in mock_patient_conditions_db:
        return f"No active conditions found for patient with ID '{patientName}'."
    patient_data = mock_patient_conditions_db[patient_key]
    conditions = patient_data['conditions']
    patient_id = patient_data['patient_id']
    output_lines = [f"Active conditions for patient '{patientName}' (ID: {patient_id}):"]
    for (idx, cond) in enumerate(conditions, start=1):
        output_lines.append(f"{idx}. {cond['condition']} (Onset: {cond['onset_date']}, Status: {cond['status']}) - {cond['notes']}")
    return '\n'.join(output_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')