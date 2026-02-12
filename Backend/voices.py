from Backend.module import pyttsx3 , gTTS , pygame , Model, KaldiRecognizer , pyaudio, time



"""

    This is for public use and study purpose with MIT LICENSE. 
    NOTE = There is no guarantee with model for any corruption after modifying it, but without modify it gives
    warranty also

How it will works this file is for handling voices I/O of our Model :) 

Explaining Functions :-

1) Listen = This is a Function Which is Totally for Speech Recognition with vosk for offline and free of cost :)

2) Tell = This is a function with pyttsx3 for Make Model Speak (For Different voice)

3) play = This is the function by with we will play output.mp3 

4) voiceGen = this is a function for generate voice from text using gTTS

"""

def listen(language : str = "en") -> str:
    """

    A voice management System for Speech Recognition With vosk in en, en-in and hindi also, and you can modify
    this for any other language by downloading other language package at vosk official site

    Link = (https://alphacephei.com/vosk/models)

    by this link you will Download your language model

    NOTE = Download small Model bcz they take memory also and cause of memory leak there is no guarantee for that
    ------------------------------

    DESCRIPTION = It takes an input language that language user want and its default is english
    ------------------------------

    More argument*s = `en-in` for Indian English, `hi` For Hindi and english is default
    """

    model = Model(r"D:\Projects\Vosk Models\en-small")
    recognizer = KaldiRecognizer(model, 16000)

    mic = pyaudio.PyAudio()

    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    
    data = stream.read(4096)

    if recognizer.AcceptWaveform(data):
        text : str = recognizer.Result()
        print("User: ",text[14:-3])
        return text[14:-3]


def tell(text : str):
    """Function To Give Model ability of Speaking and being completely on voice based!
        MODULE USED : pyttxs3

    NOTE: Any Curroption of System or memory lose will not be our responsibilty so install all latest Module
    """
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)  
    engine.say(text)
    engine.runAndWait()



def voiceGen(text : str , lang : str = 'en' , file_name : str = 'output.mp3'):
    """
        Methord to generate voices in mp3 file to play 
        MODULE USED: gTTS
        _________________________________
        Argument Information
        ________________

        1) text -> text That Have to Convert to voice in mp3 file
        \n
        2) lang -> Language in that Text to be converted 
            valid Languages - English(en) Default, hindi(hi), indian-English(en-in)
        \n
        3) file_name -> it is defoulty output.mp3 but You can modify it, it is the File where our output mp3 will Store
        _______________________

    """

    outPut = gTTS(text=text, lang=lang)
    outPut.save(file_name)

def play(file_name : str = 'output.mp3'):
    """Function To Play our generated mp3"""
    pygame.mixer.init()
    pygame.mixer.music.set_volume(1.2)
    pygame.mixer.music.load(filename=file_name)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)



