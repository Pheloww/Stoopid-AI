import threading
from datetime import datetime
import webbrowser

webbrowser.open("https://www.youtube.com/channel/UC9GRq2DBljL32kaxlb-euBQ?view_as=subscriber")

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
#welcome user
print("Hello im Stoopid")
name = input("what is your name: ")
print("Welcome " + name + " to Stoopid AI")

if name == "godmode":
    webbrowser.open("https://www.twitch.tv/mrbeen34")
    while name == "godmode":
        print("Folllow")
#make password
password = input ("Make a password: ")
print("Your Password is " + password)


#make sure it is him
reasure = input("please input your password again " + name + " ")

if reasure != password:
    while reasure != password:
        reasure = input("please input your password ")

print("Hello " + name + " and welcome to Stoopid AI")

print("i can, Tell the Time, Secret, YouTube")

select = input("what would you like to do i can :")

if select == "time":
    print(current_time)

elif select == "secret":
    webbrowser.open("https://www.youtube.com/watch?v=oHg5SJYRHA0")
    while select == "secret":
        print("GOTEEM")

elif select == "youtube":
    webbrowser.open("https://www.youtube.com/watch?v=z4CUHQXCSaQ")
    while select == "youtube":
        print("I HAVE STROKE")