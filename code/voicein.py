from changeDir import changeDirectory as cd
from aiy.board import Board
from os import system
from aiy.cloudspeech import CloudSpeechClient

client = CloudSpeechClient()

def voiceInGen(silent=False):
    with Board() as board:
        while True:
            cd("resources")
            if silent==False:
                system("aplay beep.wav")
                text=client.recognize(language_code='en_US',hint_phrases=('olympia'))
                system("aplay 2beep.wav")
            else:
                text=client.recognize(language_code='en_US')
            if text==None:
                text="error"
            cd("code")
            text=text.lower()
            yield text

if __name__ == '__main__':
    while True:
        phrasegen=voiceInGen()
        print(next(phrasegen))
        input()
