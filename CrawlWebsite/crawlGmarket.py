from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

options = Options()
ua = UserAgent()
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')
#browser = webdriver.Chrome(chrome_options=options)
browser = webdriver.Chrome()
browser.get("https://www.esmplus.com/Member/SignIn/LogOn")
browser.find_element_by_id("Id").send_keys("***")
browser.find_element_by_id("Password").send_keys("***")
browser.find_element_by_id("btnLogOn").click()
browser.get('https://www.esmplus.com/Escrow/Delivery/Sending?status=1050&type=N&menuCode=TDM111')
html = browser.page_source
soup = BeautifulSoup(html,'html.parser')

firstSeparator =soup.select_one('#dataGrid').getText()
print(firstSeparator)
secondSeparator = soup.select_one('#gridPanel > div:nth-child(2) > div.grid_table_type2.sb-grid-dct').getText()
print(secondSeparator)

browser.quit()