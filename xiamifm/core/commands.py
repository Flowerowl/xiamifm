#encoding:utf-8
from __future__ import print_function, unicode_literals

from utils import response, details


__all__ = ['play', 'pause', 'quit', 'login', 'logout', 'like', 'dislike', 'next']

def play():
    print ('歌曲列表初始化...')
    playlist = details.get_playlist(response.get_source('http://www.xiami.com/radio/xml/type/8/id/0'))
    print ('歌曲列表完毕')

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
    pass
