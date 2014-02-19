#encoding:utf-8
from core.api import RADIO_URL
from utils.get_response import get_source

from config.config import intro, command_list


def main():
    print intro

def play():
    print 'play'

def listen():
    while 1:
        command = raw_input('>')
        if command in command_list:
            eval(command)()

if __name__ == '__main__':
    main()
    listen()
