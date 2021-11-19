from calendar import week
from time import sleep
import json
from bs4 import BeautifulSoup
import datetime as dt
import pandas as pd
import re
import get_browser, columnname, userinfo
import columnname

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
        print('인터파크 로그인 성공')
        sleep(2)
        """
        wait until browser loadas 추가
        """
    except:
        print("로그인 중 에러")
        # sleep(2)
        while(stack <3):
            print('로그인 다시시도')
            stack += 1
            browser.close()
            sleep(2)
            crawlInterpark()
            if stack >= 3:
                print('인터파크 로그인 실패')
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
    url = 'https://seller.interpark.com/api/orders/acknowledge?orderSendStep=releasedForShipment&orderStatus=40&detailedSearchType=&detailedSearchValue=&searchPeriodType=orderDate&startDate='
    url += week.strftime('%Y-%m-%d')
    url += 'T15%3A00%3A00Z&endDate='
    url += now.strftime('%Y-%m-%d')
    url += 'T14%3A59%3A00Z&page=1&size=500'

    # 완료된 주문문
    # url = ' https://seller.interpark.com/api/orders/delivery?orderStatus=stepComplete&detailedSearchType=&detailedSearchValue=&buyConfirmHoldYn=all&searchPeriodType=deliveredDate&startDate=2021-09-23T15%3A00%3A00Z&endDate=2021-10-23T14%3A59%3A00Z&page=1&size=30'
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
    length = len(data["data"]["orders"])#지금 배송완료에서 따옴
    if(int(length) == 0):
        print('인터파크 주문 0건')
    else:
        print('인터파크 총주문 개수는 : ', length)
        createDf(data, length)

def createDf(customer_data, length):
    # df = pd.DataFrame.from_records(customer_data["data"]['orderDeliveries'][0], index=[0]) 배송완료
    column_name = columnname.interparkColumnname
    df = pd.DataFrame.from_records(customer_data["data"]["orders"][0], index=[0])
    if(int(length) > 1):
        for i in range(int(length)-1):
            df = df.append(customer_data["data"]["orders"][i+1], ignore_index=True)
    df.columns = column_name
    # df = df.drop('del',axis=1)

    createCsv(df)

def createCsv(df):
    df.to_csv(userinfo.path +'interpark.csv', index=True, header=True, na_rep='-', encoding='utf-8-sig')












