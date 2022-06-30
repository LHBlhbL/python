
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
    while newUrl != "":
        html = requests.get(newUrl, headers=headers).content
        soup = BeautifulSoup(html, 'html.parser')
        novel_text='/n'+soup.find('h1').text+'\n'
        list3=soup.find(name='div',attrs={"class":"bottem2"})
        aList = list3.find_all('a')
        newUrl='http://www.bookrb.com'+aList[3].get('href')
        list1 = soup.find(id='content')
        text=str(list1)
        novel_text+=text.replace('<br/>',"\n").replace('<div id="content">',"").replace("</div>","")
        with open(fileName, 'a', encoding='utf-8')as f:
            f.write(novel_text)
        
        
    

if __name__ == "__main__":
    pre=""
    url=input("url:")
    fileName=input("fileName:")
    novel_request(url,pre,fileName)