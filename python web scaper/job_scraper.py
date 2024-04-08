#scraper할때 알아야 할점
#1. 웹사이트 구조 변경->
#2. scraping은 법적으로 모호한 영역, 사이트 정책 존중
import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"
response = requests.get(url)

soup = BeautifulSoup(
    response.content,
    "html.parser",
    )

#jobs = soup.find("section", id="category-2")
#jobs = soup.find("section",class_="jobs") #class_는 python기본함수랑 겹치지 않게하기 위함
#jobs = soup.find("section",class_="jobs").find("li") #첫번째요소 찾아옴
#jobs = soup.find("section",class_="jobs").find_all("li") #전체
jobs = soup.find("section",class_="jobs").find_all("li")[1:-1] #인덱싱,슬라이싱 가능
#print(jobs)

#사이트에서 데이터 추출
"""all_jobs = []
for job in jobs:
    title = job.find("span",class_="title").text
    company, position, region_ = job.find_all("span",class_="company")
    url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
    job_data = {
        "title": title,
        "company": company.text,
        "position": position.text,
        "region": region_.text,
        "url": f"https://weworkremotely.com{url}",
    }
    all_jobs.append(job_data)
    
print(all_jobs)"""

#페이지 스크랩
all_jobs = []
def scrape_page(url):
    print(f"Scrapping {url} ...")
    response = requests.get(url) #페이지 요청
    soup = BeautifulSoup(response.content, "html.parser") #html파싱
    jobs = soup.find("section",class_="jobs").find_all("li")[1:-1]
    
    for job in jobs:
        title = job.find("span",class_="title").text
        company, position, region_ = job.find_all("span",class_="company")
        url = job.find("div", class_="tooltip--flag-logo").next_sibling["href"]
        job_data = {
            "title": title,
            "company": company.text,
            "position": position.text,
            "region": region_.text,
            "url": f"https://weworkremotely.com{url}",
        }
        all_jobs.append(job_data)

def get_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    buttons = len(soup.find("div",class_="pagination").find_all("span", class_="page"))
    return buttons

#main
total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")
for x in range(total_pages):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    scrape_page(url)

print(all_jobs)
