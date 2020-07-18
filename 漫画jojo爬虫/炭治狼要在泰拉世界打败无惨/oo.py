import requests
from contextlib import closing

download_header = {
    'Referer': 'https://www.dmzj.com/info/tanzhilangyaozaitailashijiedabaiwucan.html'
}

dn_url = 'https://images.dmzj.com/img/chapterpic/32271/121068/15862469011855.png'
with closing(requests.get(dn_url, headers=download_header, stream=True)) as response:
    chunk_size = 1024
    content_size = int(response.headers['content-length'])
    if response.status_code == 200:
        print('文件大小:%0.2f KB' % (content_size / chunk_size))
        with open('ff.jpg', "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
    else:
        print('链接异常')
print('下载完成！')
