from time import sleep
from bs4 import BeautifulSoup
import userinfo, get_browser
import pandas as pd
import re
import columnname
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
                return False
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
    browser.find_element_by_xpath('//*[@id="wing-top-body"]/div/div[2]/div[4]/ul/li[5]/article').click() #배송완료 클릭
    sleep(2)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    getData(soup)

def getData(soup):
    # ordernum = soup.select_one('#wing-top-body > div > div:nth-child(2) > div:nth-child(4) > ul > li:nth-child(1) > article > div > em').get_text() #신규주문
    ordernum = soup.select_one('#wing-top-body > div > div:nth-child(2) > div:nth-child(4) > ul > li:nth-child(5) > article > div > em').get_text()
    total_order = int(ordernum)
    if(int(total_order) == 0):
        print('주문이 없습니다!')
    else:
        print('총주문 개수는 : ', total_order)
        customer_data = soup.select_one('#wing-top-body > div > div.search-table > div > div:nth-child(4) > table > tbody')
        createDf(customer_data, int(total_order))

def createDf(customer_data, length):
    customerList = [[0 for col in range(15)] for row in range(length)] #배송완료 15개
    cnt = 1  # tr 순서 선택
    sleep(2)
    pattern = re.compile(r'\s+')
    for i in range(length):
        info = customer_data.select('tr:nth-child(%d)>td' % cnt)  # 첫번째 tr 선택
        jcnt = 0  # 배열에 넣기 위한 count 증가
        cnt += 1  # 다음 tr 을위해 증가
        for j in info:
            # customerList[i][jcnt] = str(j.get_text()).split()# 배열에 삽입
            customerList[i][jcnt] = re.sub(pattern,' ',str(j.get_text())).strip()# 배열에 삽입
            # print(testList[i][jcnt]) #리스트에 들어간 value들 표시
            jcnt += 1

    # column_name = columnname.esmColumnname
    df = pd.DataFrame(customerList)
    df = df.drop(df.columns[3], axis=1)
    createCsv(df)
    print(df)

def createCsv(df):
    df.to_csv('coupang.csv', index=True, header=True, na_rep='-', encoding='utf-8-sig')
#
#
# cnt = 1
# count = 0
# testList = [0] * 40
# for i in range(length):
#     info = tbody.select('tr:nth-child(%d)>td' % cnt)  # 첫번째 tr 선택
#     cnt += 1  # 다음 tr 을위해 증가
#     count = 0  # 배열에 넣기 위한 count 증가
#     for j in info:
#         testList[count] = j.get_text() + ','  # 배열에 삽입
#         print(testList[count])  #
#         count += 1
#     print("-" * 100)


