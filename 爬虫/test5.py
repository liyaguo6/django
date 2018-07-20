from bs4 import BeautifulSoup


import urllib.request, re,os
from selenium import webdriver

url = 'http://p.weather.com.cn/'

pattern0 = r'http://\S+(?:\.png|\.jpg)'
pattern1 = r'src="([.\S|]+(?:\.png|\.jpg))"'
def findall_imge_url(htmlstr):
    sp = BeautifulSoup(htmlstr,'html.parser')  #实例化一个对象
    imgtablist = sp.find_all('img')
    # print(imgtablist)  #<class 'bs4.element.ResultSet'>
    # print(type(imgtablist))
    srclist = list(map(lambda u:u.get('src'),imgtablist))
    filtered_srclist = list(filter(lambda u:u.lower().endswith('.png')or u.endswith('.jpg'),srclist))
    return filtered_srclist


def getfilename(urlstr):
    pos = urlstr.rfind('/')
    # print(pos)
    return urlstr[pos + 1:]


req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read()
    htmlstr = data.decode()
    url_list0 = findall_imge_url(htmlstr)
    # url_list1 = findall_imge_url(htmlstr,pattern1)


print(url_list0)

for img_url in url_list0:
    req = urllib.request.Request(img_url)
    with urllib.request.urlopen(req) as response:
        data = response.read()
        if len(data) <= 1024 * 100:
            continue
        if not os.path.exists('picture'):
            os.mkdir('picture')
        with open(".\\picture\\" + getfilename(img), 'wb') as f:
            f.write(data)
