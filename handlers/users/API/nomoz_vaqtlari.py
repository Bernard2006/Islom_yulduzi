import requests

import json
from pprint import pprint


# fajr-bomdod
# dhuhr-peshin
# isha-xufton
# maghrib-shom


def GetFajr(text):
    url = "https://api.pray.zone/v2/times/today.json?city=" + text.lower()
    r = requests.get(url)
    res = r.json()
    bomdod = res['results']['datetime'][0]['times']['Fajr']
    return bomdod


def GetDhuhr(text):
    url = "https://api.pray.zone/v2/times/today.json?city=" + text.lower()
    r = requests.get(url)
    res = r.json()
    peshin = res['results']['datetime'][0]['times']['Dhuhr']
    return peshin


def GetAsr(text):
    url = "https://api.pray.zone/v2/times/today.json?city=" + text.lower()
    r = requests.get(url)
    res = r.json()
    asr = res['results']['datetime'][0]['times']['Asr']
    return asr


def GetMaghrib(text):
    url = "https://api.pray.zone/v2/times/today.json?city=" + text.lower()
    r = requests.get(url)
    res = r.json()
    shom = res['results']['datetime'][0]['times']['Maghrib']
    return shom


def GetIsha(text):
    url = "https://api.pray.zone/v2/times/today.json?city=" + text.lower()
    r = requests.get(url)
    res = r.json()
    isha = res['results']['datetime'][0]['times']['Isha']
    return isha

def GetData(text):
    url = "https://api.pray.zone/v2/times/today.json?city=" + text.lower()
    r = requests.get(url)
    res = r.json()
    data = res['results']['datetime'][0]['date']['gregorian']
    return data
def GetHijriy(text):
    url = "https://api.pray.zone/v2/times/today.json?city=" + text.lower()
    r = requests.get(url)
    res = r.json()
    data = res['results']['datetime'][0]['date']['hijri']
    return data
def GetSunrise(text):
    url = "https://api.pray.zone/v2/times/today.json?city=" + text.lower()
    r = requests.get(url)
    res = r.json()
    data = res['results']['datetime'][0]['times']['Sunrise']
    return data
def GetImsak(text):
    url = "https://api.pray.zone/v2/times/today.json?city=" + text.lower()
    r = requests.get(url)
    res = r.json()
    data = res['results']['datetime'][0]['times']['Imsak']
    return data
