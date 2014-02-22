#encoding:utf-8
from __future__ import print_function, unicode_literals


def load(func):
    def __decorator():
        print ('歌曲列表初始化...')
        func()
        print ('歌曲列表完毕')
    return __decorator

