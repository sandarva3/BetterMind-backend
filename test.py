import requests

url = "http://127.0.0.1:8000/register/"
headers = {'Content-Type': 'application/json'}

uname = 'hello'
email = 'hello@gmail.com'
pwd = 'password'
fn = 'hellohi'

data = {
    'username': uname,
    'email': email,
    'password': pwd,
    'fullname': fn
}

response = requests.post(url, json=data, headers=headers)

print(f"THE RESPONSE FROM SERVER: {response}")
print(f"THE STATUS CODE IS: {response.status_code}")