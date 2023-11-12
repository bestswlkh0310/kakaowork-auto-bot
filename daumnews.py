from selenium import webdriver
import time
from bs4 import BeautifulSoup


def getNews():
    driver = webdriver.Chrome()

    driver.get('https://news.daum.net/digital/#1')

    time.sleep(1)
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    lst = soup.find(class_='list_realtime').find_all('li')

    result = []

    for i in lst:
        a = i.find('a')
        title = a.text
        url = a['href']
        print(title, url)
        result.append((title, url))
    return result


def makeMsgByNews(news):
    result = ""
    for (idx, n) in enumerate(news):
        result += f"{idx + 1}. {n[0]}\n"
        result += f"바로가기 - {n[1]}\n\n"
    return result
