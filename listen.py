import speech_recognition

def listen(sr):
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic, duration=0.5)
        audio = sr.listen(source=mic)
        task = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
    return task