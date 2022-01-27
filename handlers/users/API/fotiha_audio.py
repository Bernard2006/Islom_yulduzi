import requests
from pprint import pprint as print

#url = f'https://api.quran.sutanlab.id/surah/1/1'


def Getaudio():
    url = 'https://api.quran.sutanlab.id/surah/1/1'
    r = requests.get(url)
    res = r.json()
    audio = res['data']['audio']['primary']
    return audio
def Getaudio1():
    url = 'https://api.quran.sutanlab.id/surah/1/2'
    r = requests.get(url)
    res = r.json()
    audio1 = res['data']['audio']['primary']
    return audio1
def Getaudio2():
    url = 'https://api.quran.sutanlab.id/surah/1/3'
    r = requests.get(url)
    res = r.json()
    audio2 = res['data']['audio']['primary']
    return audio2
def Getaudio3():
    url = 'https://api.quran.sutanlab.id/surah/1/4'
    r = requests.get(url)
    res = r.json()
    audio3 = res['data']['audio']['primary']
    return audio3
def Getaudio4():
    url = 'https://api.quran.sutanlab.id/surah/1/5'
    r = requests.get(url)
    res = r.json()
    audio4 = res['data']['audio']['primary']
    return audio4
def Getaudio5():
    url = 'https://api.quran.sutanlab.id/surah/1/6'
    r = requests.get(url)
    res = r.json()
    audio5 = res['data']['audio']['primary']
    return audio5
def Getaudio6():
    url = 'https://api.quran.sutanlab.id/surah/1/7'
    r = requests.get(url)
    res = r.json()
    audio6 = res['data']['audio']['primary']
    return audio6
