import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read the email file
f = open('email.txt', 'r')
email_content = f.read()
f.close()

print("Email content:")
print(email_content)
print("\n" + "="*50 + "\n")

prompt = f"""extract bullet points from the following text:
{email_content}
"""
client = openai.OpenAI(base_url=os.environ["OLLAMA_ENDPOINT"], api_key="nokeyneeded")
MODEL_NAME = os.environ["OLLAMA_MODEL"]
response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {"role": "system", "content": "You are a helpful assistant that extracts bullet points from text."},
        {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message.content)