import torch
from TTS.api import TTS
import os
# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Print device
print( "device: ", device.upper, "\n" )
print("\n")

# List available 🐸TTS models
print("models:")
for model in TTS().list_models().list_tts_models():
    print(model)
print("\n")


# Init TTS
tts = TTS("tts_models/en/jenny/jenny").to(device)


def tts_to_file(text : str, filename="output.wav", autoplay=False):
    """Convert text to speech and save to file"""

    # Synthesize text
    tts.tts_to_file(text=text, file_path=filename)
    if autoplay:
        os.system(f"start {filename}")

if __name__ == "__main__":
    tts_to_file(text="What are you doing in bed, shouldn't you be getting up and taking a shower?")
    os.system("start output.wav")