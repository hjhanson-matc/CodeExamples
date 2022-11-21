# Hunter Hanson

import requests

res = requests.get('http://notpurple.com')

try:
    res.raise_for_status()
except Exception as exc:
    print ('There was a problem: %s' % (exc))

html = open('my_web_file.html', 'wb')

for chunk in res.iter_content(10000):
    html.write(chunk)

html.close()
