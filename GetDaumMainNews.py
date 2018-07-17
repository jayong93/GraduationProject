#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup


def get_article_title(url):
    ret_url = url
    rq = requests.get(url)
    soup = BeautifulSoup(rq.text, 'html.parser')
    if 'm.media' in url:
        article = soup.select('div.item_mainnews div.cont_thumb a')
        ret_url = article[0]['href']
        rq = requests.get(ret_url)
        soup = BeautifulSoup(rq.text, 'html.parser')

    return (soup.find('h3', class_='tit_view').text, ret_url)


if __name__ == '__main__':
    rq = requests.get('https://m.daum.net')
    soup = BeautifulSoup(rq.text, 'html.parser')
  
    articles = []
    articles += soup.select('div.out_ibox div:nth-of-type(1) ul.list_txt a')

    titles = [get_article_title(article['href']) for article in articles[:5]]
    
    for title in titles:
        print(title[0])
        print(title[1])