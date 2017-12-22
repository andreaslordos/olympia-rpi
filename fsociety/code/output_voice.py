'''
Input: textToSay, list (e.g. ["Hello world"] or ["Hello world","My name is Olympia"]
Output: sound
'''

from gtts import gTTS as tts
from tinytag import TinyTag as tt
from time import sleep
from changeDir import changeDirectory as cd
from sys import platform
from os import system
import subprocess
operating_system=platform

def voiceOutput(textToSay):
    try:
        cd("resources")
        fullstr=""
        for strings in textToSay:
            fullstr+=strings+". "
        fullstr=fullstr[:-1]
        whatToSay=tts(text=fullstr,lang='en')
        whatToSay.save("output.mp3")
        audio=tt.get("output.mp3")
        if "linux" in operating_system:
            system("mplayer output.mp3")
        elif "darwin" in operating_system.lower():
            system("afplay output.mp3")
        else:
            subprocess.run("output.mp3",shell=True)
        if "linux" not in operating_system:
            sleep(audio.duration)
    except ConnectionError:
        print("connection error")
    return
 