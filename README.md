# Kayo
***A Voice Assistent With Expand of Security and IoT!***

# ✨New Features✨
- ***User Simplicity***
- ***Offline Speech-To-Text (vosk)***
- ***UI Introduced***
- ***Better Automation***
- ***Almost All language Support Added***

## Things To Do 🎈
- **Change Username and Language**
    ```bash
    Backend/UserInfo.py
    ```

    Change Things as yourself!

    ``` bash
        info = {
            # Change This According to You!
        "name" : None, # Change None to You're name like this "Name"
        "language" : "en" # Your language For This Model
        }
    ```

- **Add API Key**

    ***go https://aistudio.google.com/ and Sign up and get API Key***

    ``` bash
    backend/api.py
    api_gemini = "GEMINI-API-KEY" # Paste you're API Key Here!
    ```

- **Download Vosk Model**

    ***Go https://alphacephei.com/vosk/models and Download you're language Model***

    *and paste your model's path at `Backend/voices.py`*

    ```bash
    model = Model(r"D:\Projects\Vosk Models\en-small") # Paste Model Path here
    ```
- **Make Sure You Downloaded Python**
- **Make Sure To Connect a Working Mic**
    

## For More Backend Information Read <a href="Backend/README.md" >Backend Info</a>
## For More Frontend Information Read <a href="Frontend/README.md">Frontend Info</a>


### Thank You!