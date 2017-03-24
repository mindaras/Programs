import urllib.request
from bs4 import BeautifulSoup
import re
import csv
import io

row_list = []
p = 0

class Scraper():
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        row_list = []

        def get_single_item_data(item_url):
            new_list = []
            global row_list
            global p
            r = urllib.request.urlopen(item_url)
            html = r.read()
            parser = "html.parser"
            sp = BeautifulSoup(html, parser)
            for item_name in sp.find_all("h1"):
                new_list.append(item_name.string)
            for text in sp.find_all("p"):
                strong_tag = text.find("strong")
                if strong_tag is None:
                    continue
                if "Talpa:" in strong_tag:
                    # print(strong_tag.string)
                    found = re.findall("\d", str(text))
                    new_list.append("Talpa: " + "".join(found) + "ml")
            for stock in sp.find_all("span", {"id" : "quantityAvailable"}):
                new_list.append("Kiekis: " + stock.string)
            
            row_list.append(new_list)
            p += 1
            print("Pakrauta produktu: {}".format(p))
                
        for tag in sp.find_all("h3"):
            a = tag.find("a")
            url = a.get("href")
            title = a.get("title")
            # print(url)
            # print(title)
            get_single_item_data(url)
        
Scraper('http://selective.lt/lt/51-insight-professional').scrape()

with io.open("Duomenys.csv", "w", encoding='cp1252', errors='replace') as f:
    w = csv.writer(f, delimiter=",")
    for i in row_list:
        w.writerow(i)
    
