from time import sleep
from bs4 import BeautifulSoup
import userinfo, get_browser

def crawlEsm():
    # 로그인
    try:
        browser = get_browser.get_browser()
        browser.get("https://www.esmplus.com/Member/SignIn/LogOn")
        browser.find_element_by_id("Id").send_keys(userinfo.gmarket_id)
        browser.find_element_by_id("Password").send_keys(userinfo.gmarket_pw)
        browser.find_element_by_id("btnLogOn").click()
        #browser.get('https://www.esmplus.com/Escrow/Order/NewOrder?type=N2&menuCode=TDM105') 새주문
        browser.get('https://www.esmplus.com/Escrow/Delivery/Sending?status=1050&type=N&menuCode=TDM111') #완료된주문

    except:
        print("로그인 중 중에러")

    # 브라우저 html 받기
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    sleep(2)

    # 데이터가져오기
    data = soup.select_one('#dataGrid > table > tbody')
    tr = data.findAll("tr")  # tr이 주문자 개수
    length = len(tr)  # 테이블의 사람들 개수
    sleep(2)
    if (data == " 조회된 데이터가 없습니다."):
        print("ESM 에서 새로운 주문이 없습니다.")
    else:
        print(length, "개의 주문이 있습니다.")
        data = soup.select_one('#dataGrid > table > tbody') #tbody
        tbody = soup.select_one('tbody.sb-grid-results') #결과
        get_info(tbody, length,soup)



def get_info(tbody, length, soup):
    testList = [0] * 70
    sleep(3)
    tbody = soup.select_one('tbody.sb-grid-results')
    # info = tbody.select('tr:nth-child(1)>td')
    cnt = 0
    sleep(3)
    #     info = tbody.select('tr:nth-child(%d)>td' % cnt)
    for i in range(length):
        info = tbody.select('tr:nth-child(%d)>td' % cnt) # 첫번째 tr 선택
        cnt += 1 #다음 tr 을위해 증가
        count = 0 #배열에 넣기 위한 count 증가
        for j in info:
            testList[count] = j.get_text() + ',' #배열에 삽입
            print(testList[count]) #
            count += 1
        print("-" * 100)

