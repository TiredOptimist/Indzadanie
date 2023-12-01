# Привет! Это голосовой помощник Нейронов Юрий Рафаэлевич! Я могу рассказать тебе о любом объекте, если ты
# правильно меня об этом попросишь :)
# Просто вызови меня и скажи "Велосипед - это.."
# Не обижайся, но я не всегда способен распознать твою речь! Пожалуйста, наберись терпения...


# pip install SpeechRecognititon
# pip install PyAudio
# pip install gTTS
# pip install playsound==1.2.2
# pip install wikipedia

import speech_recognition
import gtts
import wikipedia
from playsound import playsound

recognition = speech_recognition.Recognizer()
mic = speech_recognition.Microphone()

def get_audio():
    with mic as audio_file:
        recognition.adjust_for_ambient_noise(audio_file)
        audio = recognition.listen(audio_file)
        text = ""
        try:
            text = recognition.recognize_google(audio, language='ru-Ru')
        except Exception as e:
            print("Exception: Ваш голос не распознан. Пожалуйста, повторите!")
        return text.lower()

wakeup = "нейронов юрий рафаэлевич"

begin = gtts.gTTS("Окей, я Вас слушаю!", lang="ru")
begin.save("begin.mp3")

rofl = gtts.gTTS("Я медленно снимаю с себя очки и начинаю отвечать на Ваш вопрос!", lang="ru")
rofl.save("rofl.mp3")

wikipedia.set_lang("ru")

while True:
    print("Я все слышу...")
    text = get_audio()
    if text.count(wakeup) != 0:
        playsound("begin.mp3")
        text = get_audio()
        if text.count("это") != 0:
            playsound("rofl.mp3")
            print(text)
            result = wikipedia.summary(text.replace("это", " "))
            print(result)
            info = gtts.gTTS(result, lang="ru")
            info.save("info.mp3")
            playsound("info.mp3")
