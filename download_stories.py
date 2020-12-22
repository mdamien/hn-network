import requests
import bs4
import glob

id = 25505347

while True:
    url = f"https://news.ycombinator.com/item?id={id}"
    print(url)
    resp = requests.get(url)
    open(f"data/stories/{id}", 'w').write(resp.text)
    id -= 1