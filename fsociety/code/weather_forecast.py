'''
This is really bad code. But it works better than almost any other module, so I don't really want to touch it.
Essentially, it figures out the day (don't ask me how) the user wants data on, gets data from Yahoo's weather API and returns it to main
'''
def Forecast(userinput):
    import yweather
    from yahooweather import YahooWeather,UNIT_C
    import logging
    from datetime import datetime as dt
    from random import randint
    from changeDir import changeDirectory as cd
    
    client=yweather.Client()
    cd("resources")
    location=open("location.txt","r")
    city=location.read()
    location.close()
    woeid=client.fetch_woeid(city)
    logging.basicConfig(level=logging.WARNING)
    yweather=YahooWeather(woeid,UNIT_C)
    datelist=["Tomorrow","tomorrow","days","today","week","today","Tomorrow?","tomorrow?","today?","week?","days?"]
    prefixdatelist=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh","twelfth","thirteenth","fourteenth","fifteenth","sixteenth","seventeenth","eighteenth","nineteenth","twentieth","twenty first","twenty second","twenty third","twenty fourth","twenty fifth","twenty sixth","twenty seventh","twenty eight","twenty ninth","thirtieth","thirty first"]
    numberlist=["nine","eight","seven","six","five","four","three","two","one","1","2","3","4","5","6","7","8","9"]
    monthlist=["january","february","march","april","may","june","july","august","september","october","november","december","january?","february?","march?","april?","may?","june?","july?","august?","september?","october?","november?","december?"]
    daylist=["monday","tuesday","wednesday","thursday","friday","saturday","sunday","monday?","tuesday?","wednesday?","thursday?","friday?","saturday?","sunday?"]
    ignore=["What's","whats","what","is","like", "the","in","on", "What","will","be"]
    dict1={"first":"1","second":"2","third":"3","fourth":"4","fifth":"5","sixth":"6","seventh":"7","eigth":"8","ninth":"9","tenth":"10","eleventh":"11","twelfth":"12","thirteenth":"13","fourteenth":"14","fifteenth":"15","sixteenth":"16","seventeenth":"17","eighteenth":"18","nineteenth":"19","twentieth":"20","twenty first":"21","twenty second":"22","twenty third":"23","twenty fourth":"24","twenty fifth":"25","twenty sixth":"26","twenty seventh":"27","twenty eight":"28","twenty ninth":"29","thirtieth":"30","thirty first":"31"}
    dict2={"january?":"Jan","february?":"Feb","march?":"Mar","april?":"Apr","may?":"May","june?":"Jun","july?":"Jul","august?":"Aug","september?":"Sep","october?":"Oct","november?":"Nov","december?":"Dec","january?":"Jan","february?":"Feb","march?":"Mar","april?":"Apr","may?":"May","june?":"Jun","july?":"Jul","august?":"Aug","september?":"Sep","october?":"Oct","november?":"Nov","december?":"Dec"}
    dict3={"Wed":"Wednesday","Mon":"Monday","Tue":"Tuesday","Thu":"Thursday","Fri":"Friday","Sat":"Saturday","Sun":"Sunday"}
    year=dt.today().year
    #step 1: Identify they're talking about the weather (keywords: hot, cold, weather)
    #step 2: Identify which day they're talking about ()
    if yweather.updateWeather():
        forecast=yweather.Forecast

    def genList(forecast):
        #generates list of possible days the user can ask for
        dayList=[]
        for x in range(len(forecast)-1):
            dayList.append(forecast[x]['day'])
        return dayList



    def identifyDay(userinput):
            ignoreFirst=False
            searchDay=""
            listofinput=userinput.split()
            dayList=genList(forecast)
            for word in listofinput:
                if word in ignore:
                    searchDay=searchDay #filler
                elif word in datelist: #done with datelist (Completed)
                    if word=="days" or word=="days?":
                        number=listofinput[-2]
                        if number in numberlist:
                            if number=="seven" or number=="eight" or number=="nine" or number=="7" or number=="8" or number =="9":
                                ignoreFirst=True
                            if number=="one" or number=="eight" or number=="8" or number=="1":
                                searchDay=dayList[1]
                            elif number=="two" or number=="nine" or number=="2" or number=="9":
                                searchDay=dayList[2]
                            elif number=="three" or number=="3":
                                searchDay=dayList[3]
                            elif number=="four" or number=="4":
                                searchDay=dayList[4]
                            elif number=="five" or number=="5":
                                searchDay=dayList[5]
                            elif number=="six" or number=="6":
                                searchDay=dayList[6]
                            elif number=="seven" or number=="7":
                                searchDay=dayList[7]
                    elif word.lower()=="tomorrow" or word.lower()=="tomorrow?":
                        searchDay=dayList[1]
                    elif word=="today" or word=="today?":
                        searchDay=dayList[0]
                    elif word=="week" or word=="week?":
                        searchDay=dayList[7]
                        ignoreFirst=True
                    else:
                        print("ERROR")
                    returnTuple=(ignoreFirst,searchDay)
                    return(returnTuple)

                elif word.lower() in monthlist:
                    foundDate=False
                    searchNumber=0
                    day=""
                    fulldate=""
                    month=""
                    for x in range(len(prefixdatelist)):
                        if prefixdatelist[x] in userinput:
                            day=dict1[prefixdatelist[x]]
                    month=dict2[word.lower()]
                    fulldate=str(day)+" "+str(month)+" "+str(year)
                    while foundDate==False and searchNumber<9:
                        if searchNumber>6 and ignoreFirst==False:
                            ignoreFirst=True
                        if forecast[searchNumber]['date']==fulldate:
                            foundDate=True
                            searchDay=forecast[searchNumber]['day']
                        searchNumber+=1

                    returnTuple=(ignoreFirst,searchDay)
                    return(returnTuple)


                elif word.lower() in daylist:
                    if "next" in userinput.lower():
                        ignoreFirst=True
                    for x in range(len(dayList)):
                        if dayList[x].lower() in word.lower():
                            searchDay=dayList[x]
                            break
                    returnTuple=(ignoreFirst,searchDay)
                    return(returnTuple)
    """
    def runTests():
        tempdaylist=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","next Monday","next Tuesday","next Wednesday"]
        listofresults=[]
        for x in range(len(tempdaylist)):
            getTuple=identifyDay("What's the weather like on "+tempdaylist[x]+"?")
            forecastedweather=forecastWeather(getTuple)
            listofresults.append(forecastedweather)
        print(listofresults)
    """


    def forecastWeather(returnTuple):
        ignoreFirst=returnTuple[0]
        searchDay=returnTuple[1]
        nextDay=False
        for x in range(len(forecast)):
            if forecast[x]['day']==searchDay:
                if ignoreFirst==False:
                    hightemp=forecast[x]['high']
                    lowtemp=forecast[x]['low']
                    text=forecast[x]['text']
                    date=forecast[x]['date']
                    day=forecast[x]['day']
                    break
                else:
                    ignoreFirst=False
                    nextDay=True
        infoTuple=(hightemp,lowtemp,text,date,day,nextDay)
        return(infoTuple)


    def outputComment(forecastedWeather):
        comment=""
        temp=int(forecastedWeather[0][0])
        text=forecastedWeather[0][2].lower()
        fullcomment=forecastedWeather[1]
        if text=="rain":
            text="rainy"
        if (text=="mostly sunny" or text=="sunny") and temp<=33 and temp>=24:
            comment=("Sounds like an amazing day to go out!")
        elif (text=="mostly sunny" or text=="sunny" or text=="partly cloudy") and temp>35:
            choice=randint(1,2)
            if choice==1 or "cloudy" in text:
                comment=("It might be hot outside - stay hydrated!")
            else:
                comment=("Be sure to take some sunscreen with you!")
        elif (text=="cloudy") and temp<=16 and temp>5:
            choice=randint(1,2)
            if choice==1:
                comment=("Brrr! It might rain, so be sure to take a jacket with you!")
            elif choice==2:
                comment=("Wow, it'll be chilly outside! Maybe you should take an umbrella?")
        elif temp<5:
            comment=("It'll be freezing out there! Wear lots of warm clothes, you'll need them.")
        elif text=="rainy":
            comment=("You might want to take an umbrella with you!")
        fullcomment=fullcomment+". "+comment
        return(fullcomment)





    def outputWeather(forecastedWeather):
        fullcomment=""
        hightemp=forecastedWeather[0]
        lowtemp=forecastedWeather[1]
        text=forecastedWeather[2]
        date=forecastedWeather[3]
        day=forecastedWeather[4]
        nextDay=forecastedWeather[5]
        day=dict3[day]
        if nextDay==False:
            #CHANGE TO SOMETHING THAT MAKES MORE SENSE
            fullcomment="This "+day+", the weather in "+city+" will be "+text.lower()+". The temperature will range from "+lowtemp+" to "+hightemp+" celsius."
            #fullcomment="In "+city+" this "+day+" there will be a high of "+hightemp+", a low of "+lowtemp+" and it will be "+text.lower()+"."
        else:
            fullcomment="Next "+day+" the weather in "+city+" will be "+text.lower()+". The temperature will range from "+lowtemp+" to "+hightemp+" celsius."
        tuple2=(forecastedWeather,fullcomment)
        return(tuple2)


    getTuple=(False, '')
    """
    while getTuple==(False, ''):
        userinput=input("What day would you like to learn about? ")
        getTuple=identifyDay(userinput)
    """
    getTuple=identifyDay(userinput)
    if getTuple==(False, ''):
        getTuple=(False, dayList[0])
    forecastedWeather=forecastWeather(getTuple)
    tuple2=outputWeather(forecastedWeather)
    fullcomment=outputComment(tuple2)
    return fullcomment
