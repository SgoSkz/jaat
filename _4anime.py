#!/usr/bin/env python
import cfscrape
import js2py
import bs4
import re

sources = "https://4anime.to/?s="
headers = {
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
        }
scraper = cfscrape.create_scraper()

# Retrieves all animes found on website
# TODO: add pages
def search(query: str):
    query.replace(" ", "+")
    searchLink = sources + query
    html = scraper.get(searchLink)
    soup = bs4.BeautifulSoup(html.text, 'html5lib')
    results = soup.find_all("div", id="headerDIV_95")
    resultsSpecific = [i.find_all("a")[0] for i in results]
    animes = {i.find_all("div")[0].string: i["href"] for i in resultsSpecific}
    return animes

# Creates an anime object containing the anime's information
class Anime(object):
    name = ""
    base_link = ""
    description = ""
    enumerated_ep = {}

    def __init__(self, link):
        self.base_link = link
        self.base = scraper.get(self.base_link)
        self.html = self.base.text
        self.soup=bs4.BeautifulSoup(self.html, "html5lib")

    def get_info(self):
        if(self.anime_name()):
            print(self.anime_name())
#         if(self.get_desc()):
#             print(self.get_desc())
        if(self.enumerate_episodes()):
            print(self.enumerate_episodes())
    
    def anime_name(self):
        name = self.soup.find_all("p", class_="single-anime-desktop")
        if(not(name)):
            return "Failed to find a name"
        self.name = name[0].string

    def get_desc(self):
        div = self.soup.find_all("div", class_="synopsis")
        if(not(div)):
            return "Failed to find a description"
        p = div[0].find_all("p")
        descList = [p[i].string+"\n" for i in range(1, len(p))]
        self.description = "Description:\n".join(descList)

    def enumerate_episodes(self):
        epUl = self.soup.find_all("ul", class_="episodes")
        if(not(epUl)):
            return "Failed to find any episodes"
        epLi = epUl[0].find_all("li")
        epLinks = [i.find_all("a")[0]["href"] for i in epLi]
        self.enumerated_ep = {num: url for (num, url) in enumerate(epLinks, 1)}


# Retrieves a random anime from 4anime
def random():
    # Get the random anime
    randAnime = scraper.get("https://4anime.to/random")
    # Soup that html 
    souped = bs4.BeautifulSoup(randAnime.text, "html5lib")
    # Narrow results down to the episodes
    epLink = souped.find_all("ul", class_="episodes")[0].find_all("li")[0].find_all("a")[0]["href"]
    epDataSouped = bs4.BeautifulSoup(scraper.get(epLink).text, "html5lib")
    link = epDataSouped.find_all("a", id="titleleft")[0]["href"]
    # Create anime status
    return Anime(link)

# Retrieves episode/video link
def vidLink(epLink):
    link=re.findall("\"(h.*.mp4)\"", scraper.get(epLink).text)
    if(not(link)):
        logFile = open("log", "a")
        logFile.write("No link found")
        logFile.close()
        return "No link found"
    logFile = open("log", "a")
    logFile.write(link[0])
    logFile.close()
    return link[0]

def main():
    print("This isn't the intended use of this file.")

if __name__ == "__main__":
    main()
