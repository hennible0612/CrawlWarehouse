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
        browser.get('https://www.esmplus.com/Escrow/Order/NewOrder?type=N2&menuCode=TDM105')
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
    if (data == "    조회된 데이터가 없습니다."):
        print("ESM 에서 새로운 주문이 없습니다.")
        return False
    else:
        print(length + "개의 주문이 있습니다.")
        list = []  # 고객 정보들
        cnt = 0
        orderer = data.find('tr', attrs={"class": "even"})
        for i in range(length):
            if (cnt == 0):
                list.append(orderer.getText())
                cnt += 1
            else:
                orderer = orderer.next_sibling
                list.append(orderer.getText())
        return list









