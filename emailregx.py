#!/usr/bin/env python3
# -*- coding: utf-8 -
# programs takes email and password and add them into list with REGX
import re
import getpass

email_input = input("enter your name:")
pasword = getpass.getpass()

search = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net)", email_input)
email_list = []
pass_list = []

if search != []:
    email_list.append(search)
    pass_list.append(pasword)
    print("email and password added ")
else:
    print("Invaild email and password")

for email in email_list:
    print(email_input + ":" + pasword)
