import requests
from bs4 import BeautifulSoup
import csv,codecs
res = requests.get('https://agefans.org/rank')
res.encoding = res.apparent_encoding
data = res.text
soup=BeautifulSoup(data, 'html.parser')
content=soup.find_all('div', class_="text-truncate text-left")
content2=soup.find_all('div', class_="img_over_text p-1 text-truncate")
f = open("movie.csv", "w",newline='')
writer = csv.writer(f)
writer.writerow(['id', 'name', 'mark'])
for i in range(len(content)):
    writer.writerow([i,content[i].text,content2[i].text])
f.close()