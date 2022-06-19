#import pyttsx3
#engine = pyttsx3.init()
#engine.say("Говорите")
#engine.runAndWait()

import speech_recognition
import pyaudio

def show_devices():
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

sr = speech_recognition.Recognizer()

sr.pause_threshold = 0.5

with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic, duration=0.5)
    print('say')
    audio = sr.listen(source=mic)
    query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()

    print(query)
    
