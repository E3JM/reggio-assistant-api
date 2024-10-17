import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from flask import Flask, request, jsonify



# Get info from .env
load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')
API_KEY_FILE = os.getenv('API_KEY_FILE')

# Initialize OpenAI variables
client = OpenAI(api_key = OPENAI_KEY)
chat_messages = [] # used to appends history (promts and responses)

# Load the license data from the JSON file
with open(API_KEY_FILE, 'r') as license_file:
    license_data = json.load(license_file)



# ========================================================================
# FUNCTIONS
# ========================================================================

def check_license(api_key):
# Check license key sent in API call
    for license_entry in license_data['licenses']:
        if license_entry['license']['apiKey'] == api_key:
            return True
    return False


def process_chat_request(prompt):
# Make a request to the OpenAI API
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



# ========================================================================
# FLASK API
# ========================================================================

app = Flask(__name__)

# Define a route for /reggio_assistant
@app.route('/reggio_assistant', methods=['POST'])
def reggio_assistant():
    print('------------------------')
    print('I am in the reggio_assistant function')
    # Check for API key in header
    api_key = request.headers.get('x-api-key')
    print('Reggio API key value:  ', api_key)
    if not api_key or not check_license(api_key):
        return jsonify({"error": "Invalid or missing API key"}), 401

    # Get input string from request
    api_prompt = request.json.get('input_text')
    print('Reggio API prompt:     ', api_prompt)
    if not api_prompt:
        return jsonify({"error": "Missing input"}), 400

    # Send prompt to ChatGPT
    response = process_chat_request(api_prompt)
    print('------------------------')
    print("Chatbot: " + response)

    # Return a JSON response with the processed text
    return jsonify({'output_text': response})
