from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import userinfo

import userinfo, get_browser
browser = get_browser.get_browser()

browser.get("https://spc.tmon.co.kr/member/login?return_url=%2Fdelivery%3Fmain_deal_srl%3D6379453%26main_deal_ti%3Cx%3Etle%3D%26delivery_status%3DAV%26start_date%3D2012.09.20%26end_date%3D2012.09.25%26page%3D3")
browser.find_element_by_id("form_id").send_keys(userinfo.tmon_id)
browser.find_element_by_id("form_password").send_keys(userinfo.tmon_pw)
browser.find_element_by_xpath('//*[@id="content"]/div[1]/form/fieldset/ul/li[7]/button').click()