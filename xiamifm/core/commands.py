#encoding:utf-8
from __future__ import print_function, unicode_literals

from termcolor import colored

from utils import response, utils
from core.apis import RADIO_URL
from decorators.decorators import load


__all__ = ['play', 'pause', 'quit', 'login', 'logout', 'like', 'dislike', 'next']

def _playlist():
    return utils.get_playlist(response.get_source(RADIO_URL))

gl_playlist = _playlist()

def _show(music):
    print (colored('title: %s' % music.title, 'red'))
    print (colored('artist: %s' % music.artist, 'red'))
    print (colored('album: %s' % music.album_name, 'red'))
    print (colored('-' * 64, 'yellow'))


def _next():
    global gl_playlist
    if len(gl_playlist) > 0:
        for music in gl_playlist:
            _show(music)
            _play(music.url)
            gl_playlist.pop(0)
            yield
    else:
        gl_playlist = _playlist()
        _next().next()


def _play(url):
    pass


def play():
    next()


def next():
    _next().next()


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
