import userinfo, get_browser
browser = get_browser.get_browser()


browser.get("https://accounts.kakao.com/login?continue=https%3A%2F%2Fcomm-auth-web.kakao.com%2Flogin%2Fcheck?hash=F0Y79Vl_q5sqOjQi0y443_XJhBy-wlBxi-XPbAmC4Xs")

browser.find_element_by_xpath('//*[@id="id_email_2"]').send_keys(userinfo.kakao_id)
browser.find_element_by_xpath('//*[@id="id_password_3"]').send_keys(userinfo.kakao_pw)
browser.find_element_by_xpath('//*[@id="login-form"]/fieldset/div[8]/button[1]').click()
browser.find_element_by_xpath('//*[@id="kakaoServiceLogo"]/span').click()
browser.find_element_by_xpath('//*[@id="mArticle"]/div[2]/div[2]/div[1]/button').click()


