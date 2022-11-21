# Hunter Hanson

import requests, bs4


res = requests.get('http://notpurple.com')

try:
    res.raise_for_status()
except Exception as exc:
    print ('There was a problem: %s' % (exc))

notpurplesoup = bs4.BeautifulSoup(res.text, 'html.parser')

titleElem = notpurplesoup.select('title')

linkElem = notpurplesoup.select('a')

print (f"The title of the page is: {titleElem}\nThe following links are on the page:\n{linkElem}")
