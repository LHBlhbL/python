
from hashlib import new
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}


def novel_request(url,preText,fileName):
    newUrl=url
    novel_text=preText
    pre='下一章'
    while newUrl != "":
        html = requests.get(newUrl, headers=headers).content.decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')
        list1 = soup.find(id='booktxt')
        list2 = list1.find_all('p')
        if pre == '下一章':
            novel_text+=soup.find('h1').text+'\n'
        for item in list2:
            novel_text += item.text+'\n'
        newItem=soup.find(id='next_url')
        new=newItem.get('href')
        newUrl = "https://www.husttest.com"+new
        if newItem.text == '下一页':
            pre='下一页'
            continue
        elif newItem.text == '下一章':
            with open(fileName, 'a', encoding='utf-8')as f:
                f.write(novel_text)
            novel_text=""
            pre='下一章'
        else:
            newUrl=""

    

if __name__ == "__main__":
    pre=""
    url=input("url:")
    fileName=input("fileName:")
    novel_request(url,pre,fileName)