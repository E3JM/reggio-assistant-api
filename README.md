# reggio-assistant

## Overview
- `reggio-assistant-api.py` is the flask API calling ChatGPT
  - To use this API, you need a license. The valid licenses are stored in `licenses/licensing.json` 
  - `licensing.json-template` describes the expected structure for the `licensing.json` file. You can make up your own licenses and replace the `API_KEY` parameter in `API-call.py` or `API-chat.py`
- `API-call.py` demonstrates a simple call the API
- `API-chat.py` is an interactive chat example, going back & forth with the reggio-assistant API.

## Getting started...

### Initialize environment
- Create the .env file in your root folder following the format documented in `/env-template` and fill up the required info (your OpenAI key for example)
- `python -m venv venv` to create your virtual environment (venv)
- `.\venv\Scripts\activate` to activate that venv
- `pip install -r requirement.txt` to install all prerequisites in this venv

### Start the API
- `set FLASK_APP=API.py`
- `set FLASK_ENV=development` to if you want to run in debug mode
- `flask run` to start the app, or `flask --app reggio-api.py run`

### Start the chat
- `python .\API-chat.py` to start the chat

## Swagger
https://editor.swagger.io/