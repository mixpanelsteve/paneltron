#!/usr/bin/python
# -*- coding: utf-8 -*-

import database

class user(object):

    def __init__(self, name, created):
        self.name = name
        self.created = created

    def create_user_properties(self):
        pass

    def get_user_properties(self):
        pass

class user_manager(object):

    def __init__(self):
        self.data = database.portal('userlist.db')

    def id_list(self):
        return self.data.id_list()

    def num_users(self):
        return len(self.id_list())

    def get_user(self, id):
        user = self.data.grab(id)
        return user if user else self.make_user(id)

    def make_user(self, id, props = {'name':'steve'}):
        props.update({'id':id})
        return self.data.create(props)
