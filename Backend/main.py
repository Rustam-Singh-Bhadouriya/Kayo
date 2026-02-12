"""

    This is for public use and study purpose with MIT LICENSE. 
    NOTE = There is no guarantie with model for any curroption after modifing it, but without modify it gives
    warrenty also

Main page For you our model For All File Managment in One

"""

from time import sleep
from Backend.setup import setup

def run():
    print("prepraring Files...")
    sleep(3)
    setup()

if __name__ == '__main__':
    run()