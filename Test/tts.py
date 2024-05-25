import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Print device
print(device)

# List available 🐸TTS models
print("models:")
for model in TTS().list_models().list_tts_models():
    print(model)
# Init TTS
tts = TTS("tts_models/en/jenny/jenny").to(device)





if __name__ == "__main__":
    tts.tts_to_file(text="Hello, how are you?")