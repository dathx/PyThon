import requests
import bs4

result = requests.get("https://www.facebook.com")
type(result)
# print(result.text)

soup = bs4.BeautifulSoup(result.text,"lxml")
# print(soup)
print(soup.select('title')[0].getText())

print(soup.select('h2'))

print(soup.select('img')[0])
print(soup.select('img'))

