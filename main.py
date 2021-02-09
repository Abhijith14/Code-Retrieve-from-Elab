import pyautogui
import win32clipboard
import time
import mysql.connector

mydb = mysql.connector.connect(
    host="HOST",
        database="DATABASE",
        user="USER",
        password="PASSWORD"
)

mycursor = mydb.cursor()

#print(pyautogui.position())

def SelectCode():
    #SELECT
    print("SELECTING CODE...")
    #-682, 320
    #-763, 249 to -756, 656
    pyautogui.click(-763, 249, button='left')
    time.sleep(0.1)
    for i in range(20):
        pyautogui.keyDown('pagedown')
    pyautogui.keyUp('pagedown')
    pyautogui.keyDown('shift')
    pyautogui.click(-500, 656, button='left')
    pyautogui.keyUp('shift')
    print("Started Copying")
    time.sleep(0.1)
    pyautogui.hotkey("ctrl","a")
    pyautogui.hotkey("ctrl","c")
    time.sleep(0.1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    print(data)

    print("Copied to Clipboard")
    print("Writing to disc...")
    #sqlformula1 = "INSERT INTO elabdata (id, CODE) VALUES (%s, %s)"
    #val = (1, data)
    #mycursor.execute(sqlformula1,val)
    #mydb.commit()
    print("Data Transferred!!")
    print(pyautogui.position())
SelectCode()

