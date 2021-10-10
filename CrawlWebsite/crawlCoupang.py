from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import userinfo

options = Options()
ua = UserAgent()
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')
#browser = webdriver.Chrome(chrome_options=options)
browser = webdriver.Chrome()
browser.get("https://wing.coupang.com/login")
browser.find_element_by_id("userID").send_keys(userinfo.coupang_id)
browser.find_element_by_id("userPWD").send_keys(userinfo.coupang_pw)
browser.find_element_by_id("btnLogin").click()
# browser.get('https://www.esmplus.com/Escrow/Delivery/Sending?status=1050&type=N&menuCode=TDM111')
# html = browser.page_source
# soup = BeautifulSoup(html,'html.parser')
