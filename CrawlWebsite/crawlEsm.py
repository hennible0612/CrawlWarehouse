from time import sleep
from bs4 import BeautifulSoup
import userinfo, get_browser
import pandas as pd
import re
import columnname
stack = 0

def crawlEsm():
    # 로그인
    global stack
    browser = get_browser.get_browser()
    try:
        browser.get("https://www.esmplus.com/Member/SignIn/LogOn")
        browser.find_element_by_id("Id").send_keys(userinfo.gmarket_id)
        browser.find_element_by_id("Password").send_keys(userinfo.gmarket_pw)
        browser.find_element_by_id("btnLogOn").click()
        print('로그인 성공')
        sleep(2)
    except:
        print("로그인 중 중에러")
        sleep(2)
        while(stack <3):
            print('로그인 다시시도')
            stack += 1
            browser.close()
            sleep(2)
            crawlEsm()
            if stack >= 3:
                print('esm로그인 실패')
                return False
                break
    getSoup(browser)

def Logout(browser):
    browser.get('https://www.esmplus.com/Home/Home')
    browser.find_element_by_xpath('//*[@id="logoff"]/a').click()
    browser.close()


def getSoup(browser):
    # 브라우저 html 받기
    # browser.get('https://www.esmplus.com/Escrow/Order/NewOrder?type=N2&menuCode=TDM105') #새주문
    browser.get('https://www.esmplus.com/Escrow/Delivery/Sending?status=1050&type=N&menuCode=TDM111')  # 완료된주문
    sleep(2)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # Logout(browser)
    getData(soup)


def getData(soup):
    # 주문 데이터 가져오기
    ordernum = soup.select_one('#totalSendingCount > span')  # 주문완료에서 따옴
    # ordernum = soup.select_one('#liTab1 > a > span') #신규주문
    total_order = re.sub(r'[^0-9]', '', str(ordernum))
    if (int(total_order) == 0):
        print('주문이 없습니다!')
    else:
        print('총주문 개수는 : ', total_order)
        customer_data = soup.select_one('tbody.sb-grid-results')  # 결과
        createDf(customer_data, int(total_order))


def createDf(customer_data, length):
    testList = [[0 for col in range(62)] for row in range(length)]
    cnt = 1  # tr 순서 선택
    sleep(2)
    for i in range(length):
        info = customer_data.select('tr:nth-child(%d)>td' % cnt)  # 첫번째 tr 선택
        jcnt = 0  # 배열에 넣기 위한 count 증가
        cnt += 1  # 다음 tr 을위해 증가
        for j in info:
            testList[i][jcnt] = j.get_text()  # 배열에 삽입
            # print(testList[i][jcnt]) #리스트에 들어간 value들 표시
            jcnt += 1

    column_name = columnname.esmColumnname
    df = pd.DataFrame(testList, columns=column_name)
    createCsv(df)
    print(df)
    #     print("-"*100)
    # for i in range(length): #2차원 배열 체크용
    #     for j in range(62):
    #         print(i,j)
    #         print(testList[i][j])
    #     print("-"*100)

def createCsv(df):
    df.to_csv('esm.csv', index=True, header=True, na_rep='-', encoding='utf-8-sig')

