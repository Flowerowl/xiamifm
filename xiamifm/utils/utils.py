#encoding:utf-8
from __future__ import unicode_literals

import pickle
import io
import os
from os.path import expanduser
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import xmltodict

import requests
import subprocess
from mplayer import Player, CmdPrefix

from core.caesar import caesar
from models.models import Music


HOME_PATH = os.path.join(expanduser("~"), 'xiamifm')
Player.cmd_prefix = CmdPrefix.PAUSING_KEEP
global player


def create_home():
    if not os.path.exists(HOME_PATH):
        os.mkdir(HOME_PATH)


create_home()


def get_playlist(source):
    playlist = []
    tracklist = xmltodict.parse(source)['playList']['trackList']['track']
    for track in tracklist:
        track['url'] = caesar(track['location'])
        playlist.append(Music(track))
    return playlist


def download(url, title):
    filename = os.path.join(HOME_PATH, '%s.mp3' % title)
    raw_data = requests.get(url, cookies=load_cookies('cookies.txt'), stream=True)
    with open(filename, 'wb') as f:
        for chunk in raw_data.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    return filename


def play(filename):
    player = Player(stdout=subprocess.PIPE)
    player.loadfile(filename)


def show_img():
    pass


def save_cookies(requests_cookiejar, filename):
    with open(filename, 'wb') as f:
        pickle.dump(requests_cookiejar, f)


def load_cookies(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
