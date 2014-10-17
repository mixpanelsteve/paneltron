#!/user/bin/python
# -*- coding: utf-8 -*-

import users

hello = users.user_manager()
print hello.get_user(1)
print hello.get_user(2)
print hello.num_users()
print hello.id_list()
