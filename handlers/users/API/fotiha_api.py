import requests
from pprint import pprint
url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/1.json'

def GetFotiha():
    r = requests.get(url)
    res = r.json()
    fotiha = res['chapter'][0]['text']
    return fotiha
def GetFotiha1():
    r = requests.get(url)
    res = r.json()
    fotiha1 = res['chapter'][1]['text']
    return fotiha1
def GetFotiha2():
    r = requests.get(url)
    res = r.json()
    fotiha2 = res['chapter'][2]['text']
    return fotiha2
def GetFotiha3():
    r = requests.get(url)
    res = r.json()
    fotiha3 = res['chapter'][3]['text']
    return fotiha3
def GetFotiha4():
    r = requests.get(url)
    res = r.json()
    fotiha4 = res['chapter'][4]['text']
    return fotiha4
def GetFotiha5():
    r = requests.get(url)
    res = r.json()
    fotiha5 = res['chapter'][5]['text']
    return fotiha5
def GetFotiha6():
    r = requests.get(url)
    res = r.json()
    fotiha6 = res['chapter'][6]['text']
    return fotiha6


