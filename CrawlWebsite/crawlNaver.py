import userinfo, get_browser
browser = get_browser.get_browser()


browser.get("https://nid.naver.com/nidlogin.login?url=https%3A%2F%2Fsell.smartstore.naver.com%2F%23%2FnaverLoginCallback%3Furl%3Dhttps%253A%252F%252Fsell.smartstore.naver.com%252F%2523")

browser.find_element_by_xpath('//*[@id="id"]').send_keys(userinfo.naver_id)
browser.find_element_by_xpath('//*[@id="pw"]').send_keys(userinfo.naver_pw)
browser.find_element_by_xpath('//*[@id="log.login"]/span').click()
browser.find_element_by_xpath('//*[@id="new.save"]').click()

