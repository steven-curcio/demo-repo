import pyautogui
import time
import sys
from datetime import datetime
pyautogui.FAILSAFE = False
numMin = None

if ((len(sys.argv)<2) or sys.argv[1].isalpha() or int(sys.argv[1])<1):
    numMin = int(input("Enter the time interval you want this program to run: "))
else:
    numMin = int(sys.argv[1])

print(f"Staring automouse now. This program will run every {numMin} minute(s). ")

while(True):
    x=0
    while(x<numMin):
        time.sleep(60)
        x+=1
    for i in range(0,200):
        pyautogui.moveTo(0,i*4)
    pyautogui.moveTo(1,1)
    for i in range(0,3):
        pyautogui.press("shift")
    
    print("Movement made at {}".format(datetime.now().time()))


## https://github.com/Johnson468/Stay-Awake ##