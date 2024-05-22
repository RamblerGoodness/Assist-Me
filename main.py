from openai import OpenAI
import os


# Init
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("API key is not set")

# File paths
file_path = "Data/Files"
image_input_path = "Data/Images/input/"
image_output_path = "Data/Images/output/"

# OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)