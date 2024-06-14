# main.py

import pygame
import openai
import os
import dotenv
from Talky import tts_to_file

# Load environment variables from .env file
dotenv.load_dotenv()

openai.api_key = os.getenv("OPEN_AI")

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("TBD")

def get_openai_response(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I couldn't process that."
    

def speak_text(text):
    try:
        tts_to_file(text)
    except Exception as e:
        print(f"Error: {e}")

    pygame.mixer.music.load("output.wav")
    pygame.mixer.music.play()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with a color (e.g., white)
    screen.fill((255, 255, 255))

    # Example: Display AI response
    font = pygame.font.Font(None, 36)
    ai_text = get_openai_response("Hello, how are you?")

    text_surface = font.render(ai_text, True, (0, 0, 0))
    screen.blit(text_surface, (50, 50))

    speak_text(ai_text)
    if pygame.mixer.music.get_busy():
      pygame.time.wait(100)  


    # Update the display
    pygame.display.flip()

pygame.quit()
