import requests
from pprint import pprint
url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/114.json'

def GetAnnos1():
    r = requests.get(url)
    res = r.json()
    fotiha = res['chapter'][0]['text']
    return fotiha
def GetAnnos2():
    r = requests.get(url)
    res = r.json()
    fotiha = res['chapter'][1]['text']
    return fotiha
def GetAnnos3():
    r = requests.get(url)
    res = r.json()
    fotiha = res['chapter'][2]['text']
    return fotiha
def GetAnnos4():
    r = requests.get(url)
    res = r.json()
    fotiha = res['chapter'][3]['text']
    return fotiha
def GetAnnos5():
    r = requests.get(url)
    res = r.json()
    fotiha = res['chapter'][4]['text']
    return fotiha
def GetAnnos6():
    r = requests.get(url)
    res = r.json()
    fotiha = res['chapter'][5]['text']
    return fotiha
