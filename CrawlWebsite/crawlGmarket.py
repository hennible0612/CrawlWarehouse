from bs4 import BeautifulSoup
import userinfo, get_browser
browser = get_browser.get_browser()

browser.get("https://www.esmplus.com/Member/SignIn/LogOn")
browser.find_element_by_id("Id").send_keys(userinfo.gmarket_id)
browser.find_element_by_id("Password").send_keys(userinfo.gmarket_pw)
browser.find_element_by_id("btnLogOn").click()
browser.get('https://www.esmplus.com/Escrow/Delivery/Sending?status=1050&type=N&menuCode=TDM111')
html = browser.page_source
soup = BeautifulSoup(html,'html.parser')

#데이터가져오기
firstSeparator =soup.select_one('#dataGrid').getText()
print(firstSeparator)
secondSeparator = soup.select_one('#gridPanel > div:nth-child(2) > div.grid_table_type2.sb-grid-dct').getText()
print(secondSeparator)

browser.quit()
