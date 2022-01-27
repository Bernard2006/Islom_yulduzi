from pprint import pprint as print

import requests

url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/112.json'

def getIxlos():
    r = requests.get(url)
    res = r.json()
    ixlos = res['chapter'][0]['text']
    return ixlos
def getIxlos1():
    r = requests.get(url)
    res = r.json()
    ixlos = res['chapter'][1]['text']
    return ixlos
def getIxlos2():
    r = requests.get(url)
    res = r.json()
    ixlos = res['chapter'][2]['text']
    return ixlos
def getIxlos3():
    r = requests.get(url)
    res = r.json()
    ixlos = res['chapter'][3]['text']
    return ixlos