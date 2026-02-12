# Beta


# Copy Right Comment C.
"""

WHAT THIS FILE DO?
this file is only for merging your backend and frontend!

"""

"""
before Running The Program Please Connect a Mic or Something which You're OS detect That as Mic!
"""
from Backend.setup import setup
from Backend.module import downloadModules
import os
import sys
import warnings
warnings.filterwarnings('ignore')
from Frontend.UI import VoiceAssistantGUI
import threading

if __name__ == "__main__":
    try:
        
        setup()
    
    except ModuleNotFoundError as e:
        print(e)
        print("Downloading Modules")
        downloadModules()

        if str(sys.platform) == 'linux':
            os.system('python3 ./run.py')
        else:
            os.system('python ./run.py')
    
    except KeyboardInterrupt:
        print("Keyboard Intrupped Run again if You want...")
