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
    #배송완료
    browser.get(url)
    # browser.find_element_by_xpath('//*[@id="wing-top-body"]/div/div[2]/div[4]/ul/li[5]/article').click() #배송완료
    browser.find_element_by_xpath('//*[@id="wing-top-body"]/div/div[2]/div[4]/ul/li[1]/article').click() #결제완료
    browser.find_element_by_xpath('//*[@id="wing-top-body"]/div/div[4]/div/div[1]/span[3]/span/select/option[5]').click()
    url = 'https://wing.coupang.com/tenants/sfl-portal/delivery/management/dashboard/search?condition=%7B%22nextShipmentBoxId%22%3Anull%2C%22startDate%22%3A%22'
    url += week.strftime('%Y-%m-%d')
    url += '%22%2C%22endDate%22%3A%22'
    url += now.strftime('%Y-%m-%d')
    url += '%22%2C%22deliveryStatus%22%3A%22ACCEPT%22%2C%22deliveryMethod%22%3Anull%2C%22detailConditionKey%22%3A%22NAME%22%2C%22detailConditionValue%22%3Anull%2C%22selectedComplexConditionKey%22%3Anull%2C%22countPerPage%22%3A10%2C%22page%22%3A1%2C%22shipmentType%22%3Anull%7D&mockingTestMode=false'

    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    getData(soup)

def getDict(soup):  # interpark.txt 만들기
    dict = soup.select_one('body > pre')
    pattern = re.compile(r'\s+')
    txt = dict.get_text()
    with open('coupang.txt', 'w', encoding='utf-8-sig') as f:
        f.write(txt)
    f.close()

def getData(soup):
    getDict(soup)
    with open('coupang.txt', encoding='UTF-8-sig') as json_file:
        data = json.load(json_file)
    length = len(data)#지금 배송완료에서 따옴

    """
    필요없는 데이터삭제
    """

    for i in range(length):
        del data[i]["items"]
        del data[i]["trackingInfos"]
        del data[i]["statusTrace"]
    # data1 = data[0].update(data[0]["safeNumberDto"]) #dict안에 혼자 dict임

    if(int(length) == 0):
        print('쿠팡 주문 0건')
    else:
        print('쿠팡 총주문 개수는 : ', length)
        createDf(data, length)

def createDf(customer_data, length):

    # dfDict = pd.DataFrame.from_records(customer_data[0]["safeNumberDto"],index=0)
    dfDict = dfDict = pd.DataFrame([customer_data[0]["safeNumberDto"]])
    if(int(length)>1):
        for i in range(int(length)-1):
            dfDict = dfDict.append(customer_data[i+1]["safeNumberDto"], ignore_index=True)
    for i in range(length):
        del customer_data[i]["safeNumberDto"]
    dfList = pd.DataFrame(customer_data)
    """
    여기서 dfDict랑 dfList Column 기준으로 합치기
    """
    df = pd.concat([dfList,dfDict], axis=1,ignore_index=True)
    #dfList 먼저 후 dfDict
    createCsv(df)

def createCsv(df):
    df.to_csv(userinfo.path +'coupangTest.csv', index=True, header=True, na_rep='-', encoding='utf-8-sig')

# def createDf(customer_data, length):
#     customerList = [[0 for col in range(40)] for row in range(length)] #배송완료 15개
#     cnt = 1  # tr 순서 선택
#     sleep(2)
#     pattern = re.compile(r'\s+')
#     for i in range(length):
#         info = customer_data.select('tr:nth-child(%d)>td' % cnt)  # 첫번째 tr 선택
#         jcnt = 0  # 배열에 넣기 위한 count 증가
#         cnt += 1  # 다음 tr 을위해 증가
#         for j in info:
#             # customerList[i][jcnt] = str(j.get_text()).split()# 배열에 삽입
#             customerList[i][jcnt] = re.sub(pattern,' ',str(j.get_text())).strip()# 배열에 삽입
#             # print(testList[i][jcnt]) #리스트에 들어간 value들 표시
#             jcnt += 1
#
#     column_name = columnname.coupangColumnname
#     df = pd.DataFrame(customerList)
#     df = df.drop(df.columns[length], axis=1) #length 3이였음
#     createCsv(df)
#     print(df)
#




# 체크 주문번호 분리배송 택배사 운송장번호 출고예정일 등록상품명/옵션/수량 수취인/연락처 배송지 배송상태 주문일시 묶음배송번호 주문자명 배송지연안내 접수