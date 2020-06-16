import requests
from bs4 import BeautifulSoup


class WebScrap:
    Wiki = requests.get("https://en.wikipedia.org/wiki/Deep_learning");
    parsed = BeautifulSoup(Wiki.content, "html.parser")

    def Title(self):
        title = self.parsed.title.string
        return title

    def getlinks(self):
        list =[]
        for link in self.parsed.find_all('a'):
            list.append(link.get('href'))
        return list


test = WebScrap()
print(test.Title())
print(test.getlinks())
