from bs4 import BeautifulSoup
import userinfo, get_browser

browser = get_browser.get_browser()

#브라우저 로그인
browser.get("https://wing.coupang.com/login")
browser.find_element_by_id("userID").send_keys(userinfo.coupang_id)
browser.find_element_by_id("userPWD").send_keys(userinfo.coupang_pw)
browser.find_element_by_xpath('//*[@id="btnLogin"]').click()


#!!!!! 쿠팡은 따로 테이블이 없음 바로 html 파일 가져오면됨

#주문목록가져오기
browser.get('https://wing.coupang.com/tenants/sfl-portal/delivery/management?deliverStatus=ACCEPT&startDate=2021-09-28&endDate=2021-10-11')
html = browser.page_source
soup = BeautifulSoup(html,'html.parser')

#상품준비중에서 따왔음 나중에 바꿔야함
orderers = soup.select_one('#wing-top-body > div > div.search-table > div > div:nth-child(5) > div').getText()
