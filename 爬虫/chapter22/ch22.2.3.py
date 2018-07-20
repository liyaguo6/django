# coding=utf-8
# Created by 智捷关东升
# 本书网站：www.zhijieketang.com/group/8
# 智捷课堂在线课堂：www.zhijieketang.com
# 智捷课堂微信公共号：zhijieketang
# 邮箱：eorient@sina.com
# 读者服务QQ群：628808216
# 【配套电子书】网址：
#       百度阅读：
#       https://yuedu.baidu.com/ebook/5823871e59fafab069dc5022aaea998fcc2240fc
# 代码文件：chapter22/ch22.2.3.py

from selenium import webdriver

driver = webdriver.Firefox()

driver.get('http://q.stock.sohu.com/cn/600519/lshq.shtml')
em = driver.find_element_by_id('BIZ_hq_historySearch')
print(em.text)
# driver.close()
driver.quit()
