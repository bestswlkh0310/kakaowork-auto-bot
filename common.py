import pyautogui
import pyperclip
import time
import keyboard


def findUser(name):
    pyautogui.click(1626, 26)
    pyautogui.click(1626, 26)

    time.sleep(1)
    pyperclip.copy(name)
    time.sleep(0.1)
    keyboard.press_and_release('ctrl+v')


def sendMsg(msg):
    time.sleep(1.6)
    pyautogui.click(779, 162)
    pyautogui.click(779, 162)

    time.sleep(1)
    pyautogui.click(705, 937)
    pyautogui.click(705, 937)
    pyperclip.copy(msg)
    time.sleep(0.1)
    keyboard.press_and_release('ctrl+v')
    time.sleep(0.4)
    pyautogui.click(1876, 979)
    pyautogui.click(1876, 979)
