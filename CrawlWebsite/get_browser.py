from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_browser():
    options = Options()
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
    options.add_argument('user-agent='+ user_agent)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # options.add_argument('headless') #headless
    browser = webdriver.Chrome(chrome_options=options)
    #firefox = webdriver.Firefox()
    return browser


    # options = Options()
    # ua = UserAgent()
    # userAgent = ua.random
    # options.add_argument(f'user-agent={userAgent}')
    # options.add_experimental_option("prefs", {
    #     "profile.default_content_setting_values.notifications": 1
    # })
    # browser = webdriver.Chrome(chrome_options=options)
    # #firefox = webdriver.Firefox()
    # return browser
