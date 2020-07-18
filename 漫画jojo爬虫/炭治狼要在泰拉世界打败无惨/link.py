import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.dmzj.com/view/tanzhilangyaozaitailashijiedabaiwucan/96789.html#@page=1'
r = requests.get(url=url)
html = BeautifulSoup(r.text, 'lxml')
script_info = html.script
pics = re.findall('\d{14}', str(script_info))

pics = sorted(pics, key=lambda x:int(x))
chapterpic_hou = re.findall('\|(\d{6})\|', str(script_info))[0]
chapterpic_qian = re.findall('\|(\d{5})\|', str(script_info))[0]
for pic in pics:
    url = 'https://images.dmzj.com/img/chapterpic/' + chapterpic_qian + '/' + chapterpic_hou + '/' + pic + '.png'
    print(url)