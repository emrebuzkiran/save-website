# save-website
import requests
from bs4 import BeautifulSoup

url = "https://www.apple.com/en"

htmll = requests.get(url).content
soup = BeautifulSoup(htmll,"html.parser")
so = str(soup.prettify())
file = open("source_code.html","w",encoding="utf-8")
file.write(so)
file.close()

