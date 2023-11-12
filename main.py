import pyautogui
import pygetwindow as gw
import keyboard
from common import findUser, sendMsg

window = gw.getWindowsWithTitle("카카오워크")[0]
window.activate()
window.maximize()


# 좌표 출력
def performCapturePos():
    print(pyautogui.position())


keyboard.add_hotkey('C', performCapturePos)


# 메세지 보내기
def send(name, *msgs):
    findUser(name)

    for msg in msgs:
        sendMsg(msg)


send('박병준', '니얼굴', '아잉', '아잉')

keyboard.wait('esc')
