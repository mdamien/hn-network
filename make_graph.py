import bs4
import glob
import sys

data = []

for file in glob.glob('data/stories/*'):
    soup = bs4.BeautifulSoup(open(file).read(), 'lxml')
    title = soup.title.text.strip().replace(' | Hacker News', '').replace(';', '').replace('\n', ' ')
    if soup.select('.subtext'):
        for hnuser in soup.select('.hnuser'):
            hnuser = hnuser.text.strip()
            if hnuser:
                data.append([title, hnuser])

data2 = []

for title, hnuser in data:
    count = 0
    for title2, hnuser2 in data:
        if title != title2 and hnuser == hnuser2:
            count += 1
    if count > 1:
        data2.append([title, hnuser])

for title, hnuser in data2:
    count = 0
    for title2, hnuser2 in data2:
        if title == title2 and hnuser != hnuser2:
            count += 1
    if count > 1:
        print("story|"+title, "user|"+hnuser, sep=';')