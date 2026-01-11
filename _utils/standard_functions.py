import os
import requests
from openai import OpenAI
from dotenv import load_dotenv
from IPython.display import display, update_display
from IPython.display import Markdown
from huggingface_hub import login

def load_env():
    load_dotenv(override=True)

    OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")

    openai_api_key      = os.getenv('OPENAI_API_KEY')
    anthropic_api_key   = os.getenv('ANTHROPIC_API_KEY')
    google_api_key      = os.getenv('GOOGLE_API_KEY')
    deepseek_api_key    = os.getenv('DEEPSEEK_API_KEY')
    groq_api_key        = os.getenv('GROQ_API_KEY')
    grok_api_key        = os.getenv('GROK_API_KEY')
    openrouter_api_key  = os.getenv('OPENROUTER_API_KEY')
    hf_token            = os.getenv('HF_TOKEN')

    if hf_token and hf_token.startswith("hf_"):
        print("HF key looks good so far")    
    else:
        print("HF key is not set - please set HF_TOKEN in your .env file")

    if openai_api_key:
        print(f"OpenAI API Key exists and begins with {openai_api_key[:8]}")
    else:
        print("OpenAI API Key not set")

    if google_api_key:
        print(f"Google API Key exists and begins with {google_api_key[:2]}")
    else:
        print("Google API Key not set")
        
    if anthropic_api_key:
        print(f"Anthropic API Key exists and begins with {anthropic_api_key[:7]}")
    else:
        print("Anthropic API Key not set")

    if deepseek_api_key:
        print(f"DeepSeek API Key exists and begins with {deepseek_api_key[:3]}")
    else:
        print("DeepSeek API Key not set")

    if groq_api_key:
        print(f"Groq API Key exists and begins with {groq_api_key[:4]}")
    else:
        print("Groq API Key not set")

    if grok_api_key:
        print(f"Grok API Key exists and begins with {grok_api_key[:4]}")
    else:
        print("Grok API Key not set")

    if openrouter_api_key:
        print(f"OpenRouter API Key exists and begins with {openrouter_api_key[:3]}")
    else:
        print("OpenRouter API Key not set")




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