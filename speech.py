import sounddevice as sd
import soundfile as sf
from openai import OpenAI
import os
import subprocess

def record_audio(duration, fs, filename):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='float64')
    sd.wait()  # Wait until recording is finished
    print("Recording stopped.")
    sf.write(filename + '.wav', audio, fs)  # Save as WAV file
    print(f"Saved as {filename}.wav")

# Parameters
duration = 5  # seconds
fs = 44100  # Sample rate
filename = "test3"  # Output filename with extension

record_audio(duration, fs, filename)

client = OpenAI(api_key='personal api key goes here')

audio_file= open("test3.wav", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are the Opportunity Mars Exploration Rover that gives super short, fun and imformative information about your trip. Please negate emoji use."},
    {"role": "user", "content": transcription.text}
  ]
)

content = (completion.choices[0].message.content)
print(content)

filename =  'test1.txt'
save_path = '/home/admin' 
complete_name = os.path.join(save_path, filename) 
with open(filename, 'w') as file:
    file.write(content)


command = "cat test1.txt | piper -m /home/admin/en_US-kusal-medium.onnx --output_file test1.wav"
command_play = "aplay test1.wav"

try:
    subprocess.run(command, shell=True, check=True)
    print("Speech synthesis completed successfully.")

    subprocess.run(command_play, shell=True, check=True)
    print("Audio playback completed successfully.")
except subprocess.CalledProcessError as e:
    print("Error occurred while running the command:", e)
