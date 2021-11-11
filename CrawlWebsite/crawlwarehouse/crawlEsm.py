from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import re
import get_browser, columnname, userinfo


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
        print('ESM 로그인 성공')
        sleep(2)
        """
        wait until browswerloads
        """
    except:
        print("로그인 중 에러")
        # sleep(2)
        while(stack <3):
            print('로그인 다시시도')
            stack += 1
            browser.close()
            crawlEsm()
            if stack >= 3:
                print('ESM 로그인 실패')
                return False
                break
    getSoup(browser)

def Logout(browser):
    browser.get('https://www.esmplus.com/Home/Home')
    browser.find_element_by_xpath('//*[@id="logoff"]/a').click()
    browser.close()

def getSoup(browser):
    # 브라우저 html 받기
    browser.get('https://www.esmplus.com/Escrow/Order/NewOrder?type=N2&menuCode=TDM105') #새주문
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    getData(soup)

def getData(soup):
    # 주문 데이터 가져오기
    ordernum = soup.select_one('#liTab1 > a > span') #신규주문
    total_order = re.sub(r'[^0-9]', '', str(ordernum))
    if (int(total_order) == 0):
        print('ESM 주문 0건')
    else:
        print('ESM 총주문 개수는 : ', total_order)
        customer_data = soup.select_one('tbody.sb-grid-results')  # 결과
        createDf(customer_data, int(total_order))

def createDf(customer_data, length):
    customerList = [[0 for col in range(62)] for row in range(length)]
    cnt = 1  # tr 순서 선택
    pattern = re.compile(r'\s+')
    # sleep(2)
    for i in range(length):
        info = customer_data.select('tr:nth-child(%d)>td' % cnt)  # 첫번째 tr 선택
        jcnt = 0  # 배열에 넣기 위한 count 증가
        cnt += 1  # 다음 tr 을위해 증가
        for j in info:
            customerList[i][jcnt] = re.sub(pattern,' ',str(j.get_text())).strip() # 배열에 삽입
            jcnt += 1

    column_name = columnname.esmColumnname
    df = pd.DataFrame(customerList, columns=column_name)
    df = df.drop(df.columns[i], axis=1)
    createCsv(df)

def createCsv(df):
    df.to_csv(userinfo.path + 'esm.csv', index=True, header=True, na_rep='-', encoding='utf-8-sig')

