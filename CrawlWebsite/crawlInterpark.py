from bs4 import BeautifulSoup

import userinfo, get_browser
browser = get_browser.get_browser()

browser.get("https://seller.interpark.com/login")

browser.find_element_by_id("memId").send_keys(userinfo.interpark_id)
browser.find_element_by_id("memPwd").send_keys(userinfo.interpark_pw)

browser.find_element_by_xpath('//*[@id="frmMemberLogin"]/div[1]/button').click()

#데이터 가져오기
browser.get("https://seller.interpark.com/views/orders/acknowledge?orderSendStep=releasedForShipment")
browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/label/span").click()
browser.find_element_by_xpath('//*[@id="btnSearch"]').click()

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
orderers = soup.select_one('//*[@id="DataGrid"]/div/canvas')



