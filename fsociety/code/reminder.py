'''
Used to set alarms or timers. Appends the reminder.txt file with the date of the alarm/timer and then starts up alarmclock.py so that
it stays updated
'''
from changeDir import changeDirectory as cd
def setAlarm(when):
    import datetime
    from time import sleep
    cd("resources")

    months={"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,"August":8,"September":9,"October":10,"November":11,"December":12}

    def removeAlarm():
        #beta, still not operational
        try:
            f=open("reminders.txt","r")
        except:
            return("FNF error")
        contents=f.read()
        f.close()
        contents.split("#")[:-1]
        contents.pop(-1)
        f=open("reminders.txt","w")
        f.write(' '.join(contents)+"#")
        f.close()
    
    def isInt(numb):
        try:
            int(numb)
            return True
        except:
            return False
    
    
    def timerOrReminder(in1):
        for key in months:
            if key in in1:
                return "reminder"
        if "remove" in in1:
            return 'remove'
        return "timer"
    '''
    def timeUntil(alarmDate):
        now=datetime.datetime.now()
        return alarmDate-now
        
    def convertToSeconds(dateTimeObject):
        return dateTimeObject.total_seconds()

    def alarm(seconds):
        sleep(seconds)
    '''
    
    def parseAlarm(alarm):
        now=datetime.datetime.now()
        strToInt={"one":1,"two":2,"three":3,"four":4}
        hours1=0
        minutes1=0
        seconds1=0
        alarm=alarm.split()
        for x in range(len(alarm)):
            if alarm[x]=="hour" or alarm[x]=="hours" and x!=0:
                hours1=alarm[x-1]
            if alarm[x]=="minutes" or alarm[x]=="minute" and x!=0:
                minutes1=alarm[x-1]
            if alarm[x]=="seconds" or alarm[x]=="second" and x!=0:
                seconds1=alarm[x-1]
        for key in strToInt:
            if key==seconds1:
                seconds1=strToInt[key]
            if key==hours1:
                hours1=strToInt[key]
            if key==minutes1:
                minutes1=strToInt[key]
        minutes1=int(minutes1)
        hours1=int(hours1)
        seconds1=int(seconds1)
        alarmTime=now+datetime.timedelta(hours=hours1,minutes=minutes1,seconds=seconds1)
        return alarmTime

    def parseReminder(reminder):
        postfix=["st","nd","rd","th"]
        potentialDays=[]
        now=datetime.datetime.now()
        month="0"
        day="0"
        reminder=reminder.split()
        for key in months:
            if key in reminder:
                month=months[key]
        if month=="":
            month=now.month
        for word in reminder:
            if word[-2:] in postfix:
                potentialDays.append(word)
        if len(potentialDays)==1:
            if isInt(potentialDays[0][:-2])==True:
                day=potentialDays[0][:-2]
        elif len(potentialDays)==0:
            day=now.day
        else:
            for numb in potentialDays:
                if isInt(numb)==True:
                    day=numb
                    break
        am=False
        for x in range(len(reminder)):
            if reminder[x]=="a.m.":
                time=reminder[x-1]
                am=True
            if reminder[x]=="p.m.":
                time=reminder[x-1]
        time=time.split(":")
        hour=time[0]
        minute=time[1]
        if am==False and hour!="12":
            hour=int(hour)
            hour+=12
        if am==True and hour=="12":
            hour=0
        day=int(day)
        month=int(month)
        hour=int(hour)
        minute=int(minute)
        if month<now.month:
            year=now.year+1
        else:
            year=now.year
        year=int(year)
            
        alarmTime=datetime.datetime(year,month,day,hour,minute)
        
        return alarmTime
         

    typeOf=timerOrReminder(when)
    if typeOf=="timer":
        playTime=parseAlarm(when)
    elif typeOf=='remove':
        removeAlarm()
    else:
        playTime=parseReminder(when)

    realPlayTime=datetime.datetime(playTime.year,playTime.month,playTime.day,playTime.hour,playTime.minute,0)

    try:
        f=open("reminders.txt","a")
    except:
        f=open("reminders.txt","w")
    f.write(str(playTime)+"#")
    f.close()
    cd("code")

    return realPlayTime
