from bs4 import BeautifulSoup
import urllib.request


def extract():
    url = "https://en.wikipedia.org/wiki/Google"
    source = urllib.request.urlopen(url)
    parse = BeautifulSoup(source, "html.parser")
    body = parse.find('div', {'class': 'mw-parser-output'})

    body = parse.find('div', {'class': 'mw-parser-output'})
    file.write(str(body.text))


search = input('type "s" to start , type "e" to exit')
if search == 'e' or search == 'E':
    print("Ending process.")
    exit()
else:
    print("Creating file ")
    file = open('input.txt', 'a+', encoding='utf-8')
    extract()
