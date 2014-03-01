# encoding:utf-8
from __future__ import unicode_literals

import requests

from core.apis import LOGIN_URL, LOGOUT_URL
from cookies import save_cookies

def login(*args):
    pay_load = {'email': args[0], 'password': args[1]}
    response = requests.post(LOGIN_URL, cookies=pay_load)
    save_cookies(response.cookies)
    import pdb;pdb.set_trace()


def logout():
    pass
