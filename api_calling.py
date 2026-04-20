from google import genai
from dotenv import load_dotenv
from gtts import gTTS
import os
import io

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = api_key)

def generate_note(images):
    prompt = """Summarize the picture in note formate at max 100 words make sure to add necessary markdown to differentiate different section in Bangla"""
    
    try:
        res = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=[images, prompt]
        )
        return res.text

    except Exception as e:
        return f"Error generating note: {str(e)}"



# audio transcription
def generate_audio( text ):
    try:
        speech = gTTS(text =text , lang='en', slow=False)
        stream_buffer = io.BytesIO()
        speech.write_to_fp(stream_buffer)
        return stream_buffer
    except Exception as e:
        return f"Error generating audio: {str(e)}"

# quiz generation

def generate_quiz(images,  difficulty):
    prompt = f"Generate a {difficulty} quiz based on the content of the following images: {images} also add the markdown to differentiate the question and answer section"

    try:
        res = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=[images, prompt]
        )
        return res.text
    except Exception as e:
        return f"Error generating quiz: {str(e)}"
    return res.text