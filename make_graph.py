import bs4
import glob

data = []

for file in glob.glob('data/stories/*'):
    soup = bs4.BeautifulSoup(open(file).read(), 'lxml')
    title = soup.title.text.strip().replace(' | Hacker News', '').replace(';', '').replace('\n', ' ')
    for hnuser in soup.select('.hnuser'):
        hnuser = hnuser.text.strip()
        if hnuser:
            data.append([title, hnuser])

for title, hnuser in data:
    ok = False
    for title2, hnuser2 in data:
        if title != title2 and hnuser == hnuser2:
            ok = True
            break
    if ok:
        print("story|"+title, "user|"+hnuser, sep=';')