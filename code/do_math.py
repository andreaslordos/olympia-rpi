def calculate(userinput):
    from num2words import num2words
    '''
    Input: userinput, string
    Output: total, string

    Explanation:
    First, this module decides which mathematical operation the user is requesting. It does this by
    searching for keywords in decideOperation(). It then singles out the numbers using a combination
    of the function numberParser and isInt, and adds all the numbers it finds in a list. After that,
    it performs the mathematical calculation, rounds it up to 5 decimal places, converts it to a string
    and returns it to the calling function.

    '''
    def decideOperation():
        if " + " in userinput:
            return "add"
        elif " - " in userinput:
            return "min"
        elif " x " in userinput:
            return "mul"
        elif " ^ " in userinput:
            return "pow"
        elif "divide" in userinput:
            return "div"
        elif "factorial" in userinput:
            return "fac"
        elif "squared" in userinput:
            return "squ"
        elif "cubed" in userinput:
            return "cub"
        elif "square root" in userinput:
            return "squrt"
        elif "cube root" in userinput:
            return "cubrt"
        else:
            return "err"

    def isInt(number):
        try:
            int(number)
            return True
        except ValueError:
            try:
                float(number)
                return True
            except ValueError:
                return False

    def numberParser():
        numbers=[]
        for x in range(len(userinput.split())):
            if isInt(userinput.split()[x])==True:
                try:
                    numbers.append(int(userinput.split()[x]))
                except ValueError:
                    numbers.append(float(userinput.split()[x]))
        return numbers

    operation=decideOperation()
    numbers=numberParser()
    total=0
    if len(numbers)>=2:
        if operation=="add":
            total=sum(numbers)
        elif operation=="min":
            total=numbers[0]
            for x in range(len(numbers)-1):
                total-=numbers[x+1]
        elif operation=="mul":
            total=numbers[0]
            for x in range(len(numbers)-1):
                total*=numbers[x+1]
        elif operation=="pow":
            total=numbers[0]**numbers[-1]
        elif operation=="div":
            total=numbers[0]
            for x in range(len(numbers)-1):
                total=total/numbers[x+1]
        else:
            return "Error"
    elif len(numbers)==1:
        if operation=="fac":
            from math import factorial
            total=factorial(numbers[0])
        elif operation=="squ":
            total=numbers[0]**2
        elif operation=="cub":
            total=numbers[0]**3
        elif operation=="squrt":
            from math import sqrt
            total=sqrt(numbers[0])
        elif operation=="cubrt":
            total=round(int((numbers[0]**(1/3))*1000000000+1)/1000000000,5)
        else:
            return "Error"
    return num2words(round(total,5))
