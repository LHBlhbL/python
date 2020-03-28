import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import time


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}


def novel_request(url):
    html = requests.get(url, headers=headers).content.decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    novel_text = soup.find('h1').text+'\n'
    list1 = soup.find(id='content')
    list2 = list1.find_all('p')
    for item in list2:
        novel_text += item.text+'\n'
    with open('novel.txt', 'a', encoding='utf-8')as f:
        f.write(novel_text)


def main(page):
    url = 'http://www.paoshu8.com/1_1010/'
    html = requests.get(url, headers=headers).content.decode('utf-8')
    section = BeautifulSoup(html, 'lxml')
    i = 0
    test = section.find(id='list').find_all('a')
    for item in test:
        i += 1
        if(item.text[:3] == '第一章'):
            break
    del test[0:i-1]
    i = 0
    newurl = 'http://www.paoshu8.com'
    url_list = []
    for item in test:
        url_list.append(newurl+item.get('href'))
        i += 1
        if(i == page):
            break
    return url_list


if __name__ == "__main__":
    url_list = main(20)
    pool = Pool(4)
    pool.map(novel_request, url_list)
    pool.close()
    pool.join()
