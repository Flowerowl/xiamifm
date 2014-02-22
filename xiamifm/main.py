#encoding:utf-8
from core import commands
from config.config import intro


def main():
    print intro

def listen():
    while 1:
        command = raw_input('> ')
        if command in dir(commands):
            eval('commands.%s' % command)()

if __name__ == '__main__':
    main()
    listen()
