from os import getcwd
from sys import platform
from os import system

operating_system=platform
dir=getcwd()

if "linux" in operating_system or operating_system=="Darwin":
    f1=open("code/dir.txt","w")
    f2=open("resources/dir.txt", "w")
elif operating_system[0:3]=="win":
    f1=open("code\\dir.txt","w")
    f2=open("resources\\dir.txt", "w")
    
f1.write(dir)
f2.write(dir)
f2.close()
f1.close()

print("Setup complete.")
