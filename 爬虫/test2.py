import urllib.request
URL=' http://q.stock.sohu.com/hisHq?code=cn_600519&start=20180322&end=20180718&stat=1&order=D&period=w&callback=historySearchHandler&rt=jsonp&r=0.3935974924103014&0.6517555912353485'
"""
https: http://q.stock.sohu.com/hisHq?code=cn_600519&start=20180322&end=20180718&stat=1&order=D&period=w&callback=historySearchHandler&rt=jsonp&r=0.3935974924103014&0.6517555912353485

获得动态数据
"""





req = urllib.request.Request(URL)

with urllib.request.urlopen(req) as response:
    data = response.read()
    json_data = data.decode('gbk')
    json_data =json_data.replace('historySearchHandler(','')
    json_data =json_data.replace(')','')
    print(json_data)


