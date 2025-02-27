from tkinter import *
from PIL import ImageTk, Image
import pyaudio
import tkinter as tk
import asyncio
from tkinter import ttk
from PIL import Image, ImageDraw, ImageTk
#from main import otvet, start
from llm_Neru import do_promt
import speech_recognition as sr
import BD_settings
from main import start


# Создаем главный объект Tk
root = Tk()
root.title("Неру [0.5.0]")
root.geometry("800x800")
root.resizable(False, False)

# # Создаем стиль для вкладок
# style = ttk.Style()
# style.configure("TNotebook.Tab", background="#3C4249", foreground="#270E5F", padding=[10, 5], font=("Helvetica", 8))  # Цвет фона и текста для вкладок
# style.map("TNotebook.Tab", background=[("selected", "darkgray")], foreground=[("selected", "black")])  # Цвет для активной вкладки

# Создаем виджет Notebook
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill=BOTH)

# Создаем фреймы для вкладок
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)

# Добавляем фреймы в качестве вкладок
notebook.add(frame1, text="Главная")
notebook.add(frame2, text="Настройки")
notebook.add(frame3, text="Команды")

# --------------------- Элементы на первой вкладке ---------------------

# # Фоновая метка для первой вкладки
# background_image = Image.open("images/Neru_fon2.jpg")
# background_image = background_image.resize((800, 800), Image.LANCZOS)
# background_photo = ImageTk.PhotoImage(background_image)
# bg_label1 = Label(frame1, image=background_photo)
bg_label1 = Label(frame1, bg="dark gray")
bg_label1.place(relwidth=1, relheight=1)

# Пример добавления элементов на первую вкладку
img = Image.open("images/Neru_standart.jpg")
img = img.resize((310, 310), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
label_img = Label(frame1, image=photo)
label_img.pack()
label_img.place(x=460, y=10)

# Кнопка для запуска
def start_():
    #root.quit()
    #start()
    start()

btn_start = Button(
    frame1,
    text="Запуск",
    command=lambda: start_(),
    bg="#645191",
    fg="#270E5F",
    width=30,
    height=3,
    font=("Arial", 12, "bold"),
    relief="flat"
)
btn_start.place(x=462, y=435)

# Кнопка для паузы
def pause():
    print("Пауза...")

btn_pause = Button(
    frame1,
    text="Пауза",
    command=pause,
    bg="#645191",
    fg="#270E5F",
    width=30,
    height=3,
    font=("Arial", 12, "bold"),
    relief="flat"
)
btn_pause.place(x=462, y=530)

# Кнопка для фонового режима
def open_new_window():

    text_to_help = """~Главная вкладка~
Это то что вы сейчас видите, основная
панель управления голосовым помощником!
Здесь вы не только моежете включать
и выключать Неру, но и использовать
чат для общения с ней текстом.
Под изображением Неру находятся 
индикаторы показывающие ее состояние.
Так же можете обратить внимание на
ТГ бота Неру и GitHub разработчика
в нижнем левом углу, это тоже полезно!

~Настройки~
Здесь вы можете настроить различные
мелочи под себя, включая громкость
голоса, микрофон для ввода и т.д

~Команды!~
Здесь можете не только настроить 
голосовые команды, которые будет
понимать Неру, вы так же можете
изменить ее характер, или Имя!
    """

    help_win = Toplevel(root)
    help_win.title("Навигация и помощь!")
    help_win.geometry("485x600")
    help_win.resizable(False, False)
    help_text = Label(help_win, text=f"{text_to_help}", fg="#270E5F", font=("Helvetica", 17), cursor="hand2",
                      bg="#645191")
    help_text.place(x=0, y=0)

def help():
    open_new_window()

btn_help = Button(
    frame1,
    text="Помощь по боту",
    command=help,
    bg="#645191",
    fg="#270E5F",
    width=13,
    height=3,
    font=("Arial", 12, "bold"),
    relief="flat"
)
btn_help.place(x=462, y=625)

def open_new_window1():

    text_to_help1 = """Неру - голосовой помощник, с встроенным 
исскуственным интелектом,у нее тоже есть
свой Характер!Не обижайте ее! 
Она будет изо всех сил стараться помочь вам 
в ваших делах,поддержит и выслушает!
Вы также можете управлять ПК и общаться 
с ней удаленно, для этого добавьте ТГ бота 
в нижнем правом углу)
    """

    help_win = Toplevel(root)
    help_win.title("Неру?")
    help_win.geometry("505x240")
    help_win.resizable(False, False)
    help_text = Label(help_win, text=f"{text_to_help1}", fg="#270E5F", font=("Helvetica", 17), cursor="hand2",
                      bg="#645191")
    help_text.place(x=0, y=0)

def info():
    open_new_window1()

btn_info = Button(
    frame1,
    text="О Неру",
    command=info,
    bg="#645191",
    fg="#270E5F",
    width=13,
    height=3,
    font=("Arial", 12, "bold"),
    relief="flat"
)
btn_info.place(x=630, y=625)

# фон чата
chat_fon = Frame(frame1, width=405, height=420, bg="#3C4249")
chat_fon.place(x=10, y=350)

# Текстовый ввод
text_box = Text(frame1, width=44, height=2)  # Ширина и высота
text_box.place(x=15, y=725)

def otvet_print(text):
    otvets = do_promt(f"{text}", "-", "chat", "да")
    return otvets

mes = 0

def submit(event=None):
    input_text = text_box.get("1.0", END).strip()
    if input_text:
        print(f"Ввод: {input_text}")
        text_box.delete("1.0", END)
        global mes
        if mes == 0:
            mes1 = Label(frame1, text=f"{input_text}", fg="#270E5F", font=("Helvetica", 10), cursor="hand2",
                         bg="#50565D")
            mes1.place(x=80, y=375)
            mes += 1
        elif mes == 1:
            mes1 = Label(frame1, text=f"{input_text}", fg="#270E5F", font=("Helvetica", 10), cursor="hand2",
                         bg="#50565D")
            mes1.place(x=80, y=425)
        otvet = otvet_print(input_text)
        if mes == 0:
            mes1 = Label(frame1, text=f"{otvet}", fg="#270E5F", font=("Helvetica", 10), cursor="hand2",
                         bg="#50565D")
            mes1.place(x=14, y=400)
        elif mes == 1:
            mes1 = Label(frame1, text=f"{otvet}", fg="#270E5F", font=("Helvetica", 10), cursor="hand2",
                         bg="#50565D")
            mes1.place(x=14, y=450)

text_box.bind('<Return>', submit)
submit_button = Button(frame1, text="Send", command=submit, width=3, height=1, relief="flat")
submit_button.place(x=375, y=725)

def tg_bot(event):
    import webbrowser
    webbrowser.get().open(" https://t.me/Neru_testbot", autoraise=False)

# Создаем текстовую ссылку
tg_url_text = Label(frame1, text="Telegram бот Неру", fg="#9474EE", font=("Helvetica", 12), cursor="hand2",
                    bg="#645191")
tg_url_text.place(x=460, y=730)

# Привязываем событие нажатия мыши к функции open_link
tg_url_text.bind("<Button-1>", tg_bot)

# Добавляем возможность изменения цвета текста при наведении
def on_enter(event):
    tg_url_text.config(fg="#270E5F")  # Изменяем цвет текста при наведении

def on_leave(event):
    tg_url_text.config(fg="#9474EE")

tg_url_text.bind("<Enter>", on_enter)
tg_url_text.bind("<Leave>", on_leave)

def github_url(event):
    import webbrowser
    webbrowser.get().open(" https://github.com/baclazhan-ctrl", autoraise=False)

# Создаем текстовую ссылку
link1 = Label(frame1, text="GitHub создателя", fg="#9474EE", font=("Helvetica", 12), cursor="hand2", bg="#645191", )
link1.place(x=630, y=730)

# Привязываем событие нажатия мыши к функции open_link
link1.bind("<Button-1>", github_url)

# Добавляем возможность изменения цвета текста при наведении
def on_enter1(event):
    link1.config(fg="#270E5F")  # Изменяем цвет текста при наведении

def on_leave1(event):
    link1.config(fg="#9474EE")  # Возвращаем исходный цвет текста при уходе курсора

link1.bind("<Enter>", on_enter1)
link1.bind("<Leave>", on_leave1)



# --------------------- Элементы на вкладке настроек---------------------



bg_label2 = Label(frame2, bg="#606060")
bg_label2.place(relwidth=1, relheight=1)

canvas = tk.Canvas(frame2, bg="#606060")
scrollbar = ttk.Scrollbar(frame2, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)

# Настраиваем прокрутку
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Привязываем полосу прокрутки к Canvas
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.configure(yscrollcommand=scrollbar.set)

audio_title = Label(frame2, text="Аудио", fg="#270E5F", font=("Helvetica", 20), cursor="hand2",bg="#606060")
audio_title.place(x=20, y=25)

mic_set_text = """Использующийся микрофон:"""
mic_setting = Label(frame2, text=mic_set_text, fg="#270E5F", font=("Helvetica", 14), cursor="hand2", bg="#606060")
mic_setting.place(x=15, y=90)

def on_select_input(event):
    selected_value = microfons.get()
    print(f'Вы выбрали: {selected_value}')
    BD_settings.add_mic_to_set(selected_value)
if BD_settings.get_mic()== '-':
    microfon = "Выберите микрофон"
else: microfon = BD_settings.get_mic()
style = ttk.Style()
style.configure("TCombobox",
                font=("Arial", 15),  # Изменение размера шрифта
                padding=5)  # Установка отступов
mic = sr.Microphone()
list_mic = sr.Microphone.list_microphone_names()
list_of_mic = []
list_of_mic=list(set(list_mic))
#list_of_mic.reverse()
microfons = ttk.Combobox(frame2, values=list_of_mic, width=65, background='#645191', foreground='#270E5F')
microfons.set(microfon)
microfons.bind("<<ComboboxSelected>>", on_select_input)
microfons['state'] = 'readonly'
microfons.place(x=270, y=90)

mic_set_text = """Вывод:"""
mic_setting = Label(frame2, text=mic_set_text, fg="#270E5F", font=("Helvetica", 14), cursor="hand2", bg="#606060")
mic_setting.place(x=15, y=130)

def on_select_output(event):
    selected_value = output.get()
    print(f'Вы выбрали: {selected_value}')
    BD_settings.add_output_to_set(selected_value)
if BD_settings.get_mic()== '-':
    output1 = "Выберите устройство вывода"
else: output1 = BD_settings.get_output()
style = ttk.Style()
style.configure("TCombobox",
                font=("Arial", 15),  # Изменение размера шрифта
                padding=5)  # Установка отступов

list_of_out = ["Динамики", "Line 1(VAC)"]
list_of_out=list(set(list_of_out))
#list_of_mic.reverse()
output = ttk.Combobox(frame2, values=list_of_out, width=65, background='#645191', foreground='#270E5F')
output.set(output1)
output.bind("<<ComboboxSelected>>", on_select_output)
output['state'] = 'readonly'
output.place(x=85, y=130)
# Запуск основного цикла
root.mainloop()


root.mainloop()



