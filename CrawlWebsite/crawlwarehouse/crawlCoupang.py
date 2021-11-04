from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import re
import get_browser, columnname, userinfo
import datetime as dt

stack = 0

def crawlCoupang():
    global stack
    browser = get_browser.get_browser()
    try:
        browser.get("https://wing.coupang.com/login")
        browser.find_element_by_id("userID").send_keys(userinfo.coupang_id)
        browser.find_element_by_id("userPWD").send_keys(userinfo.coupang_pw)
        browser.find_element_by_xpath('//*[@id="btnLogin"]').click()
        print('로그인 성공')
        sleep(2)
    except:
        print("로그인 중 에러")
        sleep(2)
        while (stack < 3):
            print('로그인 다시시도')
            stack += 1
            browser.close()
            sleep(2)
            crawlCoupang()
            if stack >= 3:
                print('coupang로그인 실패')
                return
                break
    getSoup(browser)

def getSoup(browser):
    now = dt.datetime.now()
    week = dt.datetime.now() -dt.timedelta(weeks=1)
    url = 'https://wing.coupang.com/tenants/sfl-portal/delivery/management?deliverStatus=ACCEPT&startDate='
    url += week.strftime('%Y-%m-%d')
    url += '&endDate='
    url += now.strftime('%Y-%m-%d')
    browser.get(url)
    browser.find_element_by_xpath('//*[@id="wing-top-body"]/div/div[2]/div[4]/ul/li[1]/article').click()
    sleep(2)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    getData(soup)

def getData(soup):
    ordernum = soup.select_one('#wing-top-body > div > div:nth-child(2) > div:nth-child(4) > ul > li:nth-child(1) > article > div > em').get_text() #신규주문
    # ordernum = soup.select_one('#wing-top-body > div > div:nth-child(2) > div:nth-child(4) > ul > li:nth-child(5) > article > div > em').get_text()
    total_order = int(ordernum)
    if(int(total_order) == 0):
        print('쿠팡 주문 0건')
    else:
        print('총주문 개수는 : ', total_order)
        customer_data = soup.select_one('#wing-top-body > div > div.search-table > div > div:nth-child(4) > table > tbody')
        createDf(customer_data, int(total_order))

def createDf(customer_data, length):
    customerList = [[0 for col in range(20)] for row in range(length)] #배송완료 15개
    cnt = 1  # tr 순서 선택
    sleep(2)
    pattern = re.compile(r'\s+')
    for i in range(length):
        info = customer_data.select('tr:nth-child(%d)>td' % cnt)  # 첫번째 tr 선택
        jcnt = 0  # 배열에 넣기 위한 count 증가
        cnt += 1  # 다음 tr 을위해 증가
        for j in info:
            customerList[i][jcnt] = re.sub(pattern,' ',str(j.get_text())).strip()# 배열에 삽입
            jcnt += 1

    column_name = columnname.coupangColumnname
    df = pd.DataFrame(customerList)
    df = df.drop(df.columns[length], axis=1) #length 3이였음
    createCsv(df)
    print(df)

def createCsv(df):
    df.to_csv(userinfo.path +'coupang.csv', index=True, header=True, na_rep='-', encoding='utf-8-sig')



# 체크 주문번호 분리배송 택배사 운송장번호 출고예정일 등록상품명/옵션/수량 수취인/연락처 배송지 배송상태 주문일시 묶음배송번호 주문자명 배송지연안내 접수