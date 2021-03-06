try:
    '''
    Main - calling program
    This program waits to hear the activation word (Olympia), and then waits to hear the command. Once it has the command, it will send the
    command to determiner.py who will figure out what the user intended, and will then execute code whose output will vary depending on the
    users parameters.
    '''
    import os
    from changeDir import changeDirectory as cd
    cd("code")
    import speech_recognition as sr
    import vlc
    from random import randint
    from time import sleep
    from determiner import determine
    from startup import setMeUp
    from gtts import gTTS as tts
    import threading
    from subprocess import call
    from output_voice import voiceOutput
    from voicein import voiceInGen
    import pafy
    import requests as rq
    import lxml.html
    from aiy.board import Board, Led

    voiceGen = voiceInGen(silent=False)
    activatorGen = voiceInGen(silent=True)
    def voiceInput(silent=False):
        if silent==False:
            return next(voiceGen)
        else:
            return next(activatorGen)

    '''
    def thread_second():
        cd("code")
        call(["python3","alarmclock.py"])
        cd("resources")

    def runAlarm():
        processThread = threading.Thread(target=thread_second)
        processThread.start()
        return
    '''

    def brackets_remove(string):
        returnString=""
        foundBracket=False
        for x in range(len(string)):
            if string[x]!="(" and string[x]!=")" and foundBracket==False:
                returnString+=string[x]
            elif string[x]=="(":
                foundBracket=True
                returnString=returnString[0:-1]
            elif string[x]==")":
                foundBracket=False
        return returnString

    #paused=False

    def buttonPress():
        print("Button was pressed!")
        global flag
        global paused
        if musicPlaying:
            if p.is_playing()==1:
                print("Music was playing and p was on, so I'm pausing")
                p.stop()
                #paused=True
            else:
                print("Music was playing but p was off, so I'm playing")
                p.play()
                paused=False
        else:
            print("Set flag to true")
            flag=True

    name,location=setMeUp(False,False)

    cd("code")
    #runAlarm()
    cd("resources")
    voiceOutput(["Hello, "+name])
    print("To activate me, say 'Olympia'")
    print("Things I can do: play music, tell you the weather, give you the news, answer a question, do some math, define words and tell you a joke")
    autoActivation=False
    wikipediaFlag=False
    flag=False
    lastSong=None
    board=Board()
    board.button.when_pressed = lambda : buttonPress()

    def activationWord():
        global flag
        while True:
            z=voiceInput(silent=True)
            if z.lower()=="olympia" or flag==True:
                print(flag)
                flag=False
                return

    cd("resources")
    jokesF=open("jokes.txt","r")
    jokesL=jokesF.read()
    exec(jokesL)
    cd("code")
    musicPlaying = False

    while True:
        board.led.state = Led.OFF
        activationWord() #will wait until it hears the activation word, and then continues on to the next line
        board.led.state = Led.ON
        cd("code")
        choice=voiceInput() #waiting for a command to be spoken - once a command is spoken, the input will be converted into text
        whatToRun=determine(choice) #determines what the user meant with the command - e.g. did they mean to play music or do math?
        if whatToRun=="tellMeMore" and wikipediaFlag!=True:
            voiceOutput("I haven't searched for anything!")
        elif whatToRun=="tellMeMore" and wikipediaFlag==True:
            import wikipedia
            outstring=brackets_remove([' '.join([wikipedia.summary(wiki_last_search,sentences=3)])])
            outstring=brackets_remove(outstring)
            voiceOutput([outstring])
        elif whatToRun=="music":
            choiceIsPure=False
            import play_music as pm
            volume=80
            if "volume" in choice.split()[-1].lower():
                if "high" in choice.lower():
                    volume=100
                elif "medium" in choice.lower():
                    volume=70
                elif "low" in choice.lower():
                    volume=40
            keywords=["at","a","low","volume","high","medium"]
            choice=choice.split()
            while choice[-1] in keywords:
                choice.pop(-1)
            choice=' '.join(choice)
            if (('again' in choice or 'repeat' in choice) and lastSong!=None):
                choice=lastSong
                choiceIsPure=lastChoiceIsPure
            elif "music" in choice or "song" in choice:
                voiceOutput(["What would you like to listen to?"])
                choice=voiceInput()
                choiceIsPure=True
            lastSong=choice
            lastChoiceIsPure=choiceIsPure
            p=pm.playMusic(choice,choiceIsPure)
            p.audio_set_volume(volume)
            p.play()
            musicPlaying=True
            sleep(10)
            while musicPlaying:
                if p.is_playing()==0:
                    break
                #print("In here")
            print("Done streaming!")
            p.stop()
            musicPlaying=False
        elif whatToRun=="math":
            from do_math import calculate
            answer=calculate(choice)
            if len(str(answer))>3000:
                voiceOutput(["This might take me a very long time.. Give me a moment please."])
            elif len(str(answer))>1000:
                voiceOutput(["This might take me a while. Are you writing all this down?"])
            voiceOutput([calculate(choice)])
        elif whatToRun=="weather":
            import weather_forecast as wf
            forecastedWeather=wf.Forecast(choice)
            voiceOutput([forecastedWeather])
            askedForWeather=False
        elif whatToRun=="wiki":
            import wiki_search as ws
            wiki_tuple=ws.wikipedia(choice,1)
            mod=1
            while True:
                if len(wiki_tuple[0].split())<=2:
                    wiki_tuple=ws.wikipedia(choice,1+mod)
                    mod+=1
                else:
                    break
            wiki_result=wiki_tuple[0]
            wiki_last_search=wiki_tuple[1]
            wikipediaFlag=True
            wiki_result=brackets_remove(wiki_result)
            voiceOutput([wiki_result])
        elif whatToRun=="wolfram":
            voiceOutput(["What is your question?"])
            query=voiceInput()
            if query==None:
                voiceOutput(["Sorry, I didn't quite get that."])
            else:
                from question import answer
                answer=answer(query)
                answer=brackets_remove(answer)
                voiceOutput([answer])
        elif whatToRun=="dict":
            from word_knowledge import wordStuff
            voiceOutput([wordStuff(choice)])
        elif whatToRun=="news":
            import news_update as news
            newsTuple=news.getNews(choice)
            newsString=""
            for news in newsTuple:
                newsString+=news+".. "
            newsString=newsString[:-1]
            voiceOutput(["Sure "+name+".",newsString])
        elif whatToRun=="chance":
            from chance import Chance
            voiceOutput([Chance(choice)])
        elif whatToRun=="alarm":
            from reminder import setAlarm
            try:
                playTime=setAlarm(choice)
                voiceOutput(["Alarm set for "+str(playTime)])
                cd("code")
                runAlarm()
            except:
                voiceOutput(["error"])
        elif whatToRun=="bohemian":
            try:
                pm.playMusic("Bohemian Rhapsody",True)
            except NameError:
                import play_music as pm
                pm.playMusic("Bohemian Rhapsody",True)
        elif choice.lower()=="what is the meaning of life" or choice.lower()=="what is the meaning of life the universe and everything?":
            voiceOutput(["42."])
        elif "joke" in choice.lower():
            try:
                usedjokes=usedjokes
            except NameError:
                usedjokes=["a"]
            if len(usedjokes)==len(jokes):
                usedjokes=["a"]
            joke="a"
            while joke in usedjokes:
                whichJoke=randint(0,len(jokes)-1)
                joke=jokes[whichJoke]
            voiceOutput([joke])
            usedjokes.append(joke)
        elif "bye" in choice:
            voiceOutput(["Goodbye!"])
            os.system("sudo shutdown now")
        elif whatToRun=="ERR":
            voiceOutput(["Sorry, I'm not sure what you want me to do."])
        elif whatToRun=="help":
            voiceOutput(["Which of these do you need help on?","Music? Weather? News? Wikipedia? Settings?"])
            helpChoice=voiceInput()
            if "music" in helpChoice:
                voiceOutput(["To play music, simply say","Can you play... and then tell me the name of the song","Alternatively, you can say","Put on some music and specify the song after I ask you."])
            elif "weather" in helpChoice:
                voiceOutput(["To get the weather, simply say","What's the weather like","and then specify the day that you're looking for.","For example, you could say.","What's the weather like in four days","or you could even say","What's the weather like in a week?","Please keep in mind that I can only see nine days into the future"])
            elif "wikipedia" in helpChoice.lower():
                voiceOutput(["To get information about a topic, simply say", "What is ... and then the name of the topic..", "Alternatively, you could say, 'wikipedia' and then the name of the topic"])
            elif "news" in helpChoice:
                voiceOutput(["To get the news, simply say", "Can you get me the news?", "Alternatively, you could say ","What are the headlines today?","Furthermore, you may specify which newspaper you would like to hear from - the current ones supported are: ","CNN, Fox News, The Economist, The Huffington Post, The New York Times and the Washington Post."])
            elif "settings" in helpChoice:
                voiceOutput(["You can change your settings here.","Currently, you can change your name, location","Which of these would you like to change?"])
                settingToChange=voiceInput()
                settingToChange=settingToChange.lower()
                if "cancel" in settingToChange:
                    print("Cancelling")
                else:
                    didntGetThat=True
                    while didntGetThat==True:
                        cd("resources")
                        didntGetThat=False
                        confirmedName=True
                        confirmedLocation=True
                        if "name" in settingToChange:
                            os.remove("name.txt")
                            confirmedName=False
                        elif "location" in settingToChange or "city" in settingToChange:
                            os.remove("location.txt")
                            confirmedLocation=False
                        else:
                            voiceOutput(["Sorry, I didn't quite get that. Can you repeat?"])
                            settingToChange=voiceInput()
                            didntGetThat=True
                    cd("code")
                    name,location=setMeUp(confirmedName,confirmedLocation)
                    voiceOutput(["Change confirmed."])
except Exception as e:
    print(os.getcwd())
    print(e)
