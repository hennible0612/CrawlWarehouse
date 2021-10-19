from time import sleep
from bs4 import BeautifulSoup
import userinfo, get_browser
import pandas as pd

def crawlEsm():
    # 로그인
    try:
        browser = get_browser.get_browser()
        browser.get("https://www.esmplus.com/Member/SignIn/LogOn")
        browser.find_element_by_id("Id").send_keys(userinfo.gmarket_id)
        browser.find_element_by_id("Password").send_keys(userinfo.gmarket_pw)
        browser.find_element_by_id("btnLogOn").click()
        # browser.get('https://www.esmplus.com/Escrow/Order/NewOrder?type=N2&menuCode=TDM105') #새주문
        browser.get('https://www.esmplus.com/Escrow/Delivery/Sending?status=1050&type=N&menuCode=TDM111') #완료된주문
    except:
        print("로그인 중 중에러")

    # 브라우저 html 받기
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    sleep(2)

    # 데이터가져오기
    data = soup.select_one('#dataGrid > table > tbody')
    tr = data.findAll("tr") # tr이 주문자 개수
    length = len(tr)  # 테이블의 사람들 개수

    sleep(2)
    if (data == " 조회된 데이터가 없습니다."):
        print("ESM 에서 새로운 주문이 없습니다.")
    else:
        print(length, "개의 주문이 있습니다.")
        data = soup.select_one('#dataGrid > table > tbody') #tbody
        tbody = soup.select_one('tbody.sb-grid-results') #결과
        get_info(tbody, length,soup)
    browser.close()


def get_info(tbody, length, soup):
    testList = [[0]*62 for _ in range(62)]#*length # testList = [[0]*62] * length
    testList= [[0 for col in range(62)]for row in range(length)]
    # testList = [[0]*length for _ in range(length)]*length # testList = [[0]*62] * length
    tbody = soup.select_one('tbody.sb-grid-results')
    cnt = 1 #tr 순서 선택
    sleep(2)
    for i in range(length):
        info = tbody.select('tr:nth-child(%d)>td' % cnt) # 첫번째 tr 선택
        jcount = 0 #배열에 넣기 위한 count 증가
        cnt += 1  # 다음 tr 을위해 증가
        for j in info:
            testList[i][jcount] = j.get_text() #배열에 삽입
            # print(testList[i][jcount]) #리스트에 들어간 value들 표시
            jcount += 1
    #     print("-"*100)
    # for i in range(length): #2차원 배열 체크용
    #     for j in range(62):
    #         print(i,j)
    #         print(testList[i][j])
    #     print("-"*100)

    df = pd.DataFrame(testList)
    df.to_csv('esm.csv', index = True, header = True, na_rep = '-', encoding='utf-8-sig')







