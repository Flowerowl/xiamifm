#encoding:utf-8
from __future__ import unicode_literals

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import xmltodict

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
    pass


def play(filename):
    pass
