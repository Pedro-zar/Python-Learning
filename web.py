import bs4
import lxml
import requests

result = requests.get("https://pt.wikipedia.org/wiki/Inteligência_artificial")
soup = bs4.BeautifulSoup(result.text, "lxml")

print(soup.select("title")[0].getText())
