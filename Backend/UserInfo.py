# This is for storing Data of User Like user language or other

"""
Only For Storing and Giving Data for no toxic questions

and in every runtime you get a question 

Wanna Use or Share your data 
you can choose yes or no thats depend on you what to share what to not
"""

class userData():
    info = {
        # Change This According to You!
        "name" : None, # your name
        "age" : None, # Your Age
        "class" : None, # Your Class
        "goal" : None, # Your Goal
        "language" : "en" # Your language For This Model
        # Currently Hindi and English Supported For Other Go to vosk official site and download your desire Model and run that only need to change path
        # and change your current language now you are ready for it!
    }

    def giveInfo(self, arg : str = "name"):
        return self.info[arg]
        
"""
For better Experience Enter a global Language!
and for no erorr English is Defoult
"""

"""
english = en
hindi = hi
indian-english = en-in

and you can see other on Vosk official Website link in Voices.py
"""

if __name__ == "__main__":

    data = userData()
    print(data.info)

