import pyautogui
import pyperclip
import time
import keyboard

def findUser(name):
    pyautogui.click(1626, 26)

    time.sleep(0.3)
    pyperclip.copy(name)
    keyboard.press_and_release('ctrl+v')


def sendMsg(msg):
    time.sleep(0.3)
    pyautogui.click(779, 162)
    pyautogui.click(779, 162)

    time.sleep(0.5)
    pyautogui.click(705, 937)
    pyperclip.copy(msg)
    keyboard.press_and_release('ctrl+v')
    pyautogui.click(1876, 979)
