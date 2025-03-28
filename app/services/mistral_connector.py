import os
from mistralai import Mistral
from mistralai.models import SDKError


MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

def mistral_chat_completion(role, content):
    
    model = "mistral-large-latest"
    
    client=Mistral(api_key=MISTRAL_API_KEY)
    
    try:
        chat_completion = client.chat.complete(
            model= model,
            messages = [
                {
                    "role": role,
                    "content": content,
                },
            ]
        )
        print(chat_completion.choices[0].message.content)
        return chat_completion.choices[0].message
    
    except SDKError as err:
        print(f"Status Code: {err.status_code}")
        print(f"Error: {err.body}")
        return err;
