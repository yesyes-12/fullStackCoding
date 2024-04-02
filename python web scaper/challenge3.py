#Code Challenge3
#전체코드를 function으로 만들어보기
#function에 대한 input은 keyword로 flutter, python, nextjs, kotlin로 설정
#function의 output은 csv파일로 저장 (파일명은 keyword로 설정)
from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup 
import csv

"""keyword = ["flutter","python","nextjs","kotlin"]

def job_scraper(keyword):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False) 
    page = browser.new_page() 
    page.goto(f"https://www.wanted.co.kr/search?query={keyword}&tab=position")

    for x in range(5):
        time.sleep(3)
        page.keyboard.down("End") 

    content = page.content()
    p.stop()

    soup = BeautifulSoup(content, "html.parser")
    jobs = soup.find_all("div", class_="JobCard_container__FqChn")
    job_db = []

    for job in jobs:
        link = f"https://www.wanted.co.kr{job.find('a')['href']}" 
        title = job.find("strong",class_="JobCard_title__ddkwM").text
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
    file = open(f"{keyword}_jobs.csv", mode="w",encoding="utf-8", newline = "") #파일명, 모드
    writter = csv.writer(file)
    writter.writerow(["Title","Company","Reward","Link"])"""
    
#객체지향으로 만들어보기
class JobScraper:
    def __init__(self, keyword):
        print(f"{keyword} Scraper Initialized")
        self.keyword = keyword

    def scrape_jobs(self):
        print(f"Scraping {self.keyword} Jobs")
        p = sync_playwright().start()
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"https://www.wanted.co.kr/search?query={self.keyword}&tab=position")

        for x in range(5):
            time.sleep(3)
            page.keyboard.down("End")

        content = page.content()
        p.stop()

        soup = BeautifulSoup(content, "html.parser")
        jobs = soup.find_all("div", class_="JobCard_container__FqChn")
        job_db = []

        for job in jobs:
            link = f"https://www.wanted.co.kr{job.find('a')['href']}"
            title = job.find("strong", class_="JobCard_title__ddkwM").text
            company = job.find("span", class_="JobCard_companyName__vZMqJ").text
            reward = job.find("span", class_="JobCard_reward__sdyHn").text

            job_info = {
                "title": title,
                "company": company,
                "reward": reward,
                "link": link,
            }
            job_db.append(job_info)

        print("Scraping Done")

        # Exporting to CSV
        print("Exporting to CSV")
        file = open(f"{self.keyword}_jobs.csv", mode="w", encoding="utf-8", newline="")
        writer = csv.writer(file)
        writer.writerow(["Title", "Company", "Reward", "Link"])

        for job in job_db:
            writer.writerow([job["title"], job["company"], job["reward"], job["link"]])

        file.close()

# Usage
keyword = ["flutter", "python", "nextjs", "kotlin"]

for kw in keyword:
    scraper = JobScraper(kw)
    scraper.scrape_jobs()