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
    data = soup.select_one('#dataGrid').getText()
    sleep(2)
    if (data == "    조회된 데이터가 없습니다."):
        print("ESM 에서 새로운 주문이 없습니다.")
    else:
        print("주문이 있습니다.")

    f = open("esmUserInfo.txt", 'w', encoding="utf8")
    f.write(data)
    f.close()
    browser.close()



