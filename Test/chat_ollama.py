import ollama
from ollama import Client


# Create a client
client = Client(host="http://192.168.0.180:11434/")

#Schema
schema = {
    "message": {
        "type": "string",
        "description": "The message to be sent to the user"
    },
    "emotion": {
        "type": "string",
        "description": "The emotion of the response"
    }
}

# Payload
payload = [
    {'role':'system', 'content': f'You are a helpful AI assistant. You will respond with the best of your abilities. Output in JSON format using the schema defined here: {schema}.'},
    {'role':'user', 'content':'Hello, how are you?'},
]
# Send a message
response = client.chat(format='json', model='dolphin-mistral', messages=payload, stream=False)

print(response['message']['content'])

