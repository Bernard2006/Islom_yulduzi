import requests
from pprint import pprint as print

def getFalaq_audio():
    url = 'https://api.quran.sutanlab.id/surah/108/1'
    r = requests.get(url)
    res = r.json()
    audio = res['data']['audio']['primary']
    return audio
def getFalaq_audio1():
    url = 'https://api.quran.sutanlab.id/surah/108/2'
    r = requests.get(url)
    res = r.json()
    audio = res['data']['audio']['primary']
    return audio
def getFalaq_audio2():
    url = 'https://api.quran.sutanlab.id/surah/108/3'
    r = requests.get(url)
    res = r.json()
    audio = res['data']['audio']['primary']
    return audio