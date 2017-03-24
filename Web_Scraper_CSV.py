import csv
import urllib.request
from bs4 import BeautifulSoup
url_list = []

class Scraper():
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)

        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            url_list.append(url)

news = "https://news.google.com/"
Scraper(news).scrape()

with open("scraper.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    for i in url_list:
        w.writerow([i])
