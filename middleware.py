import json
import requests
from HTMLParser import HTMLParser
from requests import session
from bs4 import BeautifulSoup
import time
import sys


url = "https://HOST/cas/login"
urlsesson = "https://HOST/wsg/api/public/v8_0/session"

url2 = "https://HOST/wsg/api/public/v8_0/aps/MAC/operational/summary"
url3 = "https://HOST/wsg/api/public/v8_0/aps/MAC/operational/summary"
url4 = "https://HOST/wsg/api/public/v8_0/aps/MAC/operational/summary"
url5 = "https://HOST/wsg/api/public/v8_0/aps/MAC/operational/summary"
url6 = "https://HOST/wsg/api/public/v8_0/aps/MAC/operational/summary"
url7 = "https://HOST/wsg/api/public/v8_0/aps/MAC/operational/summary"
url8 = "https://HOST/wsg/api/public/v8_0/aps/MAC/operational/summary"

headers= {
    'Content-Type':'application/json;charset=UTF-8'
}

data = { "username": "Username",
         "password": "Password",
         "timeZoneUtcOffset": "+00:00"
        }
payload = json.dumps(data)


print(payload)
count = 0
while count < 5:
    with session() as c:
        r = c.get(urlsesson, data=payload,verify=False)
        u = c.post(urlsesson, data=payload ,verify=False)
        r = c.get(urlsesson, data=payload,verify=False)
        q = c.get(url2, data=payload,verify=False)
        w = c.get(url3, data=payload,verify=False)
        e = c.get(url4, data=payload,verify=False)
        r = c.get(url5, data=payload,verify=False)
        t = c.get(url6, data=payload,verify=False)
        y = c.get(url7, data=payload,verify=False)
        u = c.get(url8, data=payload,verify=False)
        time.sleep(10)
        f1=open('/var/www/html/Summary_MAC.json', 'w+')
        f1.write(q.content)
        f1.close()
        f1=open('/var/www/html/Summary_MAC.json', 'w+')
        f1.write(w.content)
        f1.close()
        f1=open('/var/www/html/Summary_MAC.json', 'w+')
        f1.write(e.content)
        f1.close()
        f1=open('/var/www/html/Summary_MAC.json', 'w+')
        f1.write(r.content)
        f1.close()
        f1=open('/var/www/html/Summary_MAC.json', 'w+')
        f1.write(t.content)
        f1.close()
        f1=open('/var/www/html/Summary_MAC.json', 'w+')
        f1.write(y.content)
        f1.close()
        f1=open('/var/www/html/Summary_MAC.json', 'w+')
        f1.write(u.content)
        f1.close()
