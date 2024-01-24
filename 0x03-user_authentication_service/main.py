#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth

email = 'bob@bob.com'
password = 'MyPwdOfBob'
auth = Auth()

u = auth.register_user(email, password)
print(u.email)
u.session_id = auth.create_session(email)
print(u.session_id)

auth.destroy_session(u.id)
print(u.session_id)


