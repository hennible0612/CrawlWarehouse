

# import imaplib
# import email
# from email.header import decode_header
# import webbrowser
# import os
#

#
# def clean(text):
#     #폴더 만들기 위해서 이름 깔끔하게
#     return "".join(c if c.isalnum() else "_" for c in text)
#
# # SSL 로 imap4 생성
# imap  = imaplib.IMAP4_SSL("imap.gmail.com") #ssl 인터넷에서 데이터 안전하게 전송하기 위해 프로토콜
# #로그인
# imap.login(username, password)
# imap.select("inbox") #도착한 메일
from urllib.request import urlopen

from imap_tools import MailBox
from bs4 import BeautifulSoup
import nltk

username = "*"
password = '*'
mailbox = MailBox("imap.gmail.com", 993)
mailbox.login(username,password, initial_folder="INBOX")

for msg in mailbox.fetch('(FROM admin@11st.co.kr UNSEEN)', limit=10, reverse=True):
    soup = BeautifulSoup(msg.html,"html")
    data1 = soup.find("td",text="인증번호")
    data2 = data1.find_next_sibling("td").getText()
    data2 = data2.strip("[")
    data2 = data2.strip("]")
    print(data2)


mailbox.logout()
