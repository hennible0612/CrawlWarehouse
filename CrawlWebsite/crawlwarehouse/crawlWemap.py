from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import re
import datetime as dt
import json
import get_browser, columnname, userinfo

stack = 0
def crawlWemap():
    global stack
    browser = get_browser.get_browser()
    try:
        browser.get("https://wpartner.wemakeprice.com/login")
        browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div[1]/div[1]/input[1]").send_keys(
            userinfo.wemap_id)
        browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div[1]/div[1]/input[2]").send_keys(
            userinfo.wemap_pw)
        browser.find_element_by_id("login").click()
        print('위메프 로그인 성공')
        sleep(2)
        """
        wait until browser loads 추가
        """
    except:
        print("로그인 중 에러")
        # sleep(2)
        while (stack < 3):
            print('로그인 다시시도')
            stack += 1
            browser.close()
            # sleep(2)
            crawlWemap()
            if stack >= 3:
                print('위매프로그인 실패')
                return
                break
    getSoup(browser)

def getSoup(browser):
    # browser.get('https://wpartner.wemakeprice.com/ship/orderMain')
    now = dt.datetime.now()
    week = dt.datetime.now() - dt.timedelta(weeks=1)
    url='https://wpartner.wemakeprice.com/ship/getOrderInfoList.json?confirmShipNoStr=&schTotalFlag=&schDateType=orderDt&schStartDate='
    url += week.strftime('%Y-%m-%d')
    url += '&schEndDate='
    url += now.strftime('%Y-%m-%d')
    url += '&schShipStatus=D1&schShipMethod=&schDelayShipInfoYn=&schType=&schValue=&schLimitCnt=100&schPageNo=1&_=1635125837449'
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    getData(soup)

def getData(soup):
    getDict(soup)
    with open('wemap.txt', encoding='UTF-8-sig') as json_file:
        data = json.load(json_file)
    length = len(data)
    if(length == 0):
        print('위메프 주문 0건')
    else:
        print('위메프 총주문 개수는 : ', length)
        createDf(data, length)

def getDict(soup): #interpark.txt 만들기
    dict = soup.select_one('body > pre')
    pattern = re.compile(r'\s+')
    txt = dict.get_text()
    with open('wemap.txt', 'w', encoding='utf-8-sig') as f:
        f.write(txt)
    f.close()

def createDf(customer_data, length):
    # df = pd.DataFrame.from_records(customer_data[0], columns=column_name, index=[0])
    df = pd.DataFrame.from_records(customer_data[0], index=[0])
    if(int(length) > 1):
        for i in range(int(length)-1):
            df = df.append(customer_data[i+1], ignore_index=True)
    column_name = columnname.wemapColumnname

    df.columns = column_name
    df = df.drop('del',axis=1)

    createCsv(df)

def createCsv(df):
    df.to_csv(userinfo.path +'Wemap.csv', index=True, header=True, na_rep='-', encoding='utf-8-sig')
