def wordStuff(userinput):
    from PyDictionary import PyDictionary as pd
    '''
    Input: userinput, string
    Output: depends on what the user is trying to do, string

    Explanation:
    Figures out what the user wants to do (define, find a synonym, spell a word)
    using the function taskToDo. After parsing the input to separate the word,
    it then goes on to perform a function according to the task that the user
    specified. It uses the PyDictionary library for definitions, synonyms and
    translations, while a simple 'for' loop is used for spelling a word.
    '''
    def taskToDo(raw_input):
        raw_input=raw_input.lower()
        if "synonym" in raw_input:
            return "syn"
        elif "define" in raw_input or "definition" in raw_input:
            return "def"
        elif "translate" in raw_input or "translation" in raw_input:
            return "tra"
        elif "spell" in raw_input or "spelled" in raw_input or "spelt" in raw_input:
            return "spe"
        return "wtf"



    def parseInput(rawinput):
        if rawinput.split()[-1].lower()=="please":
            word=rawinput.split()[-2]
        else:
            word=rawinput.split()[-1]
        return word

    def defineWord(word):
        if "a" in userinput.split():
            types=["Noun","Adjective","Pronoun"]
        else:
            types=["Adjective","Noun","Pronoun"]
        dictionary=pd(word)
        meanings=dictionary.getMeanings()
        definition=None
        x=0
        while definition==None:
            definition=meanings[word].get(types[x])
            if definition!=None:
                definition=definition[0]
                break
            x+=1
            if x==3:
                break
        definition=word + ": "+definition
        return definition

    def synonWord(word):
        dictionary=pd(word)
        syn_list=dictionary.getSynonyms()[0][word]
        fullstr="Synonyms for "+word+" include "
        for y in range(len(syn_list)-1):
            fullstr+=syn_list[y]+", "
        fullstr+="and "+syn_list[-1]
        return fullstr

    def spellWord(word):
        fullstr=""
        for letter in word:
            fullstr+=letter+", "
        return fullstr

    def transWord(word):
        return "To be added"

    task=taskToDo(userinput)
    if task!="wtf":
        word=parseInput(userinput)
        if task=="def":
            return defineWord(word)
        elif task=="syn":
            return synonWord(word)
        elif task=="tra":
            return transWord(word)
        elif task=="spe":
            return spellWord(word)
