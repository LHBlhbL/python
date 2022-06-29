from asyncio.windows_events import NULL
from hashlib import new
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}


def novel_request(url,preText):
    newUrl=url
    novel_text=preText
    while newUrl != "":
        html = requests.get(newUrl, headers=headers).content.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        list1 = soup.find(id='booktxt')
        list2 = list1.find_all('p')
        for item in list2:
            novel_text += item.text+'\n'
        newItem=soup.find(id='next_url')
        new=newItem.get('href')
        newUrl = "https://www.husttest.com"+new
        if newItem.text == '下一页':
            continue
        elif newItem.text == '下一章':
            with open('novel3.txt', 'a', encoding='utf-8')as f:
                f.write(novel_text)
            novel_text=""
        else:
            newUrl=""


def main():
    url = 'https://www.husttest.com/xiaoshuo/94361240/'
    html = requests.get(url, headers=headers).content.decode('utf-8')
    section = BeautifulSoup(html, 'html.parser')
    i = 0
    test = section.find(id='list').find_all('a')
    url_list = []
    newUrl="https://www.husttest.com"
    for item in test:
        url=item.get('href')
        url_list.append(newUrl+url)
    print(url_list)
    

if __name__ == "__main__":
    pre=""
    url=input("url:")
    novel_request(url,pre)