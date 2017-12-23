def getNews(userinput):
    '''
    Input: userinput, string
    Output: newsTuple, tuple

    Explanation:
    Uses the RSS feeds of various news sites to form a tuple (newsTuple) which
    contains three headlines. The user may specify a news source in userinput,
    and if he does, the source variable changes to match their request. Otherwise,
    the BBC RSS feed is used.
    '''

    from feedparser import parse

    source="http://feeds.bbci.co.uk/news/world/rss.xml" #BBC, DEFAULT SOURCE

    if "cnn" in userinput.lower():
        source="http://rss.cnn.com/rss/edition_world.rss"
    elif "fox" in userinput.lower():
        source="http://feeds.foxnews.com/foxnews/latest"
    elif "economist" in userinput.lower():
        source="http://www.economist.com/sections/international/rss.xml"
    elif "huffington" in userinput.lower():
        source="http://www.huffingtonpost.com/section/politics/feed"
    elif "new york times" in userinput.lower():
        source="http://rss.nytimes.com/services/xml/rss/nyt/World.xml"
    elif "washington post" in userinput.lower():
        source="http://feeds.washingtonpost.com/rss/rss_blogpost"


    feed=parse(source)
    newsTuple=(str(feed['entries'][0]['title']),str(feed['entries'][1]['title']),str(feed['entries'][2]['title']))
    return newsTuple
