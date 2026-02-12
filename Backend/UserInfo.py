# This is for storing Data of User Like user language or other

"""
Only For Storing and Giving Data for no toxic questions

and in every runtime you get a question 

Wanna Use or Share your data 
you can choose yes or no thats depend on you what to share what to not
"""


info = {
        # Change This According to You!
    "name" : None, # your name
    "language" : "en" # Your language For This Model
    # Currently Hindi and English Supported For Other Go to vosk official site and download your desire Model and run that only need to change path
    # and change your current language now you are ready for it!
    }

def giveInfo(arg : str = "name"):
    return info[arg]
        
"""
For better Experience Enter a global Language!
and for no erorr English is Defoult
"""

"""
english = en
hindi = hi
indian-english = en-in

and you can see other on Vosk official Website link in voices.py
"""

if __name__ == "__main__":

    print(giveInfo("language"))

