def changeDirectory(folder):
    from os import chdir
    from sys import platform
    
    operating_system=platform
    try:
        dirFile=open("dir.txt","r")
        directory=dirFile.read()
        dirFile.close()
    except:
        from os import getcwd
        currentDir=getcwd()
        print("Error: dir.txt not found. Should be in code directory, but instead I am in "+currentDir)
    try:
        if operating_system[0:3]=="win":
            chdir(directory+"\\"+folder)
        else:
            chdir(directory+"/"+folder)
        return True
    except:
        return False
