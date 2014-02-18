#encoding:utf-8
from core.api import RADIO_URL
from utils.get_response import get_source


def main():
    source = get_source(RADIO_URL)
    print source

if __name__ == '__main__':
    main()
