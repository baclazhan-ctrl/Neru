"""
import pyttsx3
from gtts import gTTS
import sounddevice as sd


sd.default.samplerate = 48000
sd.default.channels = 2




def say(text):
    engine = pyttsx3.init(driverName='Line 1', debug=True)
    engine.say(text)
    engine.runAndWait()

while True:
    text = input("")
    say(text)

"""

import torch
import os
from datetime import datetime
import sounddevice as sd
from BD_settings import get_output

# Установим устройство по умолчанию для воспроизведения аудио
sd.default.samplerate = 48000
sd.default.channels = 2

if get_output()[0] == "Line 1(VAC)":
    virtual_cable_device_name = 'Line 1 (Virtual Audio Cable), Windows WASAPI'
    sd.default.device = virtual_cable_device_name


# Загрузка модели Silero TTS
def load_tts_model():
    print('[TTS INIT] Начинается загрузка модели TTS...')
    local_file = './silero_tts.pt'
    if not os.path.isfile(local_file):
        torch.hub.download_url_to_file('https://models.silero.ai/models/tts/ru/v3_1_ru.pt', local_file)
    VoiceModel = torch.package.PackageImporter(local_file).load_pickle("tts_models", "model")
    VoiceModel.to(torch.device("cpu"))
    print('[TTS INIT] Модель загружена успешно.')
    return VoiceModel

VoiceModel = load_tts_model()

# Функция для преобразования текста в речь
def say2(text):
    #print(text)
    #print('Запускаем модель...')
    startTime = datetime.now()
    audio = VoiceModel.apply_tts(text=text, speaker='baya', sample_rate=48000, put_accent=True, put_yo=True)
    sd.play(audio, 48000)
    sd.wait()
    #print("время генерации ответа =", (datetime.now() - startTime))



# Пример использования функции textToSpeech
# while True:
#     text = input("")
#     textToSpeech(text)

