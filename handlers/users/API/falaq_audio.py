import requests

def getAudio1():
    url = f'https://api.quran.sutanlab.id/surah/113/1'
    r = requests.get(url)
    res = r.json()
    audio = res['data']['audio']['primary']
    return audio
def getAudio2():
    url = f'https://api.quran.sutanlab.id/surah/113/2'
    r = requests.get(url)
    res = r.json()
    audio = res['data']['audio']['primary']
    return audio
def getAudio3():
    url = f'https://api.quran.sutanlab.id/surah/113/3'
    r = requests.get(url)
    res = r.json()
    audio = res['data']['audio']['primary']
    return audio
def getAudio4():
    url = f'https://api.quran.sutanlab.id/surah/113/4'
    r = requests.get(url)
    res = r.json()
    audio = res['data']['audio']['primary']
    return audio
def getAudio5():
    url = f'https://api.quran.sutanlab.id/surah/113/5'
    r = requests.get(url)
    res = r.json()
    audio = res['data']['audio']['primary']
    return audio
