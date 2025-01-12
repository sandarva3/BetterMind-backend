import openai
from testkey import FIRSTKEY
import json

'''
def rank_professionals_with_gpt(user_data, prof_data):
    client = openai.OpenAI(api_key=test2Key)  # Initialize client with API key
    
    prompt = (
        "You are an expert at matching user needs with professional expertise.\n"
        "Given a user's requirements and a list of professionals' expertise, "
        "rank the professionals based on how well they match the user's needs."
        "\n\n"
        "User Data:\n"
        f"{user_data}\n\n"
        "Professional Data:\n"
        f"{prof_data}\n\n"
        "(IMPORTANT NOTE: ONLY RESPOND IDS OF MATCHING PROFESSIONALS, NOTHING OTHER. IDS MUST BE SEPARATED BY COMMA. THE MOST MATCHING IDS SHOULD BE AT FIRST,"
        " AND LEAST MATCHING AT LAST.)"
    )
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful assistant."},
                  {"role": "user", "content": prompt}],
        temperature=0.7,
    )
    result = response.choices[0].message.content.strip()
    return result
'''

def rank_professionals_with_gpt(user_data, prof_data):
    client = openai.OpenAI(api_key=FIRSTKEY)
    
    # Parse the JSON strings if they're not already dictionaries
    if isinstance(user_data, str):
        user_data = json.loads(user_data)
    if isinstance(prof_data, str):
        prof_data = json.loads(prof_data)

    # Extract only relevant user information
    user_info = {
        "main_issue": next((item["answer"] for item in user_data[0] if item["questionNo"] == 0), ""),
        "duration": next((item["answer"] for item in user_data[0] if item["questionNo"] == 1), ""),
        "previous_therapy": next((item["answer"] for item in user_data[0] if item["questionNo"] == 2), ""),
        "environment": next((item["answer"] for item in user_data[0] if item["questionNo"] == 3), ""),
        "age": next((item["answer"] for item in user_data[0] if "age" in item["question"].lower()), "")
    }

    # Extract only relevant professional information
    professionals = []
    for prof in prof_data:
        if not prof:  # Skip if the prof list is empty
            print("Warning: Empty professional data entry found. Skipping...")
            continue
        prof_info = {
            "id": prof[0]["prof id"],
            "expertise": next((item["answer"] for item in prof if "expertise" in item["question"].lower()), ""),
            "experience": next((item["answer"] for item in prof if "patients" in item["question"].lower()), ""),
            "specialization": next((item["answer"] for item in prof if "problems" in item["question"].lower()), ""),
            "age_group": next((item["answer"] for item in prof if "age patients" in item["question"].lower()), "")
        }
        professionals.append(prof_info)

    prompt = f"""As a professional matching expert, analyze the following user and professional profiles:

User seeking help:
{json.dumps(user_info, indent=2)}

Available professionals:
{json.dumps(professionals, indent=2)}

Based on expertise, experience, and specialization, rank the professionals by their suitability for this user.
Return only the professional IDs in order of best match, separated by commas."""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert at matching mental health professionals with patients."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    
    return response.choices[0].message.content.strip()    


user_data = {
    "id": "user1",
    "answers": ["I need help with machine learning", "Python programming experience required"]
}

prof_data = [
    {"id": "prof1", "answers": ["Expert in Python programming", "Experience in machine learning"]},
    {"id": "prof2", "answers": ["Skilled in JavaScript and frontend development"]},
    {"id": "prof3", "answers": ["Experienced in data science and machine learning"]},
]

# Call the function
# ranked_ids = rank_professionals_with_gpt(user_data, prof_data)
# print(ranked_ids)