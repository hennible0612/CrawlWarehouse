from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options

def get_browser():
    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    options.add_argument(f'user-agent={userAgent}')
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 1
    })
    browser = webdriver.Chrome(chrome_options=options)

    return browser

