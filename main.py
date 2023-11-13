import pyautogui
import pygetwindow as gw
import keyboard
from common import findUser, sendMsg
from daumnews import getDaumNews, makeDaumNewsMsg
from geeknews import getGeekNews, makeGeekNews

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


userList = [
    '권예림',
    '신민호',
    '김가영',
    '임규연',
    '이슬아',
    '이진식',
    '김명준',
    '박병준',
    '권지용',
    '민하윤'
]

testUserList = [
    '이강현',
    # '제민국',
    # '노영재',
    # '김동찬'
]

newsList = getDaumNews()
newsText = makeDaumNewsMsg(newsList)

for user in userList:
    send(user, newsText)

newsList = getGeekNews()
newsText = makeGeekNews(newsList)

for user in userList:
    send(user, newsText)

keyboard.wait('esc')
