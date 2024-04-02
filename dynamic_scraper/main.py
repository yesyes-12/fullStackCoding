from playwright.sync_api import sync_playwright #sync라고 적는이유는 playwright을 작동시키는 다른방법이 있기때문에 구분
import time

p = sync_playwright().start() #playwright 초기화

browser = p.chromium.launch(headless=False) #브라우저 실행(크롬) 기본적으로 headless=True임

page = browser.new_page() #새 창

page.goto("https://www.wanted.co.kr/") #주소로 이동
#headless모드에서는 브라우저를 볼 수 없음
time.sleep(5) #5초간 대기
#page.screenshot(path="screenshot.png") #브라우저 작동확인을 위한 스크린샷

page.click("button.Aside_searchButton__Xhqq3")
#page.locator("Aside_searchButton__Xhqq3")

time.sleep(5)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("python") #검색창에 python입력

time.sleep(5)

page.keyboard.press("Enter") #엔터키 누르기

time.sleep(5)

page.click("a#search_tab_position") #포지션 탭 클릭

time.sleep(5)

page.keyboard.down("End") 
time.sleep(2)
page.keyboard.down("End")
time.sleep(2)
page.keyboard.down("End")
time.sleep(5)

p.stop() #playwright 종료

