from time import sleep
from bs4 import BeautifulSoup
import userinfo, get_browser

try:
    browser = get_browser.get_browser()
    browser.get("https://www.esmplus.com/Member/SignIn/LogOn")
    browser.find_element_by_id("Id").send_keys(userinfo.gmarket_id)
    browser.find_element_by_id("Password").send_keys(userinfo.gmarket_pw)
    browser.find_element_by_id("btnLogOn").click()
    browser.get('https://www.esmplus.com/Escrow/Delivery/Sending?status=1050&type=N&menuCode=TDM111')
except:
    print("로그인 중 중에러")

# 브라우저 html 받기
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
sleep(2)

# 데이터가져오기
data = soup.select_one('#dataGrid > table > tbody')

tr = data.findAll("tr") # tr이 주문자 개수
length = len(tr) #테이블의 사람들 개수

# tr = data.find('tr', attrs={"class":"even"})

#배열에 저장
testList = [0] * 70
sleep(3)
tbody = soup.select_one('tbody.sb-grid-results')

#배열에 저장
info = tbody.select('tr:nth-child(1)>td')
cnt = 0
for i in info:
    testList[cnt] = i.get_text() + ','
    cnt += 1
print("-"*100)
for i in range(70):
    print(testList[i])

#a = 2
#info = tbody.select('tr:nth-child(%d)>td' %a)


# list = [] #고객 정보들
# cnt = 0
# orderer = data.find('tr', attrs={"class":"even"})
#
# for i in range(length):
#     if(cnt == 0):
#         list.append(orderer.getText())
#         cnt += 1
#     else:
#         orderer = orderer.next_sibling
#         list.append(orderer.getText())
#
# for i in range(length):
#     print("-"*100)
#     print(list[i])






