import streamlit as st
import google.genai as genai
from PIL import Image
import os
from dotenv import load_dotenv
import io

# Load environment variables
load_dotenv()

class MultiModalChatbot:
    def __init__(self):
        self.api_key = os.getenv('GOOGLE_API_KEY')
        if not self.api_key:
            st.error("Please set your GOOGLE_API_KEY in the .env file")
            st.stop()
        
        self.client = genai.Client(api_key=self.api_key)
        
    def process_text_only(self, prompt):
        """Process text-only queries"""
        try:
            response = self.client.models.generate_content(
                model='gemini-1.5-flash',
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"
    
    def process_image_and_text(self, image, prompt):
        """Process image with text prompt"""
        try:
            # Convert PIL image to bytes
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
            
            response = self.client.models.generate_content(
                model='gemini-1.5-flash',
                contents=[
                    prompt,
                    {'mime_type': 'image/png', 'data': img_byte_arr}
                ]
            )
            return response.text
        except Exception as e:
            return f"Error: {str(e)}"
    
    def analyze_image(self, image):
        """Analyze image without specific prompt"""
        prompt = "Describe this image in detail. What do you see?"
        return self.process_image_and_text(image, prompt)

def main():
    st.set_page_config(
        page_title="Multi-Modal Chatbot",
        page_icon="🤖",
        layout="wide"
    )
    
    st.title("🤖 Multi-Modal Chatbot")
    st.markdown("*Chat with text and images using Google Gemini AI*")
    
    # Initialize chatbot
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = MultiModalChatbot()
    
    # Initialize chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Sidebar for options
    with st.sidebar:
        st.header("Options")
        
        # Image upload
        uploaded_file = st.file_uploader(
            "Upload an image", 
            type=['png', 'jpg', 'jpeg', 'gif', 'bmp']
        )
        
        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Clear chat button
        if st.button("Clear Chat"):
            st.session_state.messages = []
            st.rerun()
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message["type"] == "text":
                st.markdown(message["content"])
            elif message["type"] == "image":
                st.image(message["content"], caption="User Image")
    
    # Chat input
    if prompt := st.chat_input("Type your message..."):
        # Add user message to chat history
        st.session_state.messages.append({
            "role": "user", 
            "content": prompt, 
            "type": "text"
        })
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Process based on whether image is uploaded
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                if uploaded_file:
                    # Add uploaded image to chat history
                    st.session_state.messages.append({
                        "role": "user",
                        "content": image,
                        "type": "image"
                    })
                    
                    # Process image with text
                    response = st.session_state.chatbot.process_image_and_text(image, prompt)
                else:
                    # Process text only
                    response = st.session_state.chatbot.process_text_only(prompt)
                
                st.markdown(response)
                
                # Add assistant response to chat history
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response,
                    "type": "text"
                })

if __name__ == "__main__":
    main()