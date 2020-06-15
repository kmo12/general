import speech_recognition as sr
from gtts import gTTS
import playsound

import random
import os


def respond(audio_string: str):
    tts = gTTS(audio_string, slow=False, lang="ru")
    audio_file_name = "audio-" + str(random.randint(1, 100000)) + ".mp3"
    tts.save(audio_file_name)
    playsound.playsound(audio_file_name)
    os.remove(audio_file_name)


def callback_handler(callback: str):
    callback = callback.lower()
    if callback == "привет":
        respond("Привет, человек!")
    elif callback == "прощай":
        respond("До свидания!")
        exit()
    else:
        respond("Не удалось обработать: " + callback)


r = sr.Recognizer()


def audio_from_microphone():
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            audio_data = r.recognize_google(audio, language="ru-RU")
        except sr.UnknownValueError:
            respond("Я вас не поняла!")
        except sr.RequestError:
            respond("Сервера недоступны")
    return audio_data


callback_handler(audio_from_microphone())