import os
import requests
from openai import OpenAI
from dotenv import load_dotenv
from IPython.display import display, update_display
from IPython.display import Markdown

load_dotenv(override=True)

def stream_api_response(model, messages):   
    api_key = os.getenv('OPENAI_API_KEY')
    base_url = os.getenv("OPENAI_BASE_URL")
    openAI = OpenAI(base_url=base_url, api_key=api_key)
    stream = openAI.chat.completions.create(model=model, messages=messages, stream=True)
    response = ""
    display_handle = display(Markdown(""), display_id=True)
    for chunk in stream:
        response += chunk.choices[0].delta.content or ''
        update_display(Markdown(response), display_id=display_handle.display_id)