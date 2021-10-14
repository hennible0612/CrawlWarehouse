

import get_browser
import userinfo
browser = get_browser.get_browser()

browser.get("https://spc.tmon.co.kr/member/login?return_url=%2Fdelivery%3Fmain_deal_srl%3D6379453%26main_deal_ti%3Cx%3Etle%3D%26delivery_status%3DAV%26start_date%3D2012.09.20%26end_date%3D2012.09.25%26page%3D3")
browser.find_element_by_id("form_id").send_keys(userinfo.tmon_id)
browser.find_element_by_id("form_password").send_keys(userinfo.tmon_pw)
browser.find_element_by_xpath('//*[@id="content"]/div[1]/form/fieldset/ul/li[7]/button').click()

# #데이터가져오기
# browser.find_element_by_xpath('//*[@id="summayD1"]').click()
# browser.find_element_by_xpath('//*[@id="searchForm"]/fieldset/table/tbody/tr[1]/td/div[4]/div/label[2]').click()
# browser.find_element_by_xpath('//*[@id="btnSearch"]').click()
# html = browser.page_source
# soup = BeautifulSoup(html, 'html.parser')
# orderers = soup.select_one('#__grid_DeliveryGrid > div.objbox')
