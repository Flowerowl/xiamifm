#encoding:utf-8
from __future__ import unicode_literals

import pickle
import io
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import xmltodict

import requests
import subprocess
import mplayer

from core.caesar import caesar
from models.models import Music


def get_playlist(source):
    playlist = []
    tracklist = xmltodict.parse(source)['playList']['trackList']['track']
    for track in tracklist:
        track['url'] = caesar(track['location'])
        playlist.append(Music(track))
    return playlist


def download(url):
    raw_data = requests.get(url, cookies=load_cookies('cookies.txt'), stream=True)
    return io.BytesIO(raw_data.content)


def play(data):
    #subprocess.call('mplayer %s' % data)
    p = mplayer.Player()
    p.loadfile(data)
    p.play()
    import pdb;pdb.set_trace()

def show_img():
    pass


def save_cookies(requests_cookiejar, filename):
    with open(filename, 'wb') as f:
        pickle.dump(requests_cookiejar, f)


def load_cookies(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
