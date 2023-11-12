import pyautogui
import pygetwindow as gw
import keyboard
from common import findUser, sendMsg
from daumnews import getNews, makeMsgByNews

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
    '조성걸',
    '박병준',
    '양예성',
    '문주호',
    '노영재',
    '박준현',
    '이슬아',
]

# newsList = getNews()
#
# newsText = makeMsgByNews(newsList)

for user in userList:
    send(user, "방금 보낸 것은 카카오워크 봇이 보낸 메세지입니다. 관심 있으시면 개인적으로 저에게 찾아와주세요")

keyboard.wait('esc')
