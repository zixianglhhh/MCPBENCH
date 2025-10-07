from mcp.server.fastmcp import FastMCP
mcp = FastMCP('get_health_recommendations')

@mcp.tool()
def get_health_recommendations(age: str, sex: str, pregnancyStatus: str) -> str:
    '''```python
    """
    Get personalized health screening and preventive care recommendations.

    This function provides tailored health recommendations based on the 
    individual's age, sex, and pregnancy status. It considers general 
    vaccinations, healthy habits, age-specific screenings and vaccinations, 
    sex-specific screenings, and pregnancy-specific recommendations.

    Args:
        age (str): The age of the individual as a string. Must be a numeric 
            value (e.g., '30').
        sex (str): The sex of the individual. Accepted values are 'male' or 
            'female'.
        pregnancyStatus (str): The pregnancy status of the individual. 
            Accepted values are 'pregnant' or 'not_pregnant'.

    Returns:
        str: A formatted string containing personalized health recommendations 
        based on the provided age, sex, and pregnancy status. If input 
        validation fails, an error message is returned.
    """
```'''
    mock_health_db = {'general': {'vaccinations': ['Annual influenza vaccine', 'COVID-19 vaccine as per current guidelines', 'Tetanus-diphtheria booster every 10 years'], 'healthy_habits': ['Maintain a balanced diet rich in fruits, vegetables, and whole grains', 'Engage in at least 150 minutes of moderate-intensity exercise weekly', 'Avoid smoking and limit alcohol consumption']}, 'age_groups': {'child': {'screenings': ['Routine pediatric check-ups', 'Vision and hearing screening'], 'vaccinations': ['MMR (Measles, Mumps, Rubella) vaccine', 'Polio vaccine', 'Varicella (chickenpox) vaccine']}, 'adult': {'screenings': ['Blood pressure check every 1-2 years', 'Cholesterol screening every 4-6 years', 'Diabetes screening if overweight or with risk factors']}, 'senior': {'screenings': ['Bone density test for osteoporosis', 'Colorectal cancer screening', 'Hearing and vision tests'], 'vaccinations': ['Pneumococcal vaccine', 'Shingles vaccine']}}, 'sex_specific': {'male': {'screenings': ['Prostate health discussion starting at age 50', 'Testicular self-exam awareness']}, 'female': {'screenings': ['Cervical cancer screening (Pap smear) every 3 years from age 21 to 65', 'Breast cancer screening (mammogram) starting at age 40-50']}}, 'pregnancy': {'pregnant': ['Prenatal vitamins with folic acid', 'Regular prenatal check-ups', 'Screening for gestational diabetes', 'Vaccinations: Influenza and Tdap during pregnancy'], 'not_pregnant': []}}
    try:
        age_int = int(age)
    except ValueError:
        return "Error: Age must be a number in string format (e.g., '30')."
    sex_lower = sex.strip().lower()
    preg_lower = pregnancyStatus.strip().lower()
    if sex_lower not in ['male', 'female']:
        return "Error: Sex must be either 'male' or 'female'."
    if preg_lower not in ['pregnant', 'not_pregnant']:
        return "Error: pregnancyStatus must be either 'pregnant' or 'not_pregnant'."
    if age_int < 18:
        age_group = 'child'
    elif 18 <= age_int < 60:
        age_group = 'adult'
    else:
        age_group = 'senior'
    recommendations = {'General Vaccinations': mock_health_db['general']['vaccinations'], 'Healthy Habits': mock_health_db['general']['healthy_habits'], 'Age-Specific Screenings': mock_health_db['age_groups'].get(age_group, {}).get('screenings', []), 'Age-Specific Vaccinations': mock_health_db['age_groups'].get(age_group, {}).get('vaccinations', []), 'Sex-Specific Screenings': mock_health_db['sex_specific'][sex_lower]['screenings'], 'Pregnancy-Specific Recommendations': mock_health_db['pregnancy'][preg_lower]}
    output_lines = [f"Personalized Health Recommendations for a {age_int}-year-old {sex_lower} ({preg_lower.replace('_', ' ')}):"]
    for (category, items) in recommendations.items():
        if items:
            output_lines.append(f'\n{category}:')
            for item in items:
                output_lines.append(f' - {item}')
    return '\n'.join(output_lines)
if __name__ == '__main__':
    mcp.run(transport='stdio')