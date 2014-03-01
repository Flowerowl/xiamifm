# encoding:utf-8
from __future__ import unicode_literals

import sqlite3


class DB(object):
    def __init__(self):
        self.con = sqlite3.connect('cookies.db')
        self.cur = self.con.cursor()

    def create(self):
        sql = 'create table if not exists cookies(cookies text)'
        self.cur.execute(sql)
        self.con.commit()

    def select(self):
        sql = 'select cookies from cookies'
        self.con.commit()
        return self.cur.fetchone()

    def insert(self, context):
        sql = 'insert into cookies values("%s")' % context
        self.con.commit()

    def __del__(self):
        self.con.close()


def save_cookies(cookies):
    db = DB()
    db.create()
    db.insert(cookies)


def get_cookies():
    db = db()
    return db.select()

