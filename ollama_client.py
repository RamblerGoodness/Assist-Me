# ollama_client.py
from ollama import Client

OLLAMA_SERVER_URL = "http://your-ollama-server-url"

cl = Client(host=OLLAMA_SERVER_URL)



def query_ollama(question:str , model : str):
    """One off query to ollama server without additional context"""    
    return cl.generate( model, question )


def chat_ollama(conversation , model : str):
        """Chat with ollama server with additional context provided by conversation dict"""
        return cl.chat(model, conversation)

def available_models():
    """List available models on the ollama server"""
    return cl.list()