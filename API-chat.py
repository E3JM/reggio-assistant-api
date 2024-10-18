import requests

# reggio_assistant license key
API_KEY = 'API_KEY_abc123456def'

# Initialize API parameters
url = 'http://localhost:5000/reggio_assistant'
headers = {'x-api-key': API_KEY}
data = {'input_text': ''}

# Start chat
print("------------------------")
print(" Buongiorno! My name is Loris\n I'm here to help you with your Reggio Emilia questions!\n How can I help you?")

# Enter chat loop
while True:  
    print("------------------------\nUser: ")
    user_prompt = input()
    data['input_text'] += ' ' + user_prompt # Append question to chat messages
    
    # Exit chat if user entered bye, exit or quit
    if user_prompt.lower() in ["bye", "exit", "quit"]:
        print('Good bye! I hope I was able to help you today. Have a wonderful day!')
        break
    
    # Call the reggio_assistant API (POST)
    response = requests.post(url, json=data, headers=headers)
    
    # Exit chat if license in invalid
    if response.status_code == 401:
        print("I'm sorry, but it looks like your license has expired. Please renew to continue using our services\nGoodbye!")
        break

    data['input_text'] += ' ' + response.json().get('output_text') # Append response to chat messages

    #Print response
    print("Loris: " + response.json().get('output_text'))
    

