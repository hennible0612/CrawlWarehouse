import re
from time import sleep
from bs4 import BeautifulSoup
from imap_tools import MailBox
import get_browser
import userinfo
from selenium.webdriver.common.alert import Alert
import pandas as pd
stack = 0

def crawlEleven():
    global stack
    browser = get_browser.get_browser()
    try:
        browser.get("https://login.11st.co.kr/auth/front/selleroffice/login.tmall?returnURL=https://soffice.11st.co.kr/view/main")
        browser.find_element_by_id("user-id").send_keys(userinfo.eleven_id)
        browser.find_element_by_id("passWord").send_keys(userinfo.eleven_pw)
        browser.find_element_by_id("loginbutton").click()
        sleep(2)
        #인증번호 요청
        #알림창 dismiss
    except:
        print('로그인중 에러')
    else:
        authNum = getauthNum(browser)
        browser.find_element_by_id("auth_num_02").send_keys(authNum)
        browser.find_element_by_xpath('//*[@id="div_otp_wrapper"]/div/button').click()
        getSoup(browser)

def getauthNum(browser):
    browser.find_element_by_xpath('//*[@id="ar-auth_type_list"]/ul/li[2]/div/label').click()
    browser.find_element_by_xpath('//*[@id="div_otp_wrapper"]/button').click()
    sleep(2)
    Alert(browser).dismiss()
    sleep(50)
    mailbox = MailBox("imap.gmail.com", 993)
    mailbox.login(userinfo.gmail_id, userinfo.gmail_pw, initial_folder="INBOX")
    for msg in mailbox.fetch('(FROM admin@11st.co.kr UNSEEN)', limit=10, reverse=True):
        soup = BeautifulSoup(msg.html, "html")
        data1 = soup.find("td", text="인증번호")
        data2 = data1.find_next_sibling("td").get_text()
        data2 = data2.strip("[")
        data2 = data2.strip("]")
        authNum = data2
    mailbox.logout()
    sleep(2)
    return authNum

def getSoup(browser):
    # 브라우저 html 받기
    # 신규주문
    # browser.get('https://soffice.11st.co.kr/view/35930?preViewCode=GOOD202&orgMenuNo=35930')#신규주문
    browser.get('https://soffice.11st.co.kr/view/35930?preViewCode=GOOD401&orgMenuNo=35930') #배송중
    sleep(3)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    getData(soup)

def getData(soup):
    # 주문 데이터 가져오기
    # ordernum = soup.select_one('#contenttabledataGrid')  #배송중에서 따옴
    ordernum = soup.select_one('#subClmCount > li > b:nth-child(1)')  #배송중에서 따옴
    # ordernum = soup.select_one('#liTab1 > a > span') #신규주문
    # total_order = re.sub(r'[^0-9]', '', str(ordernum))
    total_order = ordernum
    print(type(total_order))
    if (int(total_order) == 0):
        print('11번가 주문 0건')
    else:
        print('11번가 총주문 개수는 : ', total_order)
        customer_data = soup.select_one('#contenttabledataGrid')  # 결과
        print(customer_data)
        sleep(4234234234234234)
        createDf(customer_data, int(total_order))
#
def createDf(customer_data, length):
    customerList = [[0 for col in range(62)] for row in range(length)]
    cnt = 1  # tr 순서 선택
    pattern = re.compile(r'\s+')
    sleep(2)
    for i in range(length):
        # div2>div>div3>div 무한한        info = customer_data.select('tr:nth-child(%d)>td' % cnt)  # 첫번째 tr 선택
        info = customer_data.select('div:nth-child(2)>div>div:nth-child(3)>div:nth-child(2)>div>div:nth-child(%d)' % cnt)
        jcnt = 0  # 배열에 넣기 위한 count 증가
        cnt += 1  # 다음 tr 을위해 증가
        for j in info:
            customerList[i][jcnt] = re.sub(pattern,' ',str(j.get_text())).strip() # 배열에 삽입
            jcnt += 1

    # column_name = columnname.esmColumnname
    df = pd.DataFrame(customerList)
    createCsv(df)


def createCsv(df):
    df.to_csv(userinfo.path + 'eleven.csv', index=True, header=True, na_rep='-', encoding='utf-8-sig')
# #인증번호

#

#
#
#




# #데이터 가져오기
# browser.get('https://soffice.11st.co.kr/view/35930?preViewCode=GOOD202&orgMenuNo=35930')
# html = browser.page_source
# soup = BeautifulSoup(html, 'html.parser')
# orderers = soup.select_one('##row0dataGrid > div:nth-child(1)')
