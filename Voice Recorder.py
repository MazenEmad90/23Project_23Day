import sounddevice as sd
import numpy as np
import wave

freq = 44100       
duration = 5       
channels = 1       

print("Recording...")

recording = sd.rec(int(duration * freq), samplerate=freq, channels=channels, dtype='int16')
sd.wait()

print("Recording finished.")

with wave.open("my_recording.wav", "wb") as wf:
    wf.setnchannels(channels)      
    wf.setsampwidth(2)        
    wf.setframerate(freq)         
    wf.writeframes(recording.tobytes())

print("Saved as my_recording.wav")
