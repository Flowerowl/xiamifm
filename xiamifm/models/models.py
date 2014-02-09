#encoding:utf-8
from __future__ import unicode_literals


class Music(dict):
    def __init__(self, **kwargs):
        dict.__init__(self, **kwargs)
        self.__dict__ = self


class User(object):
    pass


music = Music(title='a', artist='b')
print music.title


