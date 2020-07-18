import requests
import os
import time
from tqdm import tqdm
import re
#from selenium import webdriver
#from urllib.request import urlretrieve
from contextlib import closing
from bs4 import BeautifulSoup

url = "https://www.dmzj.com/info/tanzhilangyaozaitailashijiedabaiwucan.html"
r = requests.get(url)
bs = BeautifulSoup(r.text, 'lxml')

#创建保存目录
save_dir = '炭治狼要在泰拉世界打败无惨'
if save_dir not in os.listdir('./'):
    os.mkdir(save_dir)

#1.取到章节名和链接
list_con_li = bs.find('ul', 'list_con_li')
comic_list = list_con_li.find_all('a')
chapter_names = []
chapter_url = []
for comic in comic_list:
    href = comic.get('href') + '@page=1'
    name = comic.text
    chapter_names.insert(0, name)
    chapter_url.insert(0, href)

print(chapter_url)
print(chapter_names)

#2 根据章节链接找到所有漫画图片链接

'''''
img_list = []
driver = webdriver.Chrome()
driver.get("https://www.dmzj.com/view/tanzhilangyaozaitailashijiedabaiwucan/96442.html#@page=1")
select = driver.find_element_by_id('page_select')
option_list = select.find_elements_by_tag_name('option')
for option in option_list:
    value = option.get_attribute('value')
    img_list.append(value)

print(img_list)
driver.close()

'''''
#下载漫画
for i, url in enumerate(tqdm(chapter_url)):
    download_headers = {
        'Referer': url
    }
    print(download_headers)
    name = chapter_names[i]
