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
                for x in range(100001):
                    if "d"+str(x) in word.lower():
                        dice=userinput[-1]
                        dice=dice[1:]
                        number=str(randint(1,int(dice)))
                        fullstr="You rolled a "+number
                        return fullstr
        return "Error"
        
        
