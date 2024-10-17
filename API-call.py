import requests

API_KEY = 'API_KEY_abc123456def'

print('Enter your prompt?')
print('---------------------------------------')
PROMPT = input()

url = 'http://localhost:5000/reggio_assistant'
headers = {'x-api-key': API_KEY}
data = {'input_text': PROMPT}

# API call
response = requests.post(url, json=data, headers=headers)

print('---------------------------------------')
print(response)
print('---------------------------------------')
print(response.json())
print('---------------------------------------')
print(response.json().get('output_text'))
