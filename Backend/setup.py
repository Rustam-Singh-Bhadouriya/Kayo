
"""

    This is for public use and study purpose with MIT LICENSE. 
    NOTE = NO WARRENTY OR GUARRENTY FOR ANY TECHNICAL ISSUE OF MEMORY CURROPTION 

    IF YOU GOT ANY ERROR OR BUG HELP US TO KNOW CONTRIBUTE A ISSUE ON GITHUB REPO 
    link = (THIS_REPO_GITHUB_LINK)


    this file contains whole Setup of our Assistent

    Structure 
    Setup() = Heart of these all all totaly this is a kernal who called all component
        -> SetupAuto() = For Our Assitent whcih privecy Used btw no tracking used!
        -> ManualSetup() = Only Language need but can't get good exprenience
        -> SetupAI() = Calling both up AI Functions
        -> SetupWiki() = For Wikipedia Article
    
        
    THANK YOU!


"""


from Backend.UserInfo import info
from Backend.voices import  tell, listen
from . import gemini
from Backend.article import get_article
from Frontend.UI import VoiceAssistantGUI
import threading
from Backend.urls import open_website

def SetupAuto():
    print("Checking User Info.....")
    for items,  value in info.items():
        if(value == None):
            print(f"{items} is Empty, Go to Backend/UserInfo.py and change info dict")
            return

    print("Process Done!")
    print(f"Welcome {info['name']}")

    while True:
        UserInput : str= listen(info["language"])

        if UserInput.lower() == "exit":
            break

        if open_website(UserInput):
            continue
        
        else:
            response =  gemini.generate(UserInput, info["language"])
            tell(response)




def manualSetup(lang : str = "en"):
    print("Initializing Kayo AI Bot.....")
    while True:
        UserInput : str= listen(language=lang)
        if UserInput.lower() == "exit":
            break

        response =  gemini.generate(UserInput, lang)
        tell(response)



# Setup Function for AI request
def setupAI():
    info_ask = input("Do you Wanna Share Your Information (y/n): ")
    match info_ask.lower():
        case "y":
            print("Welcome To AI World")
            app = VoiceAssistantGUI()
            t = threading.Thread(target=SetupAuto, daemon=True)
            t.start()
            app.mainloop()

        case "n":
            print("en => english\n hi => hindi\n en-in => indian english")
            language = input("Enter Language by seeing up: ")
            app = VoiceAssistantGUI()
            t = threading.Thread(target=manualSetup, args=(language,), daemon=True)
            t.start()

            app.mainloop()


        case _ :
            print("Enter y/n")
            setupAI()


def SetupWiki():
    if info["language"] == "None" or info['language'] == None:
        print("Enter a Valid Language in UserInfo.py")
        return
    
    Mode : str = input("Enter your Mode: CLI/Voice Command [vc] : ")

    if(Mode.lower() == 'cli'):
        print("enter `exit` to get out of this!")
        while True:
            UserInput : str = input("Enter Article Name: ")
            if UserInput.lower() == 'exit':
                break
            
            tell('Hmm, Let me Search For a While')
            # getting Article
            article = get_article(lang= info["language"], article_name=UserInput)

            tell('listen...')
            tell(article)
    

    else:
        app = VoiceAssistantGUI()
        t = threading.Thread(target=WikiVoice, daemon=True)
        t.start()

        app.mainloop()
        

def WikiVoice():
    print("Speak `Exit` to get out of this!")
        
    while True:
        UserInput : str = listen(info["language"])
        if UserInput.lower() == "exit": break

        article = get_article(lang= info["language"], article_name=UserInput)
        tell(article)

    




# Main Setup Function 
def setup():
    tell("Initializing kayo")

    if(input("AI request [ar] / Wikipedia article [wa]: ") == 'ar'):
        print("Initlizing Kayo...")
        setupAI()
        

    else:
        print("Initlizing Wikipedia...")
        SetupWiki()

    print("Byee, See You again")
    print("Suggest Bug and Fixes on Github, thank you!")

if __name__ == "__main__":
    setup()