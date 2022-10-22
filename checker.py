#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: github.com/xtekky
@Author: github.com/imvast
@Date: 10-21-2022
"""

# TODO: Async Conversion


import threading
import random
import requests
import os
from colorama import Fore as C


class This_Checker:
    def check(length=3):
        _username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=int(length)))
        _check = requests.post(
            "https://backend.prod.thisapp.com/graphql",
            json={
                "operationName": "CheckUsername",
                "variables": {
                    "input": {
                        "username": _username
                    }
                },
                "query": "query CheckUsername($input: CheckUsernameInput!) {\n  checkUsername(input: $input) {\n    isAvailable\n    __typename\n  }\n}\n"
            },
            headers={
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36",
                "origin": "https://thisapp.com"
            }
        )
        with open('./Input/available.txt','a') as _available:
            if '"isAvailable":true' in _check.text:
                _available.write('%s\n'%(str(_username)))
                print(f"{C.LIGHTBLACK_EX}[{C.GREEN}+{C.LIGHTBLACK_EX}]{C.GREEN} {_username}{C.RESET}")
        


if __name__ == '__main__':
    length = input("Username length > ")
    try:
        while True:
            if threading.active_count() < 500:
                threading.Thread(target=This_Checker.check(length)).start()
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)