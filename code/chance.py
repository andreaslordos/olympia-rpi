'''
Input: userinput
Output: heads/tails/you rolled a [number]
'''
def Chance(userinput):
    from random import randint
    if "coin" in userinput.lower():
        number=randint(1,2)
        if number==1:
            return "heads"
        else:
            return "tails"
    else: #roll a die feature
        userinput=userinput.split()
        for word in userinput:
            if word[0].lower()=="d":
                try:
                    roll=str(randint(1,int(word[1:])))
                    return "You rolled a "+roll
                except:
                    pass
        return "Error"
        
        
