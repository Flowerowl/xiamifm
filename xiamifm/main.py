#encoding:utf-8
from __future__ import print_function

from termcolor import colored

from core import commands
from config.config import intro


def main():
    print (colored(intro, 'yellow'))


def listen():
    while 1:
        command = raw_input('> ')
        if command in dir(commands):
            eval('commands.%s' % command)()

if __name__ == '__main__':
    main()
    listen()
