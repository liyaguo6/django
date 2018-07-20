
import urllib.request
from selenium import webdriver
eid = 'BIZ_hq_historySearch'
driver = webdriver.Firefox()
driver.get('http://q.stock.sohu.com/cn/600519/lshq.shtml')
em = driver.find_element_by_id(eid)
print(em.text)
driver.quit()