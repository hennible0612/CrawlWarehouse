from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import re
import get_browser, columnname, userinfo
stack = 0

def crawlKakao():
    global stack
    browser = get_browser.get_browser()

    try:
        browser.get("https://accounts.kakao.com/login?continue=https%3A%2F%2Fcomm-auth-web.kakao.com%2Flogin%2Fcheck?hash=F0Y79Vl_q5sqOjQi0y443_XJhBy-wlBxi-XPbAmC4Xs")
        browser.find_element_by_xpath('//*[@id="id_email_2"]').send_keys(userinfo.kakao_id)
        browser.find_element_by_xpath('//*[@id="id_password_3"]').send_keys(userinfo.kakao_pw)
        browser.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button[1]').click()
        print('Kakao 로그인 성공')
        browser.find_element_by_xpath('//*[@id="kakaoServiceLogo"]').click()
        browser.find_element_by_xpath('//*[@id="mArticle"]/div[2]/div[2]/div[1]/button').click()
        browser.find_element_by_xpath('//*[@id="mArticle"]/div/div[2]/wf-view-dashboard-shipping/div/div/ul/li[2]/a/span').click()

        sleep(2)
        """
        wait until browswerloads
        """
    except:
        print("로그인 중 에러")
        # sleep(2)
        while (stack < 3):
            print('로그인 다시시도')
            stack += 1
            browser.close()
            crawlKakao()
            if stack >= 3:
                print('Kakao 로그인 실패')
                return False
                break
    getSoup(browser)

def getSoup(browser):
    # 브라우저 html 받기
    browser.get('https://store-buy-sell.kakao.com/order/shipping?orderSummaryCount=ShippingRequest') #새주문
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    getData(soup)

def getData(soup):
    # 주문 데이터 가져오기
    ordernum = soup.select_one('#liTab1 > a > span') #신규주문
    total_order = re.sub(r'[^0-9]', '', str(ordernum))
    if (int(total_order) == 0):
        print('ESM 주문 0건')
    else:
        print('ESM 총주문 개수는 : ', total_order)
        customer_data = soup.select_one('tbody.sb-grid-results')  # 결과



# #데이터가져오기
# browser.find_element_by_xpath('//*[@id="mArticle"]/div/div[2]/wf-view-dashboard-shipping/div/div/ul/li[2]/a').click()
# html = browser.page_source
# soup = BeautifulSoup(html, 'html.parser')
# orderers = soup.select_one('//*[@id="page-grid-box_AX_tbody"]')
#



