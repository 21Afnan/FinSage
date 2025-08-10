from NLP import VoiceInput
from Extractor import text_Extractor
import torch
print("GPU Available?", torch.cuda.is_available())
print("CUDA Device Name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU")

class main:
    def __init__(self):
       vi=VoiceInput()
       extractor=text_Extractor(vi.text)
       
main()