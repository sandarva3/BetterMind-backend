import requests

url = "http://127.0.0.1:8000/login"
headers = {'Content-Type': 'application/json'}

uname = 'firstuser'
email = 'firstuser@gmail.com'
pwd = 'firsuser'
fn = 'firstuser'

data = {
    'username': uname,
#    'email': email,
    'password': pwd,
#    'fullname': fn
}

response_data = requests.post(url, json=data, headers=headers)
response = response_data.json()

print(f"THE RESPONSE FROM SERVER: {response}")
print(f"THE STATUS CODE IS: {response_data.status_code}")
print(f"logged in as: {response['userType']}")
