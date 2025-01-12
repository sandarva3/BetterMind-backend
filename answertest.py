import requests
import json

url = "http://127.0.0.1:8000/answer"
headers = {'Content-Type': 'application/json'}

answers = {
    'answer0':'This is answer0',
    'answer1':'This is answer1',
    'answer2':'This is answer2',
    'answer3':'This is answer3',
    'answer4':'This is answer4',
    'answer5':'This is answer5',
    'answer6':'This is answer6',
    'answer7':'This is answer7',
    'answer8':'This is answer8',
    'answer9':'This is answer9',
}
ID = 5


data = {
    'answers':answers,
    'profId':ID
}

response_data = requests.post(url, json=data, headers=headers)

# response = response_data.json()

# print(f"THE RESPONSE FROM SERVER: {response}")
# print(f"THE STATUS CODE IS: {response_data.status_code}")
# print(f"logged in as: {response['userType']}")


response = response_data.json()
print(f"THE RESPONSE FROM SERVER: {response}")
print(f"THE STATUS CODE IS: {response_data.status_code}")
#print(f"logged in as: {response['userType']}")
print(f"MSG: {response['msg']}")
print(f"THE profId IS: {response['profId']}")
print(f"Processed answers are: ")
for i in response['processedAnswers']:
    print(f"Value: {i}")