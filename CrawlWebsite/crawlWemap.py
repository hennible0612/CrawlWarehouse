from time import sleep

from bs4 import BeautifulSoup
from imap_tools import MailBox

import userinfo, get_browser
browser = get_browser.get_browser()

#로그인
browser.get("https://wpartner.wemakeprice.com/login")
browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div[1]/div[1]/input[1]").send_keys(userinfo.wemap_id)
browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div[1]/div[1]/input[2]").send_keys(userinfo.wemap_pw)
browser.find_element_by_id("login").click()

sleep(5)
#인증번호 요청하기
browser.find_element_by_xpath("/html/body/div/div[2]/div[1]/div/div[1]/div[2]/div/div/div/label[1]").click()
browser.find_element_by_xpath('//*[@id="sendAuth"]').click()


sleep(20)
#인증번호
username = userinfo.gmail_id
password = userinfo.gmail_pw
mailbox = MailBox("imap.gmail.com", 993)
mailbox.login(username,password, initial_folder="INBOX")
authNum = 0;

for msg in mailbox.fetch('(FROM no-reply@wemakeprice.com UNSEEN)', limit=10, reverse=True):
    soup = BeautifulSoup(msg.html,"html")
    data1 = soup.select_one('body > div > table > tbody > tr:nth-child(5) > td > table > tbody > tr:nth-child(1) > td:nth-child(3) > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(2) > td:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(2) > strong')
    authNum = data1.getText()

mailbox.logout()

#인증번호 입력
browser.find_element_by_xpath('//*[@id="authCode"]').click()
browser.find_element_by_xpath('//*[@id="authCode"]').send_keys(authNum)
browser.find_element_by_xpath('//*[@id="checkAuth"]').click()

sleep(2)
#알림창 dismiss
notice = browser.switch_to_alert()
notice.dismiss()

# 비밀번호 다음에 변경하기
browser.find_element_by_xpath('//*[@id="reactapp"]/div/div[2]/div/button[2]').click()

#데이터 가져오기
browser.find_element_by_xpath('//*[@id="requestCancelCount"]').click()
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
orderers = soup.select_one('#orderInfoGrid > div.objbox > table > tbody > tr.ev_dhx_web')

