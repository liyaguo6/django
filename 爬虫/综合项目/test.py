import urllib.request
from bs4 import BeautifulSoup
import hashlib,os,re,datetime
from db.db_access import insert_hisq_data
URL='https://www.nasdaq.com/symbol/aapl/historical#.UWdnJBDMhHk'
"""
https://www.nasdaq.com/symbol/aapl/historical#.UWdnJBDMhHk

获得静态数据
"""
import random,time
id = 'quotes_content_left_pnlAJAX'
req = urllib.request.Request(URL)
date1 = (2016,1,1,0,0,0,-1,-1,-1)
time1 = time.mktime(date1)
date2 = (2017,1,1,0,0,0,-1,-1,-1)
time2 =time.mktime(date2)

# print(random_time)
def validateUpdate(html):
    #创建MD5
    m5=hashlib.md5()
    m5.update(html.encode('utf-8'))
    md5code =m5.hexdigest()
    old_md5code=''
    print(md5code)
    f_name = 'md5.text'
    if os.path.exists(f_name):
            with open('md5.text','r',encoding='utf-8') as f:
                old_md5code =f.read()
    if md5code == old_md5code:
        print('数据没有更新')
        return True
    else:
        with open('md5.text','w',encoding='utf-8') as f:
            f.write(md5code)
            return True

with urllib.request.urlopen(req) as response:
    data = response.read()
    htmlstr = data.decode()
    sp =BeautifulSoup(htmlstr,'html.parser')
    div = sp.select('div#quotes_content_left_pnlAJAX')
    divstring = div[0]
    # print(divstring)
    if validateUpdate(divstring):
        #CSS选择器
        css = 'div#quotes_content_left_pnlAJAX table tbody tr'
        trlist=sp.select(css)
        data=[]
        fields = {}
        for tr in trlist:
            tryext = tr.text.strip('\n\r')

            if tryext == '':
                continue
            rows = re.split(r'\s+',tryext)
            # print(rows)
            try:
                df = '%m/%d/%Y'
                fields['Date']=random.uniform(time1,time2)
                # print(fields[])
                # print(random_time)
                # print(fields)
            except ValueError as e:
                print('error:',e)
                continue
            # fields['Date'] = rows[1]
            fields['Open'] = float(rows[2])
            fields['High'] = float(rows[3])
            fields['Low'] = float(rows[4])
            fields['Close'] = float(rows[5])
            fields['Volume'] =float( rows[6].replace(",",""))
            data.append(fields)
        # print(data)
        for row in data:
            row['Symbol'] = 'Appl'
            # print(tuple(row.values()))
            # insert_hisq_data(tuple(row.values()))
            insert_hisq_data(row)
            print(row)
            # print(row)
# URL ='http://q.stock.sohu.com/hisHq?code=cn_600519&stat=1&order=D&period=d&callback=historySearchHandler&rt=jsonp&0.8115656498417958'