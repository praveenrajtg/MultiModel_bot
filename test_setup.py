import os
from dotenv import load_dotenv
import requests
import json

def test_setup():
    """Test if the chatbot setup is working"""
    print("🧪 Testing Multi-Modal Chatbot Setup...")
    
    # Test 1: Environment file
    load_dotenv()
    api_key = os.getenv('GOOGLE_API_KEY')
    
    if not api_key or api_key == 'your_google_api_key_here':
        print("❌ API key not configured. Please update .env file")
        return False
    
    print("✅ API key found")
    
    # Test 2: Google AI connection
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
        
        payload = {
            "contents": [{
                "parts": [{"text": "Say 'Hello, I'm working!' in one sentence"}]
            }]
        }
        
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            result = response.json()
            ai_response = result['candidates'][0]['content']['parts'][0]['text']
            print(f"✅ AI Response: {ai_response}")
        else:
            print(f"❌ AI connection failed: {response.status_code} - {response.text}")
            return False
        
    except Exception as e:
        print(f"❌ AI connection failed: {str(e)}")
        return False
    
    print("\n🎉 Setup is complete! You can now run:")
    print("   streamlit run app_simple.py")
    
    return True

if __name__ == "__main__":
    test_setup()