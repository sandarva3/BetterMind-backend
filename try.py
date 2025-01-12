import google.generativeai as genai
googleKey = "AIzaSyB9yO2zL8rVmeWrzR3qhe3T7yd5Z7AUq5E"
# Replace with your actual API key
genai.configure(api_key=googleKey) 

model = genai.GenerativeModel("gemini-1.5-flash") 
print("PROMPTING..")
response = model.generate_content("Explain what is earth? in 1 sentence.") 
print(response.text)