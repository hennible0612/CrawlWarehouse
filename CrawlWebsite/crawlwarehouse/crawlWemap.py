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
    createCsv(df)

def createCsv(df):
    df.to_csv(userinfo.path +'Wemap.csv', index=True, header=True, na_rep='-', encoding='utf-8-sig')

# sleep(5)
# #인증번호 요청하기
# browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/label[1]").click()
# browser.find_element_by_xpath('//*[@id="sendAuth"]').click()


# sleep(20)
# #인증번호
# username = userinfo.gmail_id
# password = userinfo.gmail_pw
# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(username,password, initial_folder="INBOX")
# authNum = 0;
#
# for msg in mailbox.fetch('(FROM no-reply@wemakeprice.com UNSEEN)', limit=10, reverse=True):
#     soup = BeautifulSoup(msg.html,"html")
#     data1 = soup.select_one('body > div > table > tbody > tr:nth-child(5) > td > table > tbody > tr:nth-child(1) > td:nth-child(3) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(2) > strong')
#     authNum = data1.getText()
#
# mailbox.logout()
#
# #인증번호 입력
# browser.find_element_by_xpath('//*[@id="authCode"]').click()
# browser.find_element_by_xpath('//*[@id="authCode"]').send_keys(authNum)
# browser.find_element_by_xpath('//*[@id="checkAuth"]').click()

# sleep(2)
# #알림창 dismiss
# notice = browser.switch_to_alert()
# notice.dismiss()
#
# # 비밀번호 다음에 변경하기
# browser.find_element_by_xpath('//*[@id="reactapp"]/div/div[2]/div/button[2]').click()

# #데이터 가져오기
# browser.find_element_by_xpath('//*[@id="requestCancelCount"]').click()
# html = browser.page_source
# soup = BeautifulSoup(html, 'html.parser')
# orderers = soup.select_one('#orderInfoGrid > div.objbox > table > tbody > tr.ev_dhx_web')
#
