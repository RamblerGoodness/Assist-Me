from datetime import datetime
import requests
import json


def get_time():
    return datetime.now().strftime("%H:%M:%S")

get_time = {
    "type": "function",
    "function": {
        "name": "get_time",
        "description": "Get the current time",
        "parameters": {
            "type": "object",
            "properties": {},
        },
        "required": [],

    }
}

# Tos link: https://safety.twitch.tv/s/article/Community-Guidelines?language=en_US
comunity_guidlines = "https://safety.twitch.tv/s/article/Community-Guidelines?language=en_US"

def read_twitch_guidlines():
    response = requests.get(comunity_guidlines)
    return response.text

read__guidlines = { 
    "type": "function",
    "function": {
        "name": "read_twitch_guidlines",
        "description": "Read the twitch community guidelines",
        "parameters": {
            "type": "object",
            "properties": {},
        },
        "required": [],
    }
}

tools = [get_time, read__guidlines]

available_functions = { "get_time": get_time(), "read_twitch_guidlines": read_twitch_guidlines() }

