#encoding:utf-8
from __future__ import print_function, unicode_literals

from utils import get_response, parser


__all__ = ['play', 'pause', 'quit', 'login', 'logout', 'like', 'dislike', 'next']

def play():
    parser.xml_parser(get_response.get_source('http://www.xiami.com/radio/xml/type/8/id/0'))

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
