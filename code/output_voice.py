'''
Input: textToSay, list (e.g. ["Hello world"] or ["Hello world","My name is Olympia"]
Output: sound
'''

from gtts import gTTS as tts
from changeDir import changeDirectory as cd
from sys import platform
from os import system


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
        system("sudo ffmpeg -i output.mp3 output.wav -y")
        system("sudo aplay output.wav")
        cd("code")
    except Exception as e:
        print(e)
    return
 
