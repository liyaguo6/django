import urllib.request, re,os
from selenium import webdriver

url = 'http://p.weather.com.cn/'

pattern0 = r'http://\S+(?:\.png|\.jpg)'
pattern1 = r'src="([.\S|]+(?:\.png|\.jpg))"'
def findall_imge_url(htmlstr,pattern):
    # \S+非空字符串
    # pattern = r'src="(.*(?:\.png|\.jpg))"'
    # pattern = r'src="([.*\S]*(?:\.png|\.jpg))"'
    return re.findall(pattern, htmlstr)


def getfilename(urlstr):
    pos = urlstr.rfind('/')
    # print(pos)
    return urlstr[pos + 1:]

url_list1 = []
url_list2 = []
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read()
    htmlstr = data.decode()
    url_list0 = findall_imge_url(htmlstr,pattern0)
    url_list1 = findall_imge_url(htmlstr,pattern1)
print(len(url_list0))
print(len(url_list1))
list1 = []
for i in url_list0:
    if i in url_list1:
        pass
    else:
        list1.append(i)
print(list1)
print(len(list1))
for img in url_list0:
    req = urllib.request.Request(img)
    with urllib.request.urlopen(req) as response:
        data = response.read()
        if len(data) <= 1024 * 100:
            continue
        if not os.path.exists('picture'):
            os.mkdir('picture')
        with open(".\\picture\\" + getfilename(img), 'wb') as f:
            f.write(data)
