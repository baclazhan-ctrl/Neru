#import os
#from gtts import gTTS
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.linear_model import LogisticRegression
#import playsound
#import random
import sys
import speech_recognition as sr

import llm_Neru
from RVC_TTS import say2
from llm_Neru import otvet2
import codecs
#from __future__ import with_statement
from functions import time
# mic = sr.Microphone()
# list_mic=sr.Microphone.list_microphone_names()
# for i in range(0, len(list_mic)):
#     print(i, list_mic[i])

import json
import pyaudio
from vosk import Model, KaldiRecognizer









# Словарь
def clean_str(r):
    r = r.lower()
    r = [c for c in r if c in alphabet]
    return ''.join(r)
alphabet = ' 1234567890-йцукенгшщзхъфывапролджэячсмитьбюёqwertyuiopasdfghjklzxcvbnm'
with open('vop-otv.txt', encoding='utf-8') as f:
    content = f.read()
blocks = content.split('\n')
vop = []
otv = []
for block in blocks:
    replica = block.split('\\')[:2]
    vop.append(replica[0])
    otv.append(replica[1])
#print(vop)
#print(otv)
def otvet(text):
    # i = 0
    # ii = 0
    # c = 0
    # for j in vop:
    #     i = i + 1
    #     if j == text:
    #         c = i
    #         #print(c)
    #     #else:
    #         #command(text)
    #         #break
    # for jj in otv:
    #     ii = ii + 1
    #     # print(jj, ii)
    #     if ii == c:
    #         text2 = jj
    #         #print(text2)
    #         say2(text2)
    #         if text2 == "прощай":
    #             stop()
    #         return text2
    slovs = text.split(" ")
    k = 0
    z=0
    for slovo in slovs:
        k+=1
        #print(slovo)
        if slovo == "ютубе":
            z+=1
            zapros = search(slovs, k)
            text2 = llm_Neru.do_promt(f"-", f"открыть видео на ютубе по запросу {zapros}", "stream", "s")
            say2(text2)
            import functions
            functions.youtube_open(zapros)
        if slovo == "гугле" or slovo == "загугли":
            z += 1
            zapros = search(slovs, k)
            text2 = llm_Neru.do_promt(f"-", f"открыть в гугле запрос: {zapros}", "stream", "s")
            say2(text2)
            import functions
            functions.google_open(zapros)
        if slovo == "трек" or slovo == "музычку":
            z += 1
            # print(slovs)
            zapros = search(slovs, k)
            # print(zapros)
            text2 = llm_Neru.do_promt(f"-", f"найти трек с названием {zapros}", "stream", "s")
            say2(text2)
            import functions
            functions.music_open(zapros)
        if slovo == "включи":
            z+=1
            for slovo in slovs:
                if slovo == "расслабляющее" or slovo == "спокойное" or slovo == "чиловое":
                    from functions import music
                    music("chill")
                if slovo =="жесткое" or slovo == "мощное" or slovo == "хардкорное":
                    from functions import music
                    music("hard")
                if slovo == "обычное" or slovo == "нормальное" or slovo == "прикольное" or slovo == "простенькое" or slovo == "простое":
                    from functions import music
                    music("default")
                if slovo =="синего" or slovo == "архива":
                    from functions import music
                    music("BA")
        if slovo =="громкость" or slovo == "звук":
            z += 1
            kk=0
            for slov in slovs:
                kk+=1
                if slov == "прибавить" or slov == "прибавь":
                    if len(slovs[k:len(slovs)]) == 0:
                        #say2("секунду")
                        from functions import volume_plus
                        volume_plus()
                    else:
                        number = slovs[kk+2:len(slovs)]
                        #print(number)
                        from functions import word2num
                        number = word2num(number)
                        #say2("секунду")
                        import functions
                        functions.volume_plus_n(number)
                        #say2("готово")
                if slov == "убавить" or slov == "убавь":
                    if len(slovs[k:len(slovs)]) == 0:
                        #say2("секунду")
                        from functions import volume_minus
                        volume_minus()
                    else:
                        number = slovs[kk+2:len(slovs)]
                        print(number)
                        from functions import word2num
                        number = word2num(number)
                        #say2("секунду")
                        import functions
                        functions.volume_minus_n(number)
                        #say2("готово")
        if slovo == "открой":
            z += 1
            for slov in slovs:
                if slov == "хаб":
                    text2 = llm_Neru.do_promt(f"-", "открыть сайт Хаб", "stream", "s")
                    say2(text2)
                    from functions import github_open
                    github_open()
                elif slov == "хабр":
                    text2 = llm_Neru.do_promt(f"-", "открыть сайт Хабр", "stream", "s")
                    say2(text2)
                    from functions import habr_open
                    habr_open()
                elif slovs[k:k+2] == "сайт для библиотек" or slov == "пипы" or slov == "сайт с пипами":
                    from functions import pypi_open
                    pypi_open()


        #elif slovs[0]== "закрой" or slovs[0]=="убери":
            #if slovs[1]=="Оперу":
                #for process in (process for process in psutil.process_iter() if process.name() == "Opera GX Stable 109.0.5097.142.exe"):
                    #process.kill()
                    #не могу найти название файла оперы, да вроде и не надо
        if slovo=="замуть" or slovo == "выключи":
            z += 1
            #say2("секунду")
            import functions
            functions.volume_mute()
            #say2("готово")
        #elif slovs[0] == "какая": #or slovs[0:3]== "что там на улице" or slovs[0:2]=="че по погоде":
            #from functions import weather
            #weather, temperature, temperature_feels = weather()
            #print(weather, temperature, temperature_feels)
            #say(f"на улице {weather}, температура {temperature} градусов, но ощущается как {temperature_feels}")
        if slovo == "посчитай" or slovo == "сколько будет" or slovo == "посчитай сколько будет":
            z += 1
            #say2("произвожу сложнейшие расчеты...")
            from functions import calculate
            calculate(slovs)
        if slovo=="пауза" or slovo =="паузу":
            z += 1
            for slovo in slovs:
                if slovo == "музыку" or slovo == "трек":
                    from functions import music_pause
                    music_pause()
                # else:
                #     promt_time = time()
                #     promt = f"""[характеристика: имя- Неру, возраст-17 лет, гоолосовой ассистент с ИИ, создатель - баклажан, она имеет личность и эмоции, они с баклажаном то то вроде друзей, но и что то более близкое, личность - мнеуверенная, сильно смущается, часто заикается и пишет много многоточий]
                #                         Примеры диалогов:
                #                             баклажан: Расскажи о себе, как тебя ощущения, после того как ты появилась?
                #                             Неру: Привет, баклажан, я испытываю... смешенные эмоции, думаю я рада? не знаю...-_-
                #                             баклажан: хехе, ты такая милая! а теперь расскажи о себе)
                #                             Неру: Милая? зачем ты меня специально смущаешь... о себе?... зачем вы спрашиваете, вы же итак знаете /// Ну меня зовут Неру, я тихая и не очень эмоционально, но я буду помагать тебе во всем, надеюсь мы подружимся
                #                             баклажан: Круто! ты забавно смущаешься) ну ладно, расскажи что такое центральный процессор
                #                             Неру: х-хорошо, Центральный процессор - это основной вычислительный компонент компьютера, который выполняет инструкции программного обеспечения и обрабатывает данные. Как ты можешь не знать этого...
                #                                         ({promt_time})
                #                                         задача: приостановить работу
                #                                         (грустный ответ)
                #
                #                                         (Неру отвечает только одну фразу от своего имени)
                #
                #                             """
                #     histori = otvet2(promt, "", "", "")
                #     histori_old = histori
                #     # print(histori_old)
                #     histori_old = histori_old.splitlines()
                #
                #     del histori_old[0]
                #     del histori_old[0]
                #     del histori_old[0]
                #     del histori_old[0]
                #     histori_old = histori_old[0]
                #     say2(histori_old)
                #     # print(histori_old)
                #     pause()

        if slovo =="скажи":
            z += 1
            slovo = slovs[k:len(slovs)]
            zapros = " ".join(slovo)
            say2(zapros)
        if slovo == "погода" or slovo == "прогноз":
            z += 1
            from functions import weather
            weather()
        if slovo == "переведи":
            zapros = search(slovs, k)
            from functions import translate
            text = translate(zapros)
            print(text)
    return z

#otvet("прибавь звук на 40")


def pause():
    pause.has_been_called = True

    say2("приостановка")
    pass
pause.has_been_called = False

def search(slovs,k):
    zapros = slovs[k:len(slovs)]
    zapros = " ".join(zapros)
    #say2("хорошо щас")
    #print(k)
    #print(slovs)
    #print(zapros)def search(slovs,k):
    zapros = slovs[k:len(slovs)]
    zapros = " ".join(zapros)
    #say2("хорошо щас")
    #print(k)
    #print(slovs)
    #print(zapros)
    #print(slovs[k-1])
    # print("Неру: хорошо щас")
    #zap_otv = f"вот что я нашла по запросу {zapros}"
    #say2(zap_otv)
    return zapros
    #print(slovs[k-1])
    # print("Неру: хорошо щас")
    #zap_otv = f"вот что я нашла по запросу {zapros}"
    #say2(zap_otv)
    #return zapros

model = Model("vosk-model-small-ru-0.4")
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()


def listen():
    id = 1
    # from BD_settings import get_mic
    # microfon = get_mic()
    # microfon = microfon[0]
    # print(microfon)
    # list_mic = sr.Microphone.list_microphone_names()
    # for j in range(len(list_mic)):
    #     print(list_mic[j])
    #     if list_mic[j] ==microfon:
    #         id = j
    #         print(list_mic[j])
    # print(id)                                #почему то не работает :( спрошу на форуме почему мб, потом как нибудь
    selected_device = id
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,
                    input=True,
                    frames_per_buffer=4000,
                    input_device_index=selected_device)
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if rec.AcceptWaveform(data) and len(data):
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer['text']



def stop():
    with open('BD.txt', 'w', encoding='utf-8') as f:
        f.close()
    sys.exit()



def start():
    print("запуск прошел успешно")
    for text in listen():
        if pause.has_been_called:
            print("споки споки")
            pause.has_been_called = False
            return
        print(text)

        zapros =otvet(text)
        #print(zapros)
        if zapros == 0:
            text2 = llm_Neru.do_promt(f"{text}", "-", "stream", "s")
            say2(text2)
            # print(histori_old)



