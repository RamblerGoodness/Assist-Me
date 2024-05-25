import pygame
import pygame_menu
from pygame_menu import themes
import ollama
from ollama import Client
import openai


class functions():
    pass

class twitch():
    pass

class openai():
    pass

class ollama_ai( ):

    def __init__(self, model, host: str= 'localhost' ):
        self.host = host
        if self.host != None:
            self.client = Client(host=self.host)
        self.model = model


    def chat(self, messages:list, stream:bool=False, model:str = None, format='json'):
        if model == None:
            model = self.model
        

    def options(self):
        pass


class menu():
    pygame.init()
    pass

class TTS():
    import TTS
    pass

class character():
    pass

class stable_diff():
    pass

def main():
    pass

if __name__ == '__main__':
    main()