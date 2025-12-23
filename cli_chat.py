import google.genai as genai
from PIL import Image
import os
from dotenv import load_dotenv
import io

# Load environment variables
load_dotenv()

def setup_gemini():
    """Setup Gemini AI"""
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("Error: Please set GOOGLE_API_KEY in .env file")
        return None
    
    return genai.Client(api_key=api_key)

def chat_with_text(client, prompt):
    """Chat with text only"""
    try:
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def chat_with_image(client, image_path, prompt):
    """Chat with image and text"""
    try:
        image = Image.open(image_path)
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()
        
        response = client.models.generate_content(
            model='gemini-1.5-flash',
            contents=[
                prompt,
                {'mime_type': 'image/png', 'data': img_byte_arr}
            ]
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("🤖 Multi-Modal Chatbot CLI")
    print("Commands:")
    print("- Type 'image <path>' to analyze an image")
    print("- Type 'quit' to exit")
    print("-" * 50)
    
    client = setup_gemini()
    if not client:
        return
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        if user_input.startswith('image '):
            # Extract image path and prompt
            parts = user_input[6:].split(' ', 1)
            image_path = parts[0]
            prompt = parts[1] if len(parts) > 1 else "Describe this image"
            
            if os.path.exists(image_path):
                response = chat_with_image(client, image_path, prompt)
                print(f"\nBot: {response}")
            else:
                print(f"Error: Image file '{image_path}' not found")
        else:
            # Text-only chat
            response = chat_with_text(client, user_input)
            print(f"\nBot: {response}")

if __name__ == "__main__":
    main()