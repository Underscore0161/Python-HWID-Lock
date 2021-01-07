import subprocess
import requests
import time
import sys
import os

def printSlow(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(.1)
printSlow("Please Wait...")

hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
r = requests.get("https://pastebin.com/raw/h8Dm8HVk") # YOUR RAW PASTEBIN LINK



print("")
def Main_Program():
    if hwid in r.text:
        printSlow("Access granted. Hello!") #ACCESS GRANTED HWID IN DATABASE
        time.sleep(.1)
    else:
        print("HWID Not In Database!")
        print("Message (______) for help. Your HWID: " + hwid) #Prints HWID
        time.sleep(5)
        sys.exit()

if __name__ == "__main__":
    Main_Program()