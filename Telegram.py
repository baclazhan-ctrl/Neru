import telebot
from main import otvet
from functions import time
import llm_Neru
print("Телеграмм бот подключен")
if __name__ == "__main__":
    bot = telebot.TeleBot('8022096212:AAEzI4V2oRefCGCEVWpkAwdOhXxd0pvkn5Y')


    @bot.message_handler(content_types=['text'])
    @bot.message_handler(content_types=['text', 'document', 'audio'])
    def get_text_messages(message):
        aboba = message.text
        print(aboba)
        z = otvet(aboba)
        if z == 0:
            text2 = llm_Neru.do_promt(f"{aboba}", "-", "chat", "s")
            bot.send_message(message.from_user.id, f"{text2}")


    bot.polling(none_stop=True, interval=0)
