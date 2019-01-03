def answer(userinput):
    from urllib import request
    def getSpoken(app_id,query):
        url="http://api.wolframalpha.com/v1/spoken?appid="+app_id+"&i="+query
        url='+'.join(url.split())
        html=request.urlopen(url)
        contents=html.read()
        contents=contents.decode('utf-8')
        return contents
    
    try:
        app_id= None #need to insert app id
        answer=getSpoken(app_id,userinput.lower())
        return answer
    except:
        if app_id==None:
            return "For this to work, you must input an app_id in the python file question"
        else:
            return "Sorry, I don't know."
