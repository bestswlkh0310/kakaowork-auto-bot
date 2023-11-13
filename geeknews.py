import requests
from bs4 import BeautifulSoup


def getGeekNews():
    result = []
    for i in range(1, 51):
        response = requests.get(f'https://news.hada.io/new?page={i}')
        soup = BeautifulSoup(response.text, 'html.parser')

        topics = soup.find_all('div', 'topics')[0].find_all('div', 'topic_row')
        if len(topics) == 0:
            break
        for topic in topics:
            title = topic.find_all('div', 'topictitle')[0].text
            # description = topic.find_all('div', 'topicdesc')[0].find_all('a')[0].text
            url = topic.find_all('a')[1]['href']
            result.append((title, url))
    return result


def makeGeekNews(news):
    result = ":: Geek 뉴스\n"
    for (idx, n) in enumerate(news):
        result += f"{idx + 1}. {n[0]}\n"
        result += f"바로가기 - {n[1]}\n\n"
    return result
