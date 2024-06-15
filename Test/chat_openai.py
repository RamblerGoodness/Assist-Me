from openai import OpenAI
import os

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("API key is not set")

client = OpenAI(api_key=OPENAI_API_KEY)


response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)

if __name__ == "__main__":
    
    print("Welcome to the chatbot! Ask me anything or say goodbye to exit.\n")

    while True:
      messages = []
      prompt = input("You: ")
      messages.append({"role": "user", "content": prompt})
      response = client.chat.completions.create(
          model="gpt-4o",
          messages=messages
      )
      print("Bot: ", response.choices[0].message.content, "\n")
      messages.append({"role": "assistant", "content": response.choices[0].message.content})

      if prompt.lower() == "goodbye":
          break