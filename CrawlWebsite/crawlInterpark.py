
from time import sleep
import requests
import time
from bs4 import BeautifulSoup
import datetime as dt
import userinfo, get_browser
browser = get_browser.get_browser()


#로그인
browser.get("https://seller.interpark.com/login")
browser.find_element_by_id("memId").send_keys(userinfo.interpark_id)
browser.find_element_by_id("memPwd").send_keys(userinfo.interpark_pw)
browser.find_element_by_xpath('//*[@id="frmMemberLogin"]/div[1]/button').click()

# #데이터 가져오기

# NOW
now = dt.datetime.now()
#1주일전
week = dt.datetime.now() -dt.timedelta(weeks=1)

# #데이터 가져오기
sleep(2)
url = 'https://seller.interpark.com/api/orders/acknowledge?orderSendStep=acknowledge&orderStatus=50&detailedSearchType=&detailedSearchValue=&searchPeriodType=orderDate&startDate=2021-09-13T15%3A00%3A00Z&endDate=2021-10-14T14%3A59%3A00Z&page=1&size=30'
url = 'https://seller.interpark.com/api/orders/acknowledge?orderSendStep=acknowledge&orderStatus=50&detailedSearchType=&detailedSearchValue=&searchPeriodType=orderDate&startDate='
url += week.strftime('%Y-%m-%d')
url += 'T15%3A00%3A00Z&endDate='
url += now.strftime('%Y-%m-%d')
url += 'T14%3A59%3A00Z&page=1&size=30'
print(url)

browser.get(url)
sleep(2)

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

print(soup)



# f = open("interparkUserInfo.txt", 'w', encoding="utf8")
# f.write(data)
# f.close()
# browser.close()

