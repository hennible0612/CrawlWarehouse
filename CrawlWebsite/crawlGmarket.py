from time import sleep

from bs4 import BeautifulSoup
import userinfo, get_browser
browser = get_browser.get_browser()

browser.get("https://www.esmplus.com/Member/SignIn/LogOn")
browser.find_element_by_id("Id").send_keys(userinfo.gmarket_id)
browser.find_element_by_id("Password").send_keys(userinfo.gmarket_pw)
browser.find_element_by_id("btnLogOn").click()
browser.get('https://www.esmplus.com/Escrow/Order/NewOrder?type=N2&menuCode=TDM105')
html = browser.page_source
soup = BeautifulSoup(html,'html.parser')

sleep(2)
#데이터가져오기
data =soup.select_one('#dataGrid').getText()
print(data)

# -------  크롤된 정보 text에 적기
# f = open("gmarketUserInfo.txt",'w', encoding="utf8")
# f.write(data)
# f.close()
