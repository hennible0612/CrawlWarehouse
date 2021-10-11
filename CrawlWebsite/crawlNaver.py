from bs4 import BeautifulSoup

import userinfo, get_browser
browser = get_browser.get_browser()

browser.get("https://nid.naver.com/nidlogin.login?url=https%3A%2F%2Fsell.smartstore.naver.com%2F%23%2FnaverLoginCallback%3Furl%3Dhttps%253A%252F%252Fsell.smartstore.naver.com%252F%2523")

browser.find_element_by_xpath('//*[@id="id"]').send_keys(userinfo.naver_id)
browser.find_element_by_xpath('//*[@id="pw"]').send_keys(userinfo.naver_pw)
browser.find_element_by_xpath('//*[@id="log.login"]/span').click()
browser.find_element_by_xpath('//*[@id="new.save"]').click()
#데이터 가져오기
browser.find_element_by_xpath('//*[@id="seller-content"]/ui-view/div/div[2]/div/div[3]/div/div[2]/div[1]/div/ul/li[2]/div[1]/span[2]/a').click()
browser.find_element_by_xpath('//*[@id="__app_root__"]/div/div[2]/div[3]/div[1]/table/tbody/tr[1]/td/div[1]/div[2]/div/ul/li[1]/button').click()
browser.find_element_by_xpath('//*[@id="__app_root__"]/div/div[2]/div[3]/div[2]/button').click()

html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')
orderers = soup.select_one('#__app_root__ > div > div.napy_sub_content > div:nth-child(4) > div.npay_grid_area > div.grid > div.tui-grid-container > div.tui-grid-layer-state > div')

