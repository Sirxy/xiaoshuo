# ! /usr/bin/env python

import requests
from bs4 import BeautifulSoup as BS
import time


def download(url):
    # url = 'https://xs.sogou.com/chapter/14734139_481036348916/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Host': 'xs.sogou.com',
        'Upgrade-Insecure-Requests': '1',
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        }
    response = requests.get(url, params=headers)
    data = response.text
    # print(data)
    soup = BS(data, 'lxml')
    paperdiv = soup.select('div[class="paper-box paper-article"]')[0]
    # print(paperdiv)
    paperh1 = soup.select('div[class="paper-box paper-article"] h1')[0].string
    paperinfo = soup.select('div[class="paper-box paper-article"] div[class="info"]')[0].string
    papercontent = soup.select('div[class="paper-box paper-article"] div[id="contentWp"]')[0].get_text()
    print(paperh1 + '\n' + paperinfo + '\n' + papercontent + '\n')


# https://xs.sogou.com/chapter/14734139_481036348916/


# 整个小说
url = 'https://xs.sogou.com/list/14734139/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    }
response = requests.get(url, params=headers)
data = response.text
soup = BS(data, 'lxml')
papera = soup.select('ul[class="chapter clear"] a')
# print(papera)
for a in papera:
    a = a.get('href')  # href="/chapter/14734139_481036348916/"
    pa = 'https://xs.sogou.com' + str(a)  # 完整的url
    # print(pa)
    download(pa)
    time.sleep(1)

