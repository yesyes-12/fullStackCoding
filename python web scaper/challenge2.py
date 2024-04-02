import requests
from bs4 import BeautifulSoup

keywords = [
    "flutter",
    "python",
    "golang",
]

r = requests.get("https://remoteok.com/remote-flutter-jobs", 
                 headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"})

print(r.status_code)
