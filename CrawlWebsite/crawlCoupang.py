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
now = dt.datetime.now()
week = dt.datetime.now() -dt.timedelta(weeks=1)
url = 'https://wing.coupang.com/tenants/sfl-portal/delivery/management?deliverStatus=ACCEPT&startDate='
url += week.strftime('%Y-%m-%d')
url += '&endDate='
url += now.strftime('%Y-%m-%d')
browser.get(url)
#------------------------------------------------건들지 위로------------------------------------------------------------------------------------#
# browser.find_element_by_xpath('//*[@id="wing-top-body"]/div/div[2]/div[4]/ul/li[5]/article').click() #배송완료 클릭
sleep(4)

html = browser.page_source
soup = BeautifulSoup(html,'html.parser')


sleep(3)
tbody = soup.select_one('#wing-top-body > div > div.search-table > div > div:nth-child(4) > table > tbody')
length = len(tbody.findAll("tr"))


cnt = 1
count = 0
testList = [0] * 40
for i in range(length):
    info = tbody.select('tr:nth-child(%d)>td' % cnt)  # 첫번째 tr 선택
    cnt += 1  # 다음 tr 을위해 증가
    count = 0  # 배열에 넣기 위한 count 증가
    for j in info:
        testList[count] = j.get_text() + ','  # 배열에 삽입
        print(testList[count])  #
        count += 1
    print("-" * 100)


