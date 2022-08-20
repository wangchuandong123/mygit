__author__ = 'admin'
# coding=utf-8
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random


# 请求 数据
def get_data():
    url = "https://book.douban.com/tag/随笔"
    #url = 'https://book.douban.com/tag/随笔?start=' + str(i) + '&type=T'
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}


    data = requests.get(url, headers=headers)
# print(data.text)
    return data


# 解析数据
def parse_data(data):
    soup = BeautifulSoup(data.text, 'lxml')
    # print(soup)

    books = soup.find('ul', {'class': 'subject-list'})
    books = books.find_all('li')
    # print(books)

    img_urls = []
    titles = []
    ratings = []
    authors = []
    details = []

    for book in books:
        img_url = book.find_all('a')[0].find('img').get('src')
        img_urls.append(img_url)
        print(img_url)
        title = book.find_all('a')[1].get_text()
        title = title.replace('\n', '').replace(' ', '')
        print(title)
        titles.append(title)
        # rating = book.find('span', {'class':'rating_nums'}).get_text()
        rating = book.find('div', {'class': 'star clearfix'}).get_text()
        rating = rating.replace('\n', '').replace(' ', '')
        ratings.append(rating)
        print(rating)
        # author = book.find('p', {'class':'color-gray'}).get_text()
        author = book.find('div', {'class': 'pub'}).get_text()
        author = author.replace('\n', '').replace(' ', '')
        authors.append(author)
        print(author)
        detail = book.find('p').get_text()
        detail = detail.replace('\n', '').replace(' ', '')
        details.append(detail)
        print(detail)
    return img_urls, titles, ratings, authors, details
    '''
for i in range(20,80,20):
    url='https://book.douban.com/tag/随笔?start='+str(i)+'&type=T'
    print(url)
    data = requests.get(url, headers=headers)
    #print(data.text)
    soup = BeautifulSoup(data.text, 'lxml')
    #print(soup)
    books= soup.find('ul', {'class': 'subject-list'})
    books= books.find_all('li')
    #print(books)
    for book in books:
        img_url = book.find_all('a')[0].find('img').get('src')
        img_urls.append(img_url)
        #print(img_url)
        title = book.find_all('a')[1].get_text()
        title=title.replace('\n','').replace(' ','')
        #print(title)
        titles.append(title)
        #rating = book.find('span', {'class':'rating_nums'}).get_text()
        rating=book.find('div',{'class':'star clearfix'}).get_text()
        rating = rating.replace('\n','').replace(' ','')
        ratings.append(rating)
        print(rating)
        #author = book.find('p', {'class':'color-gray'}).get_text()
        author=book.find('div',{'class':'pub'}).get_text()
        author = author.replace('\n','').replace(' ','')
        authors.append(author)
        #print(author)
        detail = book.find('p').get_text()
        detail = detail.replace('\n','').replace(' ','')
        details.append(detail)
    time.sleep(random.randint(1,5)+random.random())
'''


# print("img_urls：",img_urls)
# print("titles:",titles)
# print("ratings",ratings)
# print("authors:",authors)
# print("details:",details)
# 存储
def save_data(img_urls, titles, ratings, authors, details):
    result = pd.DataFrame()
    result['img_urls'] = img_urls
    result['titles'] = titles
    result['ratings'] = ratings
    result['authors'] = authors
    result['details'] = details
    result.to_excel('result3.xlsx', index=None)


# 开始爬取数据
def run():
    data = get_data()
    img_urls, titles, ratings, authors, details = parse_data(data)
    save_data(img_urls, titles, ratings, authors, details)


if __name__ == '__main__':
    run()
