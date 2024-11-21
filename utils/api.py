import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

def get_completion(prompt, max_tokens=50):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"{prompt}"
            }
        ],
        max_tokens=max_tokens
    )
    return completion.choices[0].message.content