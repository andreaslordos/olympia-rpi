def wikipedia(userinput,sentenceNo):
    '''
    Inputs: userinput, string
    Outputs: result, string /// search, string

    Explanation:
    Uses the wikipedia module to search up a query and return it to main
    The reason we return the query is so that we can use the tellMeMore
    function which gives the first 3 sentences rather than the first one
    only.
    '''
    import wikipedia
    userinput=userinput.split()
    search=""
    result=""
    if "what is " in ' '.join(userinput).lower():
        search=userinput[2:]
    else:
        search=userinput[1:]
    search=' '.join(search)
    result=wikipedia.summary(search,sentences=int(sentenceNo))
    return (result,search)
