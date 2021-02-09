import pyautogui
import win32clipboard
import time
import mysql.connector
from termcolor import colored, cprint

mydb = mysql.connector.connect(
    host="HOST",
        database="DATABASE",
        user="USER",
        password="PASSWORD"
)

mycursor = mydb.cursor()

def SelectCode():
    global k
    print(k)



# x-axis -- COMMON Y = 525
#        -- x DIFF = 198 (-1085 to -292)

#251 , 335, 417, 506, 586, 673
def menudrive():
    global k
    #print(pyautogui.position())
    for i in range(251, 678, 85):
        for j in range(-1085, -292, 198):
            k = k + 1
            if k <= 100:
                pyautogui.click(j, i)
                time.sleep(1)
                SelectCode()
            pyautogui.click(-623, 64)
k = 0
for menu in range(4):
    time.sleep(0.5)
    menudrive()
    #pyautogui.click(-1262, 307)
    pyautogui.keyDown('pagedown')
#print(pyautogui.position())
#SelectCode()