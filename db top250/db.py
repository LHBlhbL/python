import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import csv


def request_doban(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def save_movie(soup):
    list = soup.find(class_='grid_view').find_all('li')
    item_list = []
    for item in list:
        item_chart = item.find('em').string
        item_name = item.find(class_='title').text
        item_score = item.find(class_='rating_num').string
        if(item.find(class_='inq')):
            item_quote = item.find(class_='inq').text
        else:
            item_quote = "  "

        item_dict = {
            'movice_chart': item_chart,
            'movice_name': item_name,
            'movice_score': item_score,
            'movice_quote': item_quote
        }
        item_list.append(item_dict)

    with open('movice.csv', 'a', encoding='utf-8')as f:
        write = csv.DictWriter(f, fieldnames=['movice_chart',
                                              'movice_name',
                                              'movice_score',
                                              'movice_quote'])
        write.writerows(item_list)


def main(url):
    html = request_doban(url)
    soup = BeautifulSoup(html, 'lxml')
    save_movie(soup)


if __name__ == "__main__":
    url_list = []
    for i in range(0, 10):
        a = i*25
        url = 'https://movie.douban.com/top250?start='+str(a)+'&filter='
        url_list.append(url)
    pool = Pool(4)
    pool.map(main, url_list)
    pool.close()
    pool.join()
