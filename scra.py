from bs4 import BeautifulSoup
import requests
import csv

def main():
    csvw = csv.writer(open('heise-https.csv', 'w'), delimiter = ';')
    request = requests.get("https://www.heise.de/thema/https")
    data = request.content
    bsoup= BeautifulSoup(data, "lxml")
    content = bsoup.findAll("div", "recommendation")
    #goes over lines from text and retrieve headers
    for c in content:
        c = c.find("header")
        b = c.string.strip()
        # Looks if the header contains the keyword
        if "https" in b or "HTTPS" in b:
            csvw.writerow([b.encode("utf-8")])

if __name__ == '__main__':
    main()
