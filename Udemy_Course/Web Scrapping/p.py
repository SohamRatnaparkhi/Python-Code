import requests
import bs4

r = requests.get("http://books.toscrape.com/index.html")
soup = bs4.BeautifulSoup(r.text, 'lxml')

#text =  r.text()
x = soup.select("h")

print(x[0].getText)
