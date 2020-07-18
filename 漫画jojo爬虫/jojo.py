import requests
from bs4 import BeautifulSoup
first_url = "http://www.myfcomic.com"
url = "http://www.myfcomic.com/comic/165"

res = requests.get(url=url)
bs = BeautifulSoup(res.text, 'lxml')
list_chapter = bs.find('div', class_='comic_chapter_list')
url_list = list_chapter.find_all('a')
comic_list = list_chapter.find_all('p')
chapter_name = []
chapter_url = []
for comic in comic_list:
    name = comic.text
    chapter_name.insert(0, name)

for comic in url_list:
    href = comic.get('href')
    href = first_url + href
    chapter_url.insert(0, href)
    #id = href[10:13]
    #cid = href[-4:]
#print(id)
#print(cid)
chapter_name.reverse()
chapter_url.reverse()
print(chapter_name) #取到所有章节的名称
print(chapter_url) #取到所有章节的url
#base_url = "http://cdnmyfcomicadminmark.myfcomic.com/images/upin_comics/"
'''''
true_url = []
for comic in url_list:
    href = comic.get('href')
    chapter_url.insert(0, href)
    id = href[10:13]
    cid = href[-4:]
    target_url = base_url + id + '/chapter/' + cid
    true_url.insert(0, target_url)
print(true_url)
'''''
src_list = []
test_url = chapter_url[0]
print(test_url)

r = requests.get(url=test_url)
bs = BeautifulSoup(r.text, 'lxml')
div_list = bs.find('div', class_='cview_list_even_box')

'''''
    div2_list = div_list.contents
    img_list = div_list.find_all('img', class_='el-image__inner')
    src = img_list.get('src')
    src_list.insert(0, src)
print(div_list)
print(src_list)
'''''
print(div_list)
'''''
http://cdnmyfcomicadminmark.myfcomic.com/images/upin_comics/165/chapter/2057/
06ee774922182351aaebb92776ae6b71.jpg@!q90?auth_key=1594463291-0-0-72ca9ec740e179a81910a99e30671f6c

http://cdnmyfcomicadminmark.myfcomic.com/images/upin_comics/165/chapter/2057/
0f6a2cf8a001ed9a6a73b671f7af72f4.jpg@!q90?auth_key=1594486613-0-0-75055dbea3295e0ed2d17c9fd960e4af

http://cdnmyfcomicadminmark.myfcomic.com/images/upin_comics/165/chapter/2057/
06ee774922182351aaebb92776ae6b71.jpg@!q90?auth_key=1594486233-0-0-6e252cfd7a76c2a135541c1d01e8bd16

http://cdnmyfcomicadminmark.myfcomic.com/images/upin_comics/165/chapter/2057/
2da4641ed4bebc224302000cd3de7185.jpg@!q90?auth_key=1594469487-0-0-063977f29dcc8c12ac5fa633b60b38b4
'''''