

import userinfo, get_browser
browser = get_browser.get_browser()

browser.get("https://seller.interpark.com/login")

browser.find_element_by_id("memId").send_keys(userinfo.interpark_id)
browser.find_element_by_id("memPwd").send_keys(userinfo.interpark_pw)

browser.find_element_by_xpath('//*[@id="frmMemberLogin"]/div[1]/button').click()
#
# browser.get('https://www.esmplus.com/Escrow/Delivery/Sending?status=1050&type=N&menuCode=TDM111')
# html = browser.page_source
# soup = BeautifulSoup(html,'html.parser')