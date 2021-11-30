from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import re
from .common import userinfo, columnname, get_browser


stack = 0

def crawlNaver():
    global stack
    browser = get_browser.get_browser()
    # try:
    browser.get('https://nid.naver.com/nidlogin.login?url=https%3A%2F%2Fsell.smartstore.naver.com%2F%23%2FnaverLoginCallback%3Furl%3Dhttps%253A%252F%252Fsell.smartstore.naver.com%252F%2523')
    browser.find_element_by_xpath('//*[@id="id"]').send_keys(userinfo.naver_id)
    browser.find_element_by_xpath('//*[@id="pw"]').send_keys(userinfo.naver_pw)
    browser.find_element_by_xpath('//*[@id="log.login"]/span').click()
    browser.find_element_by_xpath('//*[@id="new.save"]').click()
    sleep(3)
    tmpl = browser.current_url
    if(tmpl == 'https://sell.smartstore.naver.com/#/secondCertification'):
        browser.find_element_by_xpath('/html/body/ui-view[1]/form/div/div/div/div/div[1]/div[2]/div[2]/div/ncp-certificate-field-mobile/div/div[2]/div/span/button').click()
        print('인증번호 입력하세요')
        authnum = input()
        browser.find_element_by_xpath('/html/body/ui-view[1]/form/div/div/div/div/div[1]/div[2]/div[2]/div/ncp-certificate-field-mobile/div[2]/div[1]/div/input').send_keys(authnum)
        browser.find_element_by_xpath('/html/body/ui-view[1]/form/div/div/div/div/div[2]/button/span[1]').click()
        browser.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/span/button').click()
        # if('인증번호를 다시 확인해주세요' == '')
    else:
        print('네이버 로그인 성공')
    getSoup(browser)

def getSoup(browser):
    # 배송중으로 연습 할꺼임
    browser.get("https://sell.smartstore.naver.com/o/v3/n/sale/delivery") # 신규주문
    soup = BeautifulSoup(browser.page_source,'html.parser')
    getData(soup)

def getData(soup):
    # 주문 데이터 가져오기
    #아래는 신규주문
    ordernum = soup.select_one('#__app_root__ > div > div.napy_sub_content > div:nth-child(2) > div > div:nth-child(2) > ul > li.on._3In6Nn0ucW._1pb3RPYXfD > div > a._3a4NLUdd2p > b').get_text() #신규주문
    total_order = re.sub(r'[^0-9]', '', str(ordernum))
    if (int(total_order) == 0):
        print('네이버 주문 0건')
    else:
        print('네이버 총주문 개수는 : ', total_order)
        customer_data = soup.select_one('#__app_root__ > div > div.napy_sub_content > div:nth-child(4) > div.npay_grid_area > div.grid > div.tui-grid-container > div.tui-grid-content-area.tui-grid-show-lside-area > div.tui-grid-lside-area > div.tui-grid-body-area > div > div.tui-grid-table-container > table > tbody')  # 결과
        customer_data2 = soup.select_one('#__app_root__ > div > div.napy_sub_content > div:nth-child(4) > div.npay_grid_area > div.grid > div.tui-grid-container > div.tui-grid-content-area.tui-grid-show-lside-area > div.tui-grid-rside-area > div.tui-grid-body-area > div > div.tui-grid-table-container > table > tbody')
        createDf(int(total_order),customer_data,customer_data2)

def createDf(length, *args):
    customerList = [[0 for col in range(4)] for row in range(length)]
    cnt = 1  # tr 순서 선택
    pattern = re.compile(r'\s+')
    sleep(2)
    for i in range(length):
        info = args[0].select('tr:nth-child(%d)>td' % cnt)  # 첫번째 tr 선택
        jcnt = 0  # 배열에 넣기 위한 count 증가
        cnt += 1  # 다음 tr 을위해 증가
        for j in info:
            customerList[i][jcnt] = re.sub(pattern,' ',str(j.get_text())).strip() # 배열에 삽입
            jcnt += 1
    df1 = pd.DataFrame(customerList)

    #2nd div
    customerList = [[0 for col in range(60)] for row in range(length)]
    cnt = 1  # tr 순서 선택
    for i in range(length):
        info = args[1].select('tr:nth-child(%d)>td' % cnt)  # 첫번째 tr 선택
        jcnt = 0  # 배열에 넣기 위한 count 증가
        cnt += 1  # 다음 tr 을위해 증가
        for j in info:
            customerList[i][jcnt] = re.sub(pattern,' ',str(j.get_text())).strip() # 배열에 삽입
            jcnt += 1
    df2 = pd.DataFrame(customerList)
    df = pd.concat([df1,df2], axis=1,ignore_index=True)
    column_name = columnname.naverColumnname

    df.columns = column_name
    df = df.drop('del',axis=1)

    createCsv(df)

def createCsv(df):
    df.to_csv(userinfo.path + 'naver.csv', index=True, header=True, na_rep='-', encoding='utf-8-sig')
