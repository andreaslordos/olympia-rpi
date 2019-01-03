from os import getcwd
from sys import platform
from os import system
import requests

operating_system=platform
dir=getcwd()

url='http://ipinfo.io/json'
response=requests.get(url)
js=response.json()
city=js['city']

if "linux" in operating_system or operating_system=="Darwin":
    f1=open("code/dir.txt","w")
    f2=open("resources/dir.txt", "w")
    f4=open("resources/location.txt","w")
    f5=open("resources/reminders.txt","w")
elif operating_system[0:3]=="win":
    f1=open("code\\dir.txt","w")
    f2=open("resources\\dir.txt", "w")
    f4=open("resources\\location.txt","w")
    f5=open("resources\\reminders.txt","w")

f1.write(dir)
f2.write(dir)
f4.write(city)
f5.close()
f4.close()
f2.close()
f1.close()

print("Setup complete.")
