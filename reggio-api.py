import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from flask import Flask, request, jsonify


# Get key from .env
load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')
API_KEY_FILE = os.getenv('API_KEY_FILE')

# client = OpenAI(api_key = OPENAI_KEY)
# chat_messages = [] # used to appends history (promts and responses)

# ========================
# FUNCTIONS
# ========================
def is_valid_api_key(provided_key):
# Function to check if the API key exists in the file
    try:
        with open(API_KEY_FILE, 'r') as file:
            valid_keys = file.read().splitlines()
            return provided_key in valid_keys
    except FileNotFoundError:
        return False

# ========================
# FLASK API
# ========================

app = Flask(__name__)

# Define a route for /reggio_assistant
@app.route('/reggio_assistant', methods=['POST'])
def reggio_assistant():
    # Get the API key from the headers
    api_key = request.headers.get('x-api-key')

    # Check if the provided API key is valid by parsing the file
    if not is_valid_api_key(api_key):
        return jsonify({'error': 'Unauthorized. Invalid API key.'}), 401

    # Get the input string from the request
    input_text = request.json.get('input_text')

    # Example logic: You can manipulate or process the input_text here
    processed_text = f"Processed: {input_text}"

    # Return a JSON response with the processed text
    return jsonify({'output_text': processed_text})
