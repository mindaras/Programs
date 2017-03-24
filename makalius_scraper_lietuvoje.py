import urllib.request
from bs4 import BeautifulSoup
import csv

name_list = []
price_list = []
link_list = []

class Scraper():
    def __init__(self, site):
        self.site = site

    def scrape(self):
        global name_list
        global price_list
        new_list = []
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)

        for tag in sp.find_all("div", {"class": "location pull-left"}, ):
            strong = tag.find("strong")
            name_list.append(strong.string)
            
        for tag in sp.find_all("div", {"class": "price text-center pull-left"}):
            strong = tag.find("strong")
            price_list.append(strong.string)

        for tag in sp.find_all("a", {"class": "link"}):
            href = tag.get("href")
            link_list.append(href)

for i in range (1, 18):
    makalius = "http://www.makalius.lt/poilsis-lietuvoje/puslapis/" + str(i)
    Scraper(makalius).scrape()

with open("Keliones.csv", "w", encoding="cp1252", errors="replace") as f:
    w = csv.writer(f, delimiter=",")
    for a, b, c in zip(name_list, price_list, link_list):
        w.writerow([a, b, c])


