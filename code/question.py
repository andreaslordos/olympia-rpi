def answer(userinput):
    from urllib import request
    def getSpoken(app_id,query):
        url="http://api.wolframalpha.com/v1/spoken?appid="+app_id+"&i="+query
        url='+'.join(url.split())
        html=request.urlopen(url)
        contents=html.read()
        contents=contents.decode('utf-8')
        return contents
    
    def cleanUp(answer):
        for x in range(len(answer)):
            if answer[x]=="\n":
                answer=answer[0:x]+" "+answer[x+1:]
                return answer
        return answer
    
    try:
        app_id= GET_YOUR_OWN_APP_ID_AT_https://developer.wolframalpha.com
        answer=getSpoken(app_id,userinput.lower())
        return answer
    except:
        return "Sorry, I don't know."
