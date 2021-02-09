import pyautogui
import win32clipboard
import time
import mysql.connector
from termcolor import colored
import pyttsx3

def Talk(speech):
    engine = pyttsx3.init()
    voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice',voice)
    engine.say(speech)
    engine.runAndWait()


mydb = mysql.connector.connect(
    host="HOST",
        database="DATABASE",
        user="USER",
        password="PASSWORD"
)

mycursor = mydb.cursor()
def SelectCode():
    global k
    #SELECT
    Talk("Checking Code Compatibility...")
    print("SELECTING CODE...")
    #-682, 320
    #-763, 249 to -756, 656
    pyautogui.click(-763, 249, button='left')
    time.sleep(1)
    pyautogui.hotkey("ctrl","a")
    pyautogui.hotkey("ctrl","c")
    time.sleep(0.1)
    print("Started Copying")
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    #print(data)

    print("Copied to Clipboard")
    print("Processing ...")
    data = list(data.split("\r\n"))
    SESSION_temp = data[2]
    SESSION_temp = list(SESSION_temp.split(' '))
    SESSION = ""
    for sess in SESSION_temp:
        if sess != 'SESSION:':
            SESSION = SESSION + sess + " "
    NAME = data[4]
    code = ""
    question = ""
    testcase = []
    temp = []
    mainTestCase = []
    for dat in data:
        if dat != "":
            temp.append(dat)

    if '#include <stdio.h>' in temp:
        Talk("Starting Code Transfer...")
        codeS = temp.index('#include <stdio.h>')
        for codeI in range(codeS,len(temp)):
            code = code + temp[codeI] + '\r\n'

        if 'QUESTION DESCRIPTION' in temp:
            QUESTIONS = temp.index('QUESTION DESCRIPTION')
            QUESTIONE = temp.index('TEST CASE 1')
            for QI in range(QUESTIONS+1, QUESTIONE):
                question = question + temp[QI] + '<br>'

        testmain = []
        for testdata in range(QUESTIONE,codeS):
            testmain.append(temp[testdata])

        testD = ""
        testS = testmain.index('INPUT') + 1
        testE = testmain.index('OUTPUT')
        for io in range(testS, testE):
            testD = testD + testmain[io] + "<br>"

        testcase.append(k)
        testcase.append("TEST CASE 1")
        testcase.append(testD)
        testD = ""
        testS = testmain.index('OUTPUT') + 1
        if 'TEST CASE 2' in testmain:
            testE = testmain.index('TEST CASE 2')
        else:
            testE = len(testmain)
        for io in range(testS, testE):
            testD = testD + testmain[io] + "<br>"

        testcase.append(testD)
        mainTestCase.append(testcase)

        if testE != len(testmain):
            testcase = []
            testD = ""
            testS = testmain.index('INPUT', testE) + 1
            testE = testmain.index('OUTPUT', testE)
            for io in range(testS, testE):
                testD = testD + testmain[io] + "<br>"

            testcase.append(k)
            testcase.append("TEST CASE 2")
            testcase.append(testD)
            testD = ""
            testS = testmain.index('OUTPUT', testE) + 1
            if 'TEST CASE 3' in testmain:
                testE = testmain.index('TEST CASE 3')
            else:
                testE = len(testmain)
            for io in range(testS, testE):
                testD = testD + testmain[io] + "<br>"

            testcase.append(testD)
            mainTestCase.append(testcase)

        if testE != len(testmain):
            testcase = []
            testD = ""
            testS = testmain.index('INPUT', testE) + 1
            testE = testmain.index('OUTPUT', testE)
            for io in range(testS, testE):
                testD = testD + testmain[io] + "<br>"

            testcase.append(k)
            testcase.append("TEST CASE 3")
            testcase.append(testD)
            testD = ""
            testS = testmain.index('OUTPUT', testE) + 1
            if 'TEST CASE 4' in testmain:
                testE = testmain.index('TEST CASE 4')
            else:
                testE = len(testmain)
            for io in range(testS, testE):
                testD = testD + testmain[io] + "<br>"

            testcase.append(testD)
            mainTestCase.append(testcase)

        #print(k)
        print("Code Processed !!")
        print("Writing to disc...")
        sqlformula1 = "INSERT INTO elabdata (id, SESSION, QUESTION_NO, QUESTION_NAME, QUESTION_DESC, CODE)" \
                      " VALUES (%s, %s, %s, %s, %s, %s)"
        val = (k,SESSION,"Q. "+str(k)+":", NAME,question, code)
        mycursor.execute(sqlformula1,val)

        sqlformula2 = "INSERT INTO elabtestcase (dataid, TESTCASE_NO, INPUT, OUTPUT) VALUES (%s, %s, %s, %s)"
        mycursor.executemany(sqlformula2, mainTestCase)

        mydb.commit()
        print("Data Transferred!!")
        Talk("Code Successfully Transfered.")
        print("Completed - "+str(k))
        Talk("Completed Question "+str(k))

    else:
        err = colored('Error : ', 'red')
        text = colored('stdio headerfile is missing...', 'green')
        print(err + text)
        Talk(err + text)



# x-axis -- COMMON Y = 525
#        -- x DIFF = 198 (-1085 to -292)

#251 , 335, 417, 506, 586, 673
def menudrive():
    global k
    #print(pyautogui.position())
    for i in range(251, 678, 85):
        for j in range(-1085, -292, 198):
            k = k + 1
            if k <= 200:
                Talk("Starting Question "+str(k))
                pyautogui.click(j, i)
                time.sleep(3)
                SelectCode()
                time.sleep(1)
            pyautogui.click(-623, 64)


k = 100
for menu in range(4):
    time.sleep(0.5)
    menudrive()#620,51
    #pyautogui.click(-1262, 307)
    pyautogui.keyDown('pagedown')
#print(pyautogui.position())
#pyautogui.click(-623, 64)
#SelectCode()