import requests
import os
import time
from tqdm import tqdm
import re
#from selenium import webdriver
#from urllib.request import urlretrieve
from contextlib import closing
from bs4 import BeautifulSoup

#创建保存目录
save_dir = '炭治狼要在泰拉世界打败无惨'
if save_dir not in os.listdir('./'):
    os.mkdir(save_dir)

#1.取到章节名和链接
target_url = "https://www.dmzj.com/info/tanzhilangyaozaitailashijiedabaiwucan.html"
r = requests.get(target_url)
bs = BeautifulSoup(r.text, 'lxml')
list_con_li = bs.find('ul', 'list_con_li')
comic_list = list_con_li.find_all('a')
chapter_names = []
chapter_url = []
for comic in comic_list:
    href = comic.get('href') + '@page=1'
    name = comic.text
    chapter_names.insert(0, name)
    chapter_url.insert(0, href)

#下载漫画
for i, url in enumerate(tqdm(chapter_url)):
    download_headers = {
        'Referer': url
    }
    #print(download_headers)
    name = chapter_names[i]
    #print(name)

    chapter_save_dir = os.path.join(save_dir, name)
    if name not in os.listdir(save_dir):
        os.mkdir(chapter_save_dir)
        r = requests.get(url=target_url)
        html = BeautifulSoup(r.text, 'lxml')
        script_info = html.script
        pics = re.findall('\d{14}', str(script_info))
        #1586 2469 0118 55
        print(pics)
        #pics = sorted(pics, key=lambda x: int(x))
        chapterpic_hou = re.findall('\|(\d{6})\|', str(script_info))[0]
        chapterpic_qian = re.findall('\|(\d{5})\|', str(script_info))[0]
        print(chapterpic_hou)
        print(chapterpic_qian)
        for idx, pic in enumerate(pics):
            url = 'https://images.dmzj.com/img/chapterpic/' + chapterpic_qian + '/' + chapterpic_hou + '/' + pic + '.png'
            pic_name = '%03d.jpg' % (idx + 1)

            pic_save_path = os.path.join(chapter_save_dir, pic_name)
            with closing(requests.get(url, headers=download_headers, stream=True)) as response:
                chunk_size = 1024
                content_size = int(response.headers['content-length'])
                if response.status_code == 200:
                    with open(pic_save_path, "wb") as file:
                        for data in response.iter_content(chunk_size=chunk_size):
                            file.write(data)
                else:
                    print('链接异常')
        time.sleep(10)
        print(pic_name)

    #2 根据章节链接找到所有漫画图片链接
        #selenium方法
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
        #用正则匹配js
'''''

        download_header = {
            #'Referer': 'http://www.myfcomic.com/cview?id=165&cid=2057'
            'Referer' : url
            #'Referer': 'https://www.dmzj.com/info/tanzhilangyaozaitailashijiedabaiwucan.html'
        }
        url = "https://images.dmzj.com/img/chapterpic/32271/121068/15862469011855.png"
        #url = "http://cdnmyfcomicadminmark.myfcomic.com/images/upin_comics/165/chapter/2057/06ee774922182351aaebb92776ae6b71.jpg@!q90?auth_key=1594463291-0-0-72ca9ec740e179a81910a99e30671f6c"
        with closing(requests.get(url, headers=download_header, stream=True)) as response:
            chunk_size = 1024
            content_size = int(response.headers['content-length'])
            if response.status_code == 200:
                print('文件大小:%0.2f KB' % (content_size / chunk_size))
                with open('1.jpg', 'wb') as file:
                    for data in response.iter_content(chunk_size=chunk_size):
                        file.write(data)
            else:
                print('链接异常')
        print('下载完成!')
'''''