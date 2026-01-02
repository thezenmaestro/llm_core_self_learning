import os
import requests
from openai import OpenAI
from dotenv import load_dotenv
from IPython.display import display, update_display
from IPython.display import Markdown

def load_env():
    load_dotenv(override=True)
    
    open_api_key = os.getenv('OPENAI_API_KEY')

    if not open_api_key:
        print("No API key was found!")
    elif not open_api_key.startswith("sk-proj-"):
        print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key. Open AI API must start with sk-proj-")
    else:
        print("API key found and looks valid!")

    OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")




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