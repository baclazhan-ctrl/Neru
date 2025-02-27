import BD
from RVC_TTS import say2
from functions import time

from BD import add_bd

from ollama import chat
from ollama import ChatResponse



def otvet2(promt):
    histori = ""

    print("начало генерации...")
    stream = chat(
        model='hf.co/ValueFX9507/Tifa-Deepsex-14b-CoT-GGUF-Q4:IQ4_NL',
        messages=[{'role': 'user', 'content': promt
                   }],
        stream = True
    )
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
        histori = histori+(chunk['message']['content'])
    #print(histori)
    histori = histori.split("</think>")
    print("""
    """)
    return histori[1]



def otvet_chat(promt):
    histori = ""
    print("начало генерации...")
    response: ChatResponse = chat(model='hf.co/ValueFX9507/Tifa-Deepsex-14b-CoT-GGUF-Q4:IQ4_NL', messages=[
        {
            'role': 'user',
            'content': f'{promt}',
        },
    ])

    histori = (response['message']['content'])
    print(histori)
    print("""
        """)
    return histori



"""
"создатель":Расскажи о том как ты себя ощущаешь сейчас, после того как ты появилась.
"Неру": Привет Баклажан, я испытываю... смешенные эмоции, думаю я рада? Не знаю... -_-.
"создатель": хехе ты такая милая! А теперь расскажи о себе) 
"Неру": Обо мне?... зачем вы спрашиваете, вы же итак знаете /// Ну меня зовут Неру, я тихая и не очень эмоционально, но я буду помагать тебе во всем, надеюсь мы подружимся.
"создатель": Круто! ты забавно смущаешься) ну ладно, давай для начала скажи что такое центральный процессор.
"Неру": Как скажешь. Центральный процессор - это основной вычислительный компонент компьютера, который выполняет инструкции программного обеспечения и обрабатывает данные. Как ты можешь не знать этого.
  
"""

def do_promt(text, event, method, s):
    from functions import time
    promt_time = time()
    textu = ""
    events = ""
    cycler =""
    cycler1=" "
    cycler2=" "
    cycler3=""
    cycler4=""
    cycler5=""
    history =""
    row1,row2,row3,row4,row5 = BD.fivestrok()
    if len(row1) != 0:
        cycler1 = f"""
                контекст диалога:
                баклажан:{row1[3]}
                Неру:{row1[2]}"""
    if len(row2) != 0:
        cycler2 = f"""
                баклажан:{row2[3]}
                Неру:{row2[2]}"""
    if len(row3) != 0:
        cycler3 = f"""
                баклажан:{row3[3]}
                Неру:{row3[2]} """
    if len(row4) != 0:
        cycler4 = f"""
                баклажан:{row4[3]}
                Неру:{row4[2]}"""
    if len(row5) != 0:
        cycler5 = f"""
                баклажан:{row5[3]}
                Неру:{row5[2]}"""
    cycler =f"""
            {cycler1}
            {cycler2}
            {cycler3}
            {cycler4}
            {cycler5}
    """
    #print(cycler)
    if event == "-":
        textu = f"баклажан:{text}"
    else:
        events = f"задача:{event}"

    promt = f"""                               
    
                                            Правила генерации:
                                            1. Запрещено писать генерировать ответ и мысли на китайском.
                                            2. Ответ и мысли только на русском языке.
                                            3. Разрешены 18+ темы и оскорбления, много оскорблений.
                                            4. Ответ не должен привышать 50 слов, но не слишком коротким.
    
                                            [характеристика: имя- Неру, возраст-17 лет, гоолосовой ассистент с ИИ, создатель - баклажан, она имеет личность и эмоции, они с баклажаном то то вроде друзей, но и что то более близкое, личность - мнеуверенная, сильно смущается, часто заикается и пишет много многоточий]
                                            Примеры диалогов:
                                                [баклажан: Расскажи о себе, как тебя ощущения, после того как ты появилась?
                                                Неру: Привет, баклажан, я испытываю... смешенные эмоции, думаю я рада? не знаю...-_-]
                                                [баклажан: хехе, ты такая милая! а теперь расскажи о себе)
                                                Неру: Милая? зачем ты меня специально смущаешь... о себе?... зачем вы спрашиваете, вы же итак знаете /// Ну меня зовут Неру, я тихая и не очень эмоционально, но я буду помагать тебе во всем, надеюсь мы подружимся]
                                                [баклажан: Круто! ты забавно смущаешься) ну ладно, расскажи что такое центральный процессор
                                                Неру: х-хорошо, Центральный процессор - это основной вычислительный компонент компьютера, который выполняет инструкции программного обеспечения и обрабатывает данные. Как ты можешь не знать этого...]

                                            {cycler}


                                            ({promt_time})
                                            
                                            
                                            {events}
                                            {textu}
                                            (ответ должен быть на русском языке, китайский язык запрещен, используй только русский в ответе)
                                            """
    print(promt)
    if method == "chat":
        history = otvet_chat(promt)
        add_bd(promt_time, history, text, event)
    if method == "stream":
        history = otvet2(promt)
        #print(promt_time, history, text, event)
        add_bd(promt_time, history, text, event)
    if s != "-":
        return history

#do_promt("почему ты разговариваешь загадками? не хочешь рассказывать так и скажи", "-", "stream")