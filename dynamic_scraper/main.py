from playwright.sync_api import sync_playwright #sync라고 적는이유는 playwright을 작동시키는 다른방법이 있기때문에 구분
import time
from bs4 import BeautifulSoup 
import csv

p = sync_playwright().start() #playwright 초기화

browser = p.chromium.launch(headless=False) #브라우저 실행(크롬) 기본적으로 headless=True임

page = browser.new_page() #새 창

#page.goto("https://www.wanted.co.kr/") #주소로 이동
page.goto("https://www.wanted.co.kr/search?query=python&tab=position")
#headless모드에서는 브라우저를 볼 수 없음

for x in range(5):
    time.sleep(3)
    page.keyboard.down("End") 

content = page.content() #페이지의 소스코드 가져오기

p.stop() #playwright 종료

soup = BeautifulSoup(content, "html.parser") #html파싱

jobs = soup.find_all("div", class_="JobCard_container__FqChn") #div태그중 class가 JobCard_active__FqChn인것 찾기

job_db = []

for job in jobs:
    link = f"https://www.wanted.co.kr{job.find('a')['href']}" #a태그의 href속성값 가져오기
    title = job.find("strong",class_="JobCard_title__ddkwM").text #strong태그의 class가 JobCard_title__ddkwM인것 가져오기
    company = job.find("span",class_="JobCard_companyName__vZMqJ").text
    reward = job.find("span",class_="JobCard_reward__sdyHn").text
    
    job_info = {"title":title,
                "company":company,
                "reward":reward,
                "link":link,
                }
    job_db.append(job_info)

print((job_db[0]))
print(len(job_db))

#Exporting to CSV
file = open("jobs.csv", "w",encoding="utf-8", newline = "") #파일명, 모드
writter = csv.writer(file)  #csv파일 쓰기
writter.writerow(["Title","Company","Reward","Link"]) #첫줄에 쓰기
for job in job_db:
    writter.writerow(job.values()) #job의 values를 리스트로 변환하여 쓰기