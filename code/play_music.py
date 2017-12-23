def playMusic(userinput, choiceIsPure):
    '''
    Input: userinput, string /// choiceIsPure, boolean
    Output: p, class

    Explanation:
    Streams audio from a youtube video, essentially acting as a music player.
    The first thing this does is seperate the query from userinput - e.g, if the
    user said 'Play Happy by Bruno Mars', it should get recognize 'Happy by Bruno
    Mars' as the query. It does this by looking for triggerwords (e.g play) and
    seperating the triggerwords from userinput. After it separates the query, it
    uses the youSearch function to load a list of the URLs of the twenty most
    relevant YouTube videos. It then uses loadMusic to load the song on VLC,
    and returns the class that allows you to control the music back to main.py



    '''
    import pafy
    import vlc
    import lxml.html
    import requests as rq
    from output_voice import voiceOutput

    def youSearch(textToSearch):
        html=rq.get('https://www.youtube.com/results?search_query='+textToSearch).text
        tree=lxml.html.fromstring(html)
        tree.make_links_absolute('https://www.youtube.com')
        links=tree.cssselect('.yt-uix-tile-link')
        return [l.attrib['href'] for l in links]

    def loadMusic(url):
        #loads the music onto VLC, and returns "p" (the track), so that it can be played in the calling program
        song=pafy.new(url)
        try:
            voiceOutput(["Now playing: "+song.title])
        except:
            pass
        audiostreams=song.audiostreams
        playthis=audiostreams[-1]
        i = vlc.Instance('--verbose 2'.split())
        p = i.media_player_new()
        p.set_mrl(playthis.url)
        return p

    def getCorrectLink(urls):
        pafy.set_api_key('AIzaSyDvf2A3-ZDoQciNhgxdbEO2NIaQyCYY33A')
        for url in urls:
            if len(url)==43 and url[:32]=='https://www.youtube.com/watch?v=':
                song=pafy.new(url[32:])
                return url
                '''
                print(song.keywords)
                if 'Music' in song.keywords:
                    print("Music in keywords!")
                    return url
                '''
                #keywords doesn't work anymore, wtf????

    #Main Program
    pafy.set_api_key('AIzaSyDvf2A3-ZDoQciNhgxdbEO2NIaQyCYY33A')
    if choiceIsPure==False:
        triggerword=["play","on"]
        if "that goes like" in userinput.lower() or "that goes" in userinput.lower() or "lyrics" in userinput.lower():
            if "that goes like" in userinput:
                triggerword=["like"]
            elif "that goes" in userinput:
                triggerword=["goes"]
            else:
                triggerword=["lyrics"]
        userinput=userinput.split()
        for x in range(len(userinput)):
            if userinput[x].lower() in triggerword:
                break
        userinput=" ".join(userinput[x+1:])
    urls=youSearch(userinput)
    shouldbreak=False
    counter=0
    if userinput!="":
        urlToUse=getCorrectLink(urls)
        p=loadMusic(urlToUse)
        p.play()
        return p
