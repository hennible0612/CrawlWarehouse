from calendar import week
from time import sleep
import json
from bs4 import BeautifulSoup
import datetime as dt
import userinfo, get_browser
import pandas as pd
import re
stack = 0
def crawlInterpark():
    # 로그인
    global stack
    browser = get_browser.get_browser()
    try:
        browser.get("https://seller.interpark.com/login")
        browser.find_element_by_id("memId").send_keys(userinfo.interpark_id)
        browser.find_element_by_id("memPwd").send_keys(userinfo.interpark_pw)
        browser.find_element_by_xpath('//*[@id="frmMemberLogin"]/div[1]/button').click()
        print('로그인 성공')
        sleep(2)
    except:
        print("로그인 중 에러")
        sleep(2)
        while(stack <3):
            print('로그인 다시시도')
            stack += 1
            browser.close()
            sleep(2)
            crawlInterpark()
            if stack >= 3:
                print('esm로그인 실패')
                return False
                break
    getSoup(browser)

# def Logout(browser):
#     browser.get('https://www.esmplus.com/Home/Home')
#     browser.find_element_by_xpath('//*[@id="logoff"]/a').click()
#     browser.close()
#
def getSoup(browser):
    # 브라우저 html 받기
    now = dt.datetime.now()
    week = dt.datetime.now() - dt.timedelta(weeks=1)
    # 신규주문
    # url = 'https://seller.interpark.com/api/orders/acknowledge?orderSendStep=releasedForShipment&orderStatus=40&detailedSearchType=&detailedSearchValue=&searchPeriodType=orderDate&startDate='
    # url += week.strftime('%Y-%m-%d')
    # url += 'T15%3A00%3A00Z&endDate='
    # url += now.strftime('%Y-%m-%d')
    # url += 'T14%3A59%3A00Z&page=1&size=500'

    # 완료된 주문문
    url = ' https://seller.interpark.com/api/orders/delivery?orderStatus=stepComplete&detailedSearchType=&detailedSearchValue=&buyConfirmHoldYn=all&searchPeriodType=deliveredDate&startDate=2021-09-20T15%3A00%3A00Z&endDate=2021-10-21T14%3A59%3A00Z&page=1&size=30'
    browser.get(url)  # 완료된주문
    sleep(2)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    getData(soup)
    sleep(3)

def getDict(soup): #interpark.txt 만들기
    dict = soup.select_one('body>pre')
    pattern = re.compile(r'\s+')
    txt = dict.get_text()
    with open('interpark.txt', 'w', encoding='utf-8-sig') as f:
        f.write(txt)
    f.close()

def getData(soup):
    getDict(soup)
    with open('interpark.txt', encoding='UTF-8-sig') as json_file:
        data = json.load(json_file)
    del data["code"]
    del data["message"]

#
# def createDf(customer_data, length):
#     customerList = [[0 for col in range(62)] for row in range(length)]
#     cnt = 1  # tr 순서 선택
#     pattern = re.compile(r'\s+')
#     sleep(2)
#     for i in range(length):
#         info = customer_data.select('tr:nth-child(%d)>td' % cnt)  # 첫번째 tr 선택
#         jcnt = 0  # 배열에 넣기 위한 count 증가
#         cnt += 1  # 다음 tr 을위해 증가
#         for j in info:
#             customerList[i][jcnt] = re.sub(pattern,' ',str(j.get_text())).strip() # 배열에 삽입
#             # print(testList[i][jcnt]) #리스트에 들어간 value들 표시
#             jcnt += 1
#
#     column_name = columnname.esmColumnname
#     df = pd.DataFrame(customerList, columns=column_name)
#     createCsv(df)
#     print(df)
#     #     print("-"*100)
#     # for i in range(length): #2차원 배열 체크용
#     #     for j in range(62):
#     #         print(i,j)
#     #         print(testList[i][j])
#     #     print("-"*100)
#
# def createCsv(df):
#     df.to_csv('esm.csv', index=True, header=True, na_rep='-', encoding='utf-8-sig')












