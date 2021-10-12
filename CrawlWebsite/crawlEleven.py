from time import sleep

from bs4 import BeautifulSoup
from imap_tools import MailBox

import userinfo, get_browser
browser = get_browser.get_browser()


browser.get("https://login.11st.co.kr/auth/front/selleroffice/login.tmall?returnURL=https://soffice.11st.co.kr/view/main")
browser.find_element_by_id("user-id").send_keys(userinfo.eleven_id)
browser.find_element_by_id("passWord").send_keys(userinfo.eleven_pw)
browser.find_element_by_id("loginbutton").click()

sleep(2)
#인증번호 요청
browser.find_element_by_xpath('//*[@id="ar-auth_type_list"]/ul/li[2]/div/label/span').click()
browser.find_element_by_xpath('//*[@id="div_otp_wrapper"]/button').click()

#알림창 종료
sleep(2)
#알림창 dismiss
notice = browser.switch_to_alert()
notice.dismiss()

sleep(40)
#인증번호
username = userinfo.gmail_id
password = userinfo.gmail_pw
mailbox = MailBox("imap.gmail.com", 993)
mailbox.login(username,password, initial_folder="INBOX")
authNum = 0;

for msg in mailbox.fetch('(FROM admin@11st.co.kr UNSEEN)', limit=10, reverse=True):
    soup = BeautifulSoup(msg.html,"html")
    data1 = soup.find("td",text="인증번호")
    data2 = data1.find_next_sibling("td").getText()
    data2 = data2.strip("[")
    data2 = data2.strip("]")
    authNum = data2



mailbox.logout()

browser.find_element_by_id("auth_num_02").send_keys(authNum)
browser.find_element_by_xpath('//*[@id="div_otp_wrapper"]/div/button').click()

#데이터 가져오기
browser.get('https://soffice.11st.co.kr/view/35930?preViewCode=GOOD202&orgMenuNo=35930')
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
orderers = soup.select_one('##row0dataGrid > div:nth-child(1)')
