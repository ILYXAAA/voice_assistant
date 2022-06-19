from Person import Person
from Assistant import Assistant
from Settings import Settings
from Vk import Vk
from Browser import Browser
from listen import listen


import speech_recognition
import pyttsx3


def main():
    assistant = Assistant()
    person = Person()
    settings = Settings()
    vk = Vk()
    browser = Browser()

    sr = speech_recognition.Recognizer()
    sr.pause_threshold = 0.5

    remove_words = ['пожалуйста', 'прошу', 'хочу', 'чтобы']
    remove_words.append(assistant.name)

    while True:
        say('Слушаю вас')
        task = listen(sr)
        if task == 'стоп' or task == 'stop' or task == 'топ':
            say('До свидания')
            break


        #print(f'There were "{task}" in your speech')
        task_words = []
        for i in range(len(task.split())):
            if task.split()[i] not in remove_words:
                task_words.append(task.split()[i])
        task = ' '.join(task_words)
        print(f'There is "{task}" after cleaning')


        if 'своё' in task and 'имя' in task:
            say('Продиктуйте моё новое имя')
            new_name = listen(sr)
            remove_words.remove(assistant.name)
            assistant.change_name(new_name)
            remove_words.append(assistant.name)
            say(f'Успешно сменила имя на {new_name}')

        elif task == 'как тебя зовут':
            say(f'Меня зовут {assistant.name}')

        elif 'найди в интернете' in task:
            task_words = []
            for i in range(len(task.split())):
                if task.split()[i] not in ['найди', 'поищи', 'интернете', 'в']:
                    task_words.append(task.split()[i])
            task = ' '.join(task_words)
            #say('Продиктуйте запрос')
            #task = listen(sr)
            say('Открываю')
            browser.open_search(task)


def say(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()

if __name__ == '__main__':
    main()
