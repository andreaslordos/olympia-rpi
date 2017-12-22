def setMeUp(confirmedName,confirmedBirthday,confirmedLocation):
    '''
    Input: confirmedName, boolean /// confirmedBirthday, boolean /// confirmedGender, boolean /// confirmedLocation, boolean
    Output: name, string /// gender, string /// dateofbirth, string /// location, string

    Explanation:
    This module goes through the process of confirming that it has the necessary information from the user and passing it
    back into the main program. If it does not have the information, it will go through the process of asking the user for
    information (name, DOB, location and gender) and storing them in files. It's run at the beginning of main.py.

    This module can also be used to change information through settings. For example, say you wanted to change your location -
    you would delete location.txt, run this module with confirmedName, confirmedGender and confirmedBirthday set to True and
    confirmedLocation set to False. This way, it would only write to location.txt and not ask for other info.
    '''
    import speech_recognition as sr
    import datetime
    import yweather
    import os
    from output_voice import voiceOutput
    from changeDir import changeDirectory as cd
    
    now=datetime.datetime.now()
    year=now.year
    cd("resources")

    def confirmName(doIntro):
        try:
            name=open("name.txt",'r')
            username=name.read()
            name.close()
            return True
        except FileNotFoundError:
            if doIntro==True:
                voiceOutput(["Hello! I'm Olympia, your personal Artificial Intelligent assistant.","I can do a wide range of things for you - including playing music, giving you the weather, the news and setting calendar reminders. If you ever need any help, just tell me so by saying HELP please.","Lets get started with some basic setup. What would you like me to call you?"])
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


    def confirmBirthday(year):
        dict1={"first":"1","second":"2","third":"3","fourth":"4","fifth":"5","sixth":"6","seventh":"7","eigth":"8","ninth":"9","tenth":"10","eleventh":"11","twelfth":"12","thirteenth":"13","fourteenth":"14","fifteenth":"15","sixteenth":"16","seventeenth":"17","eighteenth":"18","nineteenth":"19","twentieth":"20","twenty first":"21","twenty second":"22","twenty third":"23","twenty fourth":"24","twenty fifth":"25","twenty sixth":"26","twenty seventh":"27","twenty eight":"28","twenty ninth":"29","thirtieth":"30","thirty first":"31","1st":"1","2nd":"2","3rd":"3","4th":"4","5th":"5","6th":"6","7th":"7","8th":"8","9th":"9","10th":"10","11th":"11","12th":"12","13th":"13","14th":"14","15th":"15","16th":"16","17th":"17","18th":"18","19th":"19","20th":"20","21st":"21","22nd":"22","23rd":"23","24th":"24","25th":"25","26th":"26","27th":"27","28th":"28","29th":"29","30th":"30","31st":"31"}
        dict2={"january":"1","february":"2","march":"3","april":"4","may":"5","june":"6","july":"7","august":"8","september":"9","october":"10","november":"11","december":"12"}
        try:
            birthday=open("birthday.txt","r")
            dob=birthday.read()
            birthday.close()
            return True
        except FileNotFoundError:
            voiceOutput(["What is your birthday, in the format of day, month and year? (for example first of January, nineteen ninety five","If you prefer not to state it, say so!"])
            dob=voiceInput()
            for word in dob.split():
                if dict1.get(word.lower())!=None:
                    day=int(dict1[word.lower()])
                elif dict2.get(word.lower())!=None:
                    month=int(dict2[word.lower()])
                elif word.isdigit()==True:
                    if int(word)>1900 and int(word)<year:
                        year=int(word)
            correctDate=None
            try:
                dob=datetime.datetime(year,month,day)
                correctDate=True
            except ValueError:
                correctDate=False
            except UnboundLocalError:
                return False

        if correctDate==True:
            dob=str(dob)
            dob=dob[0:10]
            voiceOutput(["Can you confirm you were born on",dob])
            isDobRight=voiceInput()
            if isDobRight!="" and isDobRight!=None:
                if isDobRight.lower()[0]=="c" or isDobRight.lower()[0]=="y":
                    birthday=open("birthday.txt","w")
                    birthday.write(dob)
                    birthday.close()
                    return True
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

    def setup(confirmedName,confirmedBirthday,confirmedLocation):
        while confirmedName==False or confirmedBirthday==False or confirmedLocation==False:
            if confirmedName==False:
                confirmedName=confirmName(True)
                while confirmedName!=True:
                    confirmedName=confirmName(False)

            if confirmedBirthday==False:
                confirmedBirthday=confirmBirthday(year)
                while confirmedBirthday!=True:
                    confirmedBirthday=confirmBirthday(year)

            if confirmedLocation==False:
                confirmedLocation=confirmLocation()
                while confirmedLocation!=True:
                    confirmedLocation=confirmLocation()


    setup(confirmedName,confirmedBirthday,confirmedLocation)
    print("Done with setup")

    locationf=open("location.txt","r")
    location=locationf.read()
    locationf.close()

    dateofbirthf=open("birthday.txt","r")
    dateofbirth=dateofbirthf.read()
    dateofbirthf.close()

    namef=open("name.txt","r")
    name=namef.read()
    namef.close()

    return(name,dateofbirth,location)
