# Import libraries
from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json

#Import the core lib
from core import SystemInfo
#Speech Synthesis
engine = pyttsx3.init()

def speak(text):
  engine.say(text)
  engine.runAndWait()

#Speech recognition

model = Model("model")
rec = KaldiRecognizer(model, 16000)

# Opens microphone for listening.
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(10000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        # result is a string
        result = rec.Result()
        # convert it to a json
        result = json.loads(result)
        text = result['text']

        print(result['text'])

        if text == 'what time is' or text == 'tell me the time':
          speak(SystemInfo.get_time())