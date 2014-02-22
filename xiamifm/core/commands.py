#encoding:utf-8
from __future__ import print_function, unicode_literals

from termcolor import colored

from utils import response, details
from core.apis import RADIO_URL
from decorators.decorators import load


__all__ = ['play', 'pause', 'quit', 'login', 'logout', 'like', 'dislike', 'next']

def _playlist():
    playlist = details.get_playlist(response.get_source(RADIO_URL))
    for music in playlist:
        yield music

def _show(music):
    print (colored('title: %s' % music.title, 'red'))
    print (colored('artist: %s' % music.artist, 'red'))
    print (colored('album: %s' % music.album_name, 'red'))
    print (colored('-' * 64, 'yellow'))

def play():
    next()

def pause():
    pass

def quit():
    pass

def login():
    pass

def logout():
    pass

def like():
    pass

def dislike():
    pass

def next():
    music = _playlist().next()
    _show(music)
