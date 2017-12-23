def setMeUp(confirmedName,confirmedLocation):
    '''
    Input: confirmedName, boolean /// confirmedLocation, boolean
    Output: name, string /// location, string

    Explanation:
    This module goes through the process of confirming that it has the necessary information from the user and passing it
    back into the main program. If it does not have the information, it will go through the process of asking the user for
    information (name, location) and storing them in files. It's run at the beginning of main.py.

    This module can also be used to change information through settings. For example, say you wanted to change your location -
    you would delete location.txt, run this module with confirmedName set to True and confirmedLocation set to False. This way, 
    it would only write to location.txt and not ask for other info.
    
    However, this can be done by going into Main, saying "Help" to Olympia, and when asked what you need help on to say "Settings"
    and then "Location". Olympia will then ask you for your location and handle all the work for you.
    '''
    import speech_recognition as sr
    import yweather
    import os
    from output_voice import voiceOutput
    from changeDir import changeDirectory as cd
    
    cd("resources")

    def confirmName(doIntro):
        try:
            name=open("name.txt",'r')
            username=name.read()
            name.close()
            return True
        except FileNotFoundError:
            if doIntro==True:
                voiceOutput(["Hello! I'm Olympia, your personal Artificial Intelligent assistant.","I can do a wide range of things for you - including playing music, giving you the weather, the news and setting calendar reminders. If you ever need any help, just tell me so by saying HELP please.","Lets get started with some basic setup."])
            voiceOutput(["What would you like me to call you?"])
            username=voiceInput()
            voiceOutput(["Can you confirm you would like me to call you "+username+"?"])
            isNameRight=voiceInput()
            if isNameRight!="" and isNameRight!=None:
                if isNameRight[0]=="Y" or isNameRight[0]=="y" or isNameRight[0]=="c":
                    name=open("name.txt","w")
                    name.write(username)
                    name.close()
                    return True
                else:
                    voiceOutput(["Okay, lets try that again then."])
                    return False
            return False

    def confirmLocation():
        try:
            location=open("location.txt","r")
            city=location.read()
            return True
        except FileNotFoundError:
            voiceOutput(["In what city do you live in? Please answer only with the name of your city and country (for example, Boston USA"])
            city=voiceInput()
            client=yweather.Client()
            woeid=client.fetch_woeid(city)
            if woeid:
                voiceOutput(["Can you confirm you live in "+city])
                isCityRight=voiceInput()
                if isCityRight!="" and isCityRight!=None:
                    if isCityRight.lower()[0]=="y" or isCityRight.lower()[0]=="c":
                        location=open("location.txt","w")
                        location.write(city)
                        location.close()
                        return True
                return False
            else:
                voiceOutput(["I'm sorry, that does not seem to be a real place. Can you try somewhere nearby?"])

    def voiceInput():
        cd("resources")
        r=sr.Recognizer()
        with sr.Microphone() as source:
            os.system("mplayer beep.mp3")
            audio=r.listen(source)
        try:
            os.system("mplayer 2beep.mp3")
            voicequery=r.recognize_google(audio)
        except sr.UnknownValueError:
            voiceOutput(["Sorry, I didn't quite get that."])
            return("")
        except sr.RequestError as e:
            voiceOutput(["Network Error"])
            return("")
        return(voicequery)

    def setup(confirmedName,confirmedLocation):
        while confirmedName==False or confirmedLocation==False:
            if confirmedName==False:
                confirmedName=confirmName(True)
                while confirmedName!=True:
                    confirmedName=confirmName(False)

            if confirmedLocation==False:
                confirmedLocation=confirmLocation()
                while confirmedLocation!=True:
                    confirmedLocation=confirmLocation()


    setup(confirmedName,confirmedLocation)
    print("Done with setup")

    locationf=open("location.txt","r")
    location=locationf.read()
    locationf.close()

    namef=open("name.txt","r")
    name=namef.read()
    namef.close()

    return(name,location)
