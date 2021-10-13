from time import sleep
from bs4 import BeautifulSoup
import userinfo, get_browser
import datetime as dt


browser = get_browser.get_browser()

#브라우저 로그인
browser.get("https://wing.coupang.com/login")
browser.find_element_by_id("userID").send_keys(userinfo.coupang_id)
browser.find_element_by_id("userPWD").send_keys(userinfo.coupang_pw)
browser.find_element_by_xpath('//*[@id="btnLogin"]').click()
sleep(2)

#주문목록가져오기
x = dt.datetime.now()
url = x.strftime("https://wing.coupang.com/tenants/sfl-portal/delivery/management?deliverStatus=ACCEPT&startDate=%Y-%m-%d&endDate=%Y-%m-%d")
browser.get(url)

#지난 7일 클릭
browser.find_element_by_xpath('//*[@id="wing-top-body"]/div/div[3]/div[2]/div[1]/dl[1]/dd[2]/div/ul/li[2]/button').click()
#검색클릭
browser.find_element_by_xpath('//*[@id="wing-top-body"]/div/div[3]/div[2]/div[2]/button[2]').click()

sleep(4)

html = browser.page_source
soup = BeautifulSoup(html,'html.parser')

#15
#상품준비중에서 따왔음 나중에 바꿔야함
orderers = soup.select_one('#wing-top-body > div > div.search-table > div > div:nth-child(4) > table > tbody')

print(orderers.getText())
