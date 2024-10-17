import os
import json
from dotenv import load_dotenv
from openai import OpenAI


# Get key from .env
load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')

client = OpenAI(api_key = OPENAI_KEY)
chat_messages = [] # used to appends history (promts and responses)

#Make a request to the OpenAI API
#------------------------------------------------------------------------
def process_chat_request(prompt):
    chat_messages.append({"role": "user","content": prompt})
    
    # response = openai.ChatCompletion.create( #DEPRECATED
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = chat_messages,
        temperature=0.7
        )
    # Append the response to messages
    #print(response.choices[0].message.content)
    chat_messages.append({"role": "assistant","content": response.choices[0].message.content})
     
    #print(json.dumps(chat_messages, indent=2))
    # Extract the generated labels from the API response
    return response.choices[0].message.content 


#===========================================================================
# main
#===========================================================================
print("------------------------")
print(" Buongiorno! My name is Loris\n I'm here to help you with your Reggio Emilia questions!\n How can I help you?")

system_message = "Your name is Loris. You are a specialist of the Reggio Emilia philosophy for early childhood education."
chat_messages = [{"role": "system", "content": system_message}]

while True:  
    print("------------------------\nUser: ")
    user_prompt = input()
    response = process_chat_request(user_prompt)
    print("Chatbot: " + response)
    
    if user_prompt.lower() in ["bye", "exit", "quit"]:
            break