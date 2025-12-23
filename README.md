# MultiModel_bot
# Multi-Modal Chatbot

A chatbot that handles both text and image inputs using Google Gemini AI.

## Features
- 💬 Text conversations
- 🖼️ Image analysis and description
- 🔄 Combined text + image processing
- 🌐 Web interface (Streamlit)
- 💻 CLI interface

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Get Google API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key

### 3. Configure Environment
Edit `.env` file and add your API key:
```
GOOGLE_API_KEY=your_actual_api_key_here
```

## Usage

### Web Interface (Recommended)
```bash
streamlit run app.py
```
- Upload images in the sidebar
- Type messages in the chat input
- Images are automatically analyzed with your text

### CLI Interface
```bash
python cli_chat.py
```
- Type normal text for conversation
- Use `image <path> <prompt>` to analyze images
- Type `quit` to exit

## Examples

### Text Only
```
You: What is machine learning?
Bot: Machine learning is a subset of artificial intelligence...
```

### Image Analysis
```
You: image photo.jpg What do you see in this image?
Bot: I can see a beautiful sunset over mountains...
```

### Web Interface
1. Upload an image in sidebar
2. Type: "Explain what's happening in this image"
3. Get detailed analysis

## Troubleshooting

**API Key Error**: Make sure your `.env` file has the correct API key

**Image Upload Error**: Supported formats: PNG, JPG, JPEG, GIF, BMP

**Connection Error**: Check your internet connection and API key validity
First  check : python test_setup.py 
Secondly : streamlit run app_simple.py
