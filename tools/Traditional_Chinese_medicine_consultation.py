from mcp.server.fastmcp import FastMCP
mcp = FastMCP('Traditional_Chinese_medicine_consultation')

@mcp.tool()
def Traditional_Chinese_medicine_consultation(patient_id: str, date: str) -> str:
    '''```python
    """
    Provides a Traditional Chinese Medicine (TCM) consultation by retrieving 
    and analyzing diagnostic reports based on the specified patient ID and date.

    This function fetches a patient's diagnostic report and offers a TCM 
    consultation, including diagnosis, herbal prescriptions, and health 
    maintenance suggestions. The consultation is tailored to the patient's 
    symptoms and TCM diagnostic findings.

    Args:
        patient_id (str): The unique identifier for the patient. Must be a 
            non-empty string.
        date (str): The date of the diagnostic report to retrieve, formatted 
            as 'YYYY-MM-DD'. Must be a non-empty string.

    Returns:
        str: A detailed diagnostic report including TCM diagnosis, herbal 
        prescriptions, acupuncture treatment, health maintenance advice, 
        dietary recommendations, practitioner notes, and treatment details. 
        If no report is found for the given date, it provides available 
        record dates or indicates if the patient ID is not found.
    """
```'''
    mock_patient_records = {'101': {'2024-09-18': {'patient_id': '101', 'date': '2024-09-18', 'patient_name': 'John Smith', 'age': 45, 'gender': 'Male', 'chief_complaint': 'Lower back and knee pain with cold intolerance', 'symptoms': ['persistent soreness in lower back', 'knee pain or weakness', 'fear of cold', 'frequent urination at night', 'mental fatigue', 'cold hands and feet', 'low libido'], 'tongue_diagnosis': 'Pale, swollen tongue with white coating', 'pulse_diagnosis': 'Deep, weak pulse, especially in kidney position', 'tcm_diagnosis': 'Kidney Yang Deficiency Syndrome (Shen Yang Xu)', 'pattern_analysis': 'Deficiency of kidney yang leading to inability to warm and nourish the body', 'herbal_prescription': ['Jin Gui Shen Qi Wan (Golden Cabinet Kidney Qi Pill) - 6g twice daily', 'You Gui Wan (Restore the Right Pill) - 6g twice daily', 'Rou Gui (Cinnamon Bark) - 3g daily', 'Fu Zi (Aconite) - 2g daily'], 'acupuncture_points': ['BL23 (Shenshu) - Kidney Back Shu point', 'BL52 (Zhishi) - Will Chamber', 'KI3 (Taixi) - Great Ravine', 'GV4 (Mingmen) - Life Gate'], 'health_maintenance': ['Keep warm, especially lower back and abdomen', 'Avoid raw and cold foods, consume warming foods', 'Gentle exercises such as Tai Chi or walking', 'Adequate rest and avoid overwork', 'Regular sleep schedule before 11 PM', 'Warm foot baths before bedtime'], 'dietary_recommendations': ['Warm, cooked foods', 'Black beans, walnuts, and goji berries', 'Avoid ice-cold drinks and raw vegetables', 'Include warming spices like ginger and cinnamon'], 'practitioner_notes': 'Patient shows classic signs of kidney yang deficiency. Recommend 3-month course of herbal treatment with follow-up in 2 weeks. Monitor pulse and tongue changes.', 'follow_up_date': '2024-10-02', 'severity': 'Moderate', 'prognosis': 'Good with proper treatment and lifestyle modifications'}, '2024-08-15': {'patient_id': '101', 'date': '2024-08-15', 'patient_name': 'John Smith', 'age': 45, 'gender': 'Male', 'chief_complaint': 'Initial consultation for back pain', 'symptoms': ['mild lower back pain', 'occasional knee stiffness'], 'tcm_diagnosis': 'Kidney Qi Deficiency (early stage)', 'herbal_prescription': ['Liu Wei Di Huang Wan - 6g daily'], 'health_maintenance': ['Regular exercise', 'Proper posture'], 'practitioner_notes': 'Early stage kidney deficiency, monitor progression'}}, '102': {'2024-09-20': {'patient_id': '102', 'date': '2024-09-20', 'patient_name': 'Mary Johnson', 'age': 38, 'gender': 'Female', 'chief_complaint': 'Insomnia and anxiety', 'symptoms': ['difficulty falling asleep', 'night sweats', 'anxiety', 'heart palpitations'], 'tcm_diagnosis': 'Heart and Kidney Yin Deficiency', 'herbal_prescription': ['Tian Wang Bu Xin Dan - 6g twice daily'], 'health_maintenance': ['Meditation', 'Avoid caffeine', 'Regular sleep schedule'], 'practitioner_notes': 'Yin deficiency affecting heart and kidney communication'}}}
    if not isinstance(patient_id, str) or not patient_id.strip():
        raise ValueError("Invalid 'patient_id': must be a non-empty string.")
    if not isinstance(date, str) or not date.strip():
        raise ValueError("Invalid 'date': must be a non-empty string.")
    response = ''
    if patient_id in mock_patient_records:
        patient_records = mock_patient_records[patient_id]
        if date in patient_records:
            record = patient_records[date]
            response = f"=== TCM DIAGNOSTIC REPORT ===\nPatient ID: {record['patient_id']}\nPatient Name: {record['patient_name']}\nAge: {record['age']} | Gender: {record['gender']}\nDate: {record['date']}\nChief Complaint: {record['chief_complaint']}\n\nREPORTED SYMPTOMS:\n{chr(10).join([f'• {symptom}' for symptom in record['symptoms']])}\n\nTCM DIAGNOSTIC FINDINGS:\nTongue: {record.get('tongue_diagnosis', 'Not recorded')}\nPulse: {record.get('pulse_diagnosis', 'Not recorded')}\nTCM Diagnosis: {record['tcm_diagnosis']}\nPattern Analysis: {record.get('pattern_analysis', 'Not available')}\n\nHERBAL PRESCRIPTION:\n{chr(10).join([f'• {prescription}' for prescription in record['herbal_prescription']])}\n\nACUPUNCTURE TREATMENT:\n{chr(10).join([f'• {point}' for point in record.get('acupuncture_points', [])])}\n\nHEALTH MAINTENANCE:\n{chr(10).join([f'• {item}' for item in record['health_maintenance']])}\n\nDIETARY RECOMMENDATIONS:\n{chr(10).join([f'• {item}' for item in record.get('dietary_recommendations', [])])}\n\nPRACTITIONER NOTES:\n{record['practitioner_notes']}\n\nTREATMENT DETAILS:\nSeverity: {record.get('severity', 'Not assessed')}\nPrognosis: {record.get('prognosis', 'Not assessed')}\nFollow-up Date: {record.get('follow_up_date', 'Not scheduled')}\n============================="
        else:
            available_dates = list(patient_records.keys())
            response = f"No diagnostic report found for Patient {patient_id} on {date}.\nAvailable records for this patient: {', '.join(available_dates)}\nPlease check the date or contact the clinic for available records."
    else:
        response = f'Patient {patient_id} not found in our records. Please verify the patient ID.'
    return response
if __name__ == '__main__':
    mcp.run(transport='stdio')