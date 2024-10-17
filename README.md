# reggio-assistant

## Overview
### `reggio-api.py` is the flask API
### `API-call.py` demonstrates how to call the API
### `licenses/licensing.json` is the file containing all the licenses

## Getting started...
- Create the .env file in your root folder following the format documented in `/env-template` and fill up the required info (your OpenAI key for example)
- `python -m venv venv` to create your virtual environment (venv)
- `.\venv\Scripts\activate` to activate that venv
- `pip install -r requirement.txt` to install all prerequisites in this venv

## Flask
- `set FLASK_APP=API.py`
- `set FLASK_ENV=development` to run in debug mode
- `flask run` to start the app, or `flask --app reggio-api.py run`