import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
response = requests.get(url)

if response.status_code == 200:
    models = response.json()
    print("Available models:")
    for model in models.get('models', []):
        name = model.get('name', '')
        methods = model.get('supportedGenerationMethods', [])
        if 'generateContent' in methods:
            print(f"- {name}")
else:
    print(f"Error: {response.status_code} - {response.text}")