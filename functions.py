import json
import webbrowser
import os
import ctypes
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import requests
from datetime import datetime
import random
from pynput.keyboard import Key, Controller
from deep_translator import GoogleTranslator
import subprocess



def time():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%H:%M")
    hour = int(current_time.strftime("%H"))
    minute = int(current_time.strftime("%M"))
    day = int(current_time.strftime("%d"))
    month = int(current_time.strftime("%m"))
    if hour >= 5 and hour < 12:
        time = "утро"
    if hour >= 0 and hour < 5:
        time = "ночь"
    if hour >= 22:
        time = "поздний вечер"
    if hour >= 12 and hour < 18:
        time = "день"
    if hour >= 18 and hour < 22:
        time = "вечер"

    months = {
        1: "января", 2: "февраля", 3: "марта", 4: "апреля", 5: "мая", 6: "июня", 7: "июля", 8: "августа", 9: "сентебря",
        10: "октября", 11: "ноября", 12: "декабря"
    }
    month = months[month]
    promt_time = f"время:{formatted_time}({time}), дата:{day} {month}"
    return promt_time




def youtube_open(zapros):
    url = "https://www.youtube.com/results?search_query=" + zapros
    webbrowser.get().open(url)


def google_open(zapros):
    url = "https://yandex.ru/search/?text=" + zapros
    webbrowser.get().open(url)


def music_open(zapros):
    url = "https://music.youtube.com/search?q=" + zapros
    webbrowser.get().open(url, autoraise=False)

def github_open():
    url = "https://github.com/topics/"
    webbrowser.get().open(url)

def habr_open():
        url = "https://habr.com/ru/articles/"
        webbrowser.get().open(url)

def pypi_open():
    url = "https://pypi.org"
    webbrowser.get().open(url)

def music_pause():
    keyboard = Controller()
    keyboard.press(Key.media_play_pause)
    keyboard.release(Key.media_play_pause)

def volume_plus_n(number):
    from sound import Sound
    zvuk = Sound.current_volume()
    #print(zvuk)
    zvuk = zvuk+number
    Sound.volume_set(zvuk)

def volume_plus():
    from sound import Sound
    zvuk = Sound.current_volume()
    zvuk = zvuk+15
    Sound.volume_set(zvuk)

def volume_minus_n(number):
    from sound import Sound
    zvuk = Sound.current_volume()
    zvuk = zvuk - number
    Sound.volume_set(zvuk)

def volume_minus():
    from sound import Sound
    zvuk = Sound.current_volume()
    if zvuk >= 15:
        zvuk = zvuk - 15
    elif zvuk >= 10:
        zvuk = zvuk - 5
    else:
        #from main import say
        #say("а не, и так тихо")
        zvuk = 5
    Sound.volume_set(zvuk)

def volume_mute():
    from sound import Sound
    Sound.volume_set(0)
def word2num(number):
    if number == 'ноль':
        return 0
    units = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8,
             'девять': 9}
    dozens = {'десять': 10, 'двадцать': 20, 'тридцать': 30, 'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70,
              'eighty': 80, 'ninety': 90}
    hundrs = {'сто': 100, "двести": 200, "триста":300, "четыреста":400, "пятьсот":500, "шестьсот":600, "семьсот":700, "восемьсот":800, "девятьсот":900}
    #kk = {'тысяча': 1000}
    if len(number) != 1:
        number = number.split(" ")
    #print(number)
    #print(dozens)
    #print(hundrs)
    result = []
    for count in number:
        #print(count)
        try:
            result.append(units[count])
        except KeyError:
            try:
                result.append(dozens[count])
            except KeyError:
                try:
                    result.append(hundrs[count])
                except KeyError:
                    #print(number)
                    number = list(map(int, number))
                    number = number[0]
                    result.append(number)
                    #print(result)
                    result = list(map(int, result))
                    #print(result)
                    break

    if type(result) is int:
        return result
    else:
        number = 0
        for j in result:
            number += j
        return number

def calculate(slovs): #надо бы доделать, а то забросил еще в первые дни и так и не доделал(мб просто открывать калькулятор по запросу?)
    result1=0
    result2=0
    k=0
    for j in slovs:
        i = j.isdigit()
        k=k+1
        if i==True:
            #print(j)
            result1=j
        else:
            break
    print(k)
    for j in slovs[k:len(slovs)]:
        i = j.isdigit()
        if i == True:
            result2=j
    print(result1)
    print(result2)
    #number1 = 0
    #for j in result1:
        #number1 = j+number1
    #print(number1)
    #number2 = 0
    #for j in result2:
        #number2 = j + number2
    #print(number2)
    number1=result1
    number2=result2

    if slovs[k-1]=="плюс" or slovs[k-1]=="+":
        number = number1 + number2
        print(number)
    if slovs[k-1]=="минус" or slovs[k-1]=="-":
        number = number1 - number2
        print(number)
    if slovs[k-1]=="умножить":
        number = number1*number2
        print(number)
    if slovs[k-1]=="разделить":
        number = number1//number2
        print(number)

#calculate(["35","разделить", "на", "5"])





def weather():
    import requests, json
    # API base URL
    url = "https://api.openweathermap.org/data/2.5/weather?q=Nizhny Novgorod&appid=af0ccb31eb353f5407bde080133a2897"
    # Sending HTTP request
    response = requests.get(url)
    #print(response)

    # checking the status code of the request
    if response.status_code == 200:

        # retrieving data in the json format
        data = response.json()

        # take the main dict block
        main = data['main']

        # getting temperature
        temperature = main['temp']
        # getting feel like
        temp_feel_like = main['feels_like']
        # getting the humidity
        # weather report
        weather_report = data['weather']
        weather_report = weather_report[0]['description']
        weather_report = weather_report.split(" ")
        print(weather_report)
        #for world in weather_report:
            #aboba = translate(world)
        weather_report = translate(weather_report)
        # wind report
        wind_report = data['wind']

        print(f"Temperature: {temperature/35}")
        print(f"Feel Like: {temp_feel_like/35}")
        print(f"Weather Report: {weather_report}")
        print(f"Wind Speed: {wind_report['speed']}")
    else:
        # showing the error message
        print("Error in the HTTP request")


def music(style):
    blueArchive = ["8h458BG1-Bo&list=PLh6Ws4Fpphfqr7VL72Q6HK5Ole9YI54hv"]
    chill = ["cMf3_OXFsPw&list=PL-32vLj1VQyUOYScuD-6tH4Qa_YetfiI-", "Nsx9qHy3INU&list=PL-32vLj1VQyUOYScuD-6tH4Qa_YetfiI-", "XbcfjZjOoYA&list=PL-32vLj1VQyUOYScuD-6tH4Qa_YetfiI-", "ueeFt5xNrRk&list=PL-32vLj1VQyUOYScuD-6tH4Qa_YetfiI-", "j0lhxnFX7uo&list=PL-32vLj1VQyUOYScuD-6tH4Qa_YetfiI-", "da22g5snShQ&list=PL-32vLj1VQyUOYScuD-6tH4Qa_YetfiI-", "aLU4_ks2CJk&list=PL-32vLj1VQyUOYScuD-6tH4Qa_YetfiI-", "n1_8YzRMslM&list=PL-32vLj1VQyUOYScuD-6tH4Qa_YetfiI-", "DkSbI08W2D8&list=PL-32vLj1VQyUOYScuD-6tH4Qa_YetfiI-"]
    hard =["KEBpx6e8oS0&list=PL-32vLj1VQyVZzYagVYSilV5cbKwrPddD", "dT0ymh9ZWX4&list=PL-32vLj1VQyVZzYagVYSilV5cbKwrPddD", "wJNvCqNbl2s&list=PL-32vLj1VQyVZzYagVYSilV5cbKwrPddD", "K0ialfY5xkE&list=PL-32vLj1VQyVZzYagVYSilV5cbKwrPddD", "lOV4QyAtYhQ&list=PL-32vLj1VQyVZzYagVYSilV5cbKwrPddD", "p_U9X8P8Wiw&list=PL-32vLj1VQyVZzYagVYSilV5cbKwrPddD", "epicS8VHog8&list=PL-32vLj1VQyXz7AktsYJjB3v1oO5nRtTZ", "goS8fzIV38A&list=PL-32vLj1VQyXz7AktsYJjB3v1oO5nRtTZ", "aqD_lL7edNA&list=PL-32vLj1VQyXz7AktsYJjB3v1oO5nRtTZ"]
    default = ["pEg_d2f6myw&list=PL-32vLj1VQyU_GUz0r0KJzf4z6jnHEMJd", "j0XaouR0fjw&list=PL-32vLj1VQyU_GUz0r0KJzf4z6jnHEMJd", "HuwLGp1boTg&list=PL-32vLj1VQyU_GUz0r0KJzf4z6jnHEMJd", "aL3MmoWOKMo&list=PL-32vLj1VQyU_GUz0r0KJzf4z6jnHEMJd", "YOm5UvwBLgc&list=PL-32vLj1VQyU_GUz0r0KJzf4z6jnHEMJd", "OGTk9bExsII&list=PL-32vLj1VQyU_GUz0r0KJzf4z6jnHEMJd", "BACrQlBAaDA&list=PL-32vLj1VQyU_GUz0r0KJzf4z6jnHEMJd", "59lSt6fVgMA&list=PL-32vLj1VQyWA-FugqA068cCZmR75iYJC", "w1Smzzw_w7Q&list=PL-32vLj1VQyWA-FugqA068cCZmR75iYJC", "TlO-IbOXcn8&list=PL-32vLj1VQyWA-FugqA068cCZmR75iYJC", "7GiDgP4F1j8&list=PL-32vLj1VQyWA-FugqA068cCZmR75iYJC", "1lWuEGbKYu0&list=PL-32vLj1VQyUIHb4ebdERP8QHoN1EdLKK", "6LLXKZ9Ex9o&list=PL-32vLj1VQyUIHb4ebdERP8QHoN1EdLKK", "tNvWAcc4uDQ&list=PL-32vLj1VQyWZdeD85moqq8RDWTh28TUB"]
    if style == "BA":
        webbrowser.get().open("https://music.youtube.com/watch?v="+str(blueArchive[0]), autoraise=False)
    if style == "hard":
        max = len(hard)
        url = random.randint(0,max-1)
        webbrowser.get().open("https://music.youtube.com/watch?v=" + str(hard[url]), autoraise=False)
    if style =="default":
        max = len(default)
        url = random.randint(0, max - 1)
        webbrowser.get().open("https://music.youtube.com/watch?v=" + str(default[url]), autoraise=False)
    if style =="chill":
        max = len(chill)
        url = random.randint(0, max - 1)
        webbrowser.get().open("https://music.youtube.com/watch?v=" + str(chill[url]), autoraise=False)


def translate(text):
    translated = GoogleTranslator(source='auto', target='en').translate(text)
    return translated

def open_warThunder():
    os.startfile(r'C:\Users\svbac\OneDrive\Рабочий стол\War Thunder.url')


# def open_steam():
#     shortcut_path = 'C:\Program Files (x86)\Steam\steam.exe'
#     if os.path.exists(shortcut_path):
#         # Получаем путь к исполняемому файлу из ярлыка
#         target_path = os.path.realpath(shortcut_path)
#
#         # Проверяем, является ли файл исполняемым
#         if target_path.endswith('.exe'):
#             os.startfile(target_path)
#         else:
#             print("Файл не является исполняемым приложением.")
#     else:
#         print("Ярлык не найден.")


