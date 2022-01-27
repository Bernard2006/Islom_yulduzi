import requests
from pprint import pprint as print
url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/108.json'

def getKavsar():
    r = requests.get(url)
    res = r.json()
    kavsar = res['chapter'][0]['text']
    return kavsar
def getKavsar1():
    r = requests.get(url)
    res = r.json()
    kavsar = res['chapter'][1]['text']
    return kavsar
def getKavsar2():
    r = requests.get(url)
    res = r.json()
    kavsar = res['chapter'][2]['text']
    return kavsar
