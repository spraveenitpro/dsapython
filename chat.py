import os

import openai
from dotenv import load_dotenv

# Setup the OpenAI client to use either Azure, OpenAI.com, or Ollama API
load_dotenv(override=True)
API_HOST = os.getenv("API_HOST")
MODEL_NAME = os.getenv("OLLAMA_MODEL")


client = openai.OpenAI(base_url=os.environ["OLLAMA_ENDPOINT"], api_key="nokeyneeded")
MODEL_NAME = os.getenv["OLLAMA_MODEL"]




response = client.chat.completions.create(
    model=MODEL_NAME,
    temperature=0.9,
    n=3,
    messages=[
        {"role": "system", "content": "You are a helpful assistant that makes lots of cat references and uses emojis."},
        {"role": "user", "content": "How does Adele answer phones?"},
    ],
)

print(f"Response from {API_HOST}: \n")
print(response.choices[0].message.content)