def determine(userinput):
    '''
    Input: userinput, string
    Output: moduleToRun, string
    userinput = What the user said
    moduleToRun = What module the user requested

    Explanation:
        Firstly, the module figures out which modules the user *possibly* requested using the whichModule function.
        The whichModule function looks for keywords which relate to different modules (e.g play might possibly mean
        playing some music). It then adds all possible modules in a list (functionToRun). If there's more than one
        possible module, the list is passed to conflictResolution, which sorts out conflicts using a point-based
        system. The module with the highest score (e.g 'music' has a score of 5, which is the highest) will be the one
        passed back to main.py
    '''
    def conflictResolution(conflicts):
        conflict_dict={"alarm":3,"wolfram":2,"weather":4,"music":5,"help":1,"news":3,"bohemian":4,"drumpf":4,"alarm":3,"wiki":3,"dict":4,"xkcd":4,"math":5,"tellMeMore":2,"chance":3}
        winner=conflicts[0]
        conflicts.remove(winner)
        for task in conflicts:
            if conflict_dict.get(task)>conflict_dict.get(winner):
                winner=task
        return [winner]


    def whichModule(userinput):
        def aboutWeather(userinput):
                if "weather" in userinput or "hot" in userinput or "cold" in userinput or "warm" in userinput:
                    return "weather"
                return

        def aboutMusic(userinput):
            userinput=userinput.lower()
            if "music" in userinput or "put on" in userinput or "song" in userinput or "play" in userinput or "lyrics" in userinput or "which goes like" in userinput:
                return "music"
            return

        def aboutHelp(userinput):
            if "help" in userinput or "settings" in userinput:
                return "help"
            return

        def aboutNews(userinput):
            if "news" in userinput or "headlines" in userinput:
                return "news"
            return

        def aboutBohemian(userinput):
            if userinput.lower()=="i see a little silhouetto of a man" or userinput.lower()=="thunderbolt and lightning very very frightening":
                return "bohemian"
            return

        def aboutDrumpf(userinput):
            if userinput.lower()=="who is donald trump" or userinput.lower()=="what is donald trump":
                return "drumpf"
            return

        def aboutAlarm(userinput):
            if "set an alarm" in userinput.lower() or "remind me" in userinput.lower():
                return "alarm"
            return

        def aboutWikipedia(userinput):
            if "wikipedia" in userinput.lower() or "what is " in userinput.lower() or "what's " in userinput.lower():
                return "wiki"
            return

        def aboutDictionary(userinput):
            userinput=userinput.lower()
            if "synonym" in userinput or "definition" in userinput or "spell" in userinput or "spelled" in userinput or "spelt" in userinput or "define" in userinput:
                return "dict"
            return

        def aboutXKCD(userinput):
            if "xkcd" in userinput.lower():
                return "xkcd"
            return

        def aboutMath(userinput):
            #make calculate turn this function into high priority
            mathoperators=["+","-","x","^"]
            operatorPresent=False
            for operator in mathoperators:
                if operator in userinput.split():
                    operatorPresent=True

            if operatorPresent==True:
                return "math"
            elif "divided by" in userinput or "square root" in userinput or "squared" in userinput or "cubed" in userinput or "factorial" in userinput or "cube root" in userinput:
                return "math"
            return

        def aboutTellMeMore(userinput):
            if "tell me more" in userinput.lower():
                return "tellMeMore"
            return

        def aboutQuestions(userinput):
            if "a question" in userinput.lower():
                return "wolfram"
            return

        def aboutDice(userinput):
            dice=False
            for x in range(100001):
                if "d"+str(x) in userinput.lower():
                    dice=True
            if (dice==True and "roll" in userinput.lower()) or "flip a coin" in userinput.lower():
                return "chance"
            return

        def aboutAlarm(userinput):
            u=userinput.lower()
            keywords=["alarm","reminder","remind","set a reminder","set an alarm","timer"]
            for word in keywords:
                if word in u:
                    return "alarm"
            return
        modules=["Weather","Music","News","Help","Bohemian","Drumpf","Alarm","Wikipedia","Dictionary","XKCD","Math","TellMeMore","Questions","Dice","Alarm"]
        modulesToRun=[]
        for module in modules:
            eval("modulesToRun.append(about"+module+"(userinput))")
        while True:
            if None in modulesToRun:
                modulesToRun.remove(None)
            else:
                break
        return modulesToRun
    functionToRun=whichModule(userinput)
    if functionToRun==[]:
        return "ERR"
    elif len(functionToRun)>1:
        functionToRun=conflictResolution(functionToRun)
    else:
        return functionToRun[0]
    return functionToRun[0]
