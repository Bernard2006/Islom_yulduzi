import requests
from pprint import pprint as print

#url = f'https://api.quran.sutanlab.id/surah/1/1'


def Getaudio1():
    url = 'https://api.quran.sutanlab.id/surah/112/1'
    r = requests.get(url)
    res = r.json()
    audio = res['data']['audio']['primary']
    return audio

def Getaudio2():
    url = 'https://api.quran.sutanlab.id/surah/112/2'
    r = requests.get(url)
    res = r.json()
    audio = res['data']['audio']['primary']
    return audio

def Getaudio3():
    url = 'https://api.quran.sutanlab.id/surah/112/3'
    r = requests.get(url)
    res = r.json()
    audio = res['data']['audio']['primary']
    return audio

def Getaudio4():
    url = 'https://api.quran.sutanlab.id/surah/112/4'
    r = requests.get(url)
    res = r.json()
    audio = res['data']['audio']['primary']
    return audio
