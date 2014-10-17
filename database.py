#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite

class portal(object):

    def __init__(self, db_file):
        self.connection = lite.connect(db_file)
        with self.connection as con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Users(Id INTEGER, Name TEXT);")

    def id_list(self):
        with self.connection as con:
            cur = con.cursor()
            cur.execute("SELECT Id FROM Users")
            ids = cur.fetchall()
        return [id[0] for id in ids]

    def grab(self, id):
        with self.connection as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Users WHERE Id = %s" % str(id))
            row = cur.fetchone()
        return row

    def create(self, user):
        with self.connection as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Users VALUES(?, ?)", (user["id"], user["name"]))
        return self.grab(user["id"])
