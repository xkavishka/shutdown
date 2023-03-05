import os

action = input("Input 'S' put the computer to sleep or Use 'D' to shut it down")

if action.lower() == "s":
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
elif action.lower() == "d":
    os.system("shutdown /s /t 0")
else:
    print("Invalid option selected.")
