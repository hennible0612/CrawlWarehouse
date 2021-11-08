from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import re
import get_browser, columnname, userinfo
stack = 0

def crawlTmon():
    # 로그인
    global stack
    browser = get_browser.get_browser()
    try:
        browser.get('https://spc.tmon.co.kr/member/login?return_url=%2F')
        browser.find_element_by_id("form_id").send_keys(userinfo.tmon_id)
        browser.find_element_by_id("form_password").send_keys(userinfo.tmon_pw)
        browser.find_element_by_xpath('//*[@id="content"]/div[1]/form/fieldset/ul/li[7]/button').click()
        print('티몬 로그인 성공')
        sleep(2)
        """
        wait until browser loads
        """
    except:
        print("로그인 중 에러")
        # sleep(2)
        while(stack <3):
            print('로그인 다시시도')
            stack += 1
            browser.close()
            # sleep(2)
            crawlTmon()
            if stack >= 3:
                print('Tmon로그인 실패')
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
    # sleep(4)
    browser.get('https://spc.tmon.co.kr/delivery?deliveryStatus=D1&delay=N') #새주문
    # browser.get('https://www.esmplus.com/Escrow/Delivery/Sending?status=1050&type=N&menuCode=TDM111')  # 완료된주문
    # sleep(2)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # print(soup)
    # sleep(2)
    # Logout(browser)
    getData(soup)
#
def getData(soup):
    # 주문 데이터 가져오기
    # ordernum = soup.select_one('#totalSendingCount > span')  # 주문완료에서 따옴
    ordernum = soup.select_one('#summayD1').get_text() #신규주문
    total_order = re.sub(r'[^0-9]', '', str(ordernum))
    if (int(total_order) == 0):
        print('티몬 주문 0건')
    else:
        print('티몬 총주문 개수는 : ', total_order)
        customer_data = soup.select_one('#__grid_DeliveryGrid > div.objbox > table > tbody')  # 결과
        createDf(customer_data, int(total_order))
#
def createDf(customer_data, length):
    customerList = [[0 for col in range(49)] for row in range(length)]
    cnt = 2  # tr 순서 선택
    pattern = re.compile(r'\s+')
    # sleep(2)
    for i in range(length):
        info = customer_data.select('tr:nth-child(%d)>td' % cnt)  # 첫번째 tr 선택
        jcnt = 0  # 배열에 넣기 위한 count 증가
        cnt += 1  # 다음 tr 을위해 증가
        for j in info:
            customerList[i][jcnt] = re.sub(pattern,' ',str(j.get_text())).strip() # 배열에 삽입
            # print(testList[i][jcnt]) #리스트에 들어간 value들 표시
            jcnt += 1

    column_name = columnname.tmonColumnname
    df = pd.DataFrame(customerList, columns=column_name)
    # df = pd.DataFrame(customerList)
    createCsv(df)
#
def createCsv(df):
    df.to_csv(userinfo.path +'tmon.csv', index=True, header=True, na_rep='-', encoding='utf-8-sig')
