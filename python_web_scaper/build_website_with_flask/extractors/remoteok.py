import requests
from bs4 import BeautifulSoup

all_jobs = []

def scrape_jobs(jobs):
  for job in jobs:
    title = job.find("h2").text
    company = job.find("h3").text
    location = job.find("div", class_="location").text
    url = job.find("a")["href"]

    job_data = {
      "title": title,
      "company": company,
      "location": location,
      "link": f"https://remoteok.com{url}"
    }
    all_jobs.append(job_data) 

def extract_remoteok_jobs(keyword):
  print(f"Scrapping {keyword}...")
  url = f"https://remoteok.com/remote-{keyword}-jobs"
  response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"})
  soup = BeautifulSoup(response.text, "html.parser")
  jobs = soup.find("table", id= "jobsboard").find_all("td", class_="company position company_and_position")[1:]

  scrape_jobs(jobs)
  print(all_jobs)
  return all_jobs