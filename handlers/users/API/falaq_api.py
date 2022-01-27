import requests
from pprint import pprint as print
url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/113.json'

def getfalaq1():
    r = requests.get(url)
    res = r.json()
    fotiha = res['chapter'][0]['text']
    return fotiha
def getfalaq2():
    r = requests.get(url)
    res = r.json()
    fotiha = res['chapter'][1]['text']
    return fotiha
def getfalaq3():
    r = requests.get(url)
    res = r.json()
    fotiha = res['chapter'][2]['text']
    return fotiha
def getfalaq4():
    r = requests.get(url)
    res = r.json()
    fotiha = res['chapter'][3]['text']
    return fotiha
def getfalaq5():
    r = requests.get(url)
    res = r.json()
    fotiha = res['chapter'][4]['text']
    return fotiha