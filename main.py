#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: github.com/imvast
@Credits: github.com/RuslanUC
@Date: 10-21-2022
"""

# TODO: UI Improvement
# TODO: Add Config Support
# TODO: Finish Async
# TODO: Proxy Support
# TODO: Better Captcha Solver | idrc rn im jus using the decent one lol


import httpx
import asyncio
import random
import string
import os
import time
from colorama import Fore as C
from async_hcaptcha import AioHcaptcha

os.system("clear || cls")


class ThisAPP:
    def __init__(self) -> None:
        pass
    
    def _print(self, content):
        print("%s[%s%s%s]%s %s%s" % (C.LIGHTBLACK_EX, C.RED, time.strftime("%H:%M:%S", time.gmtime()), C.LIGHTBLACK_EX, C.RED, content, C.RESET))
    
    async def Solve_Captcha(self) -> str:
        while True:
            try:
                solver = AioHcaptcha("6123da29-ecad-48e9-a0df-37dbbb7de9cb", "https://thisapp.com",
                                    {"executable_path": "./chromedriver.exe"})
                resp = await solver.solve()
                break
            except KeyboardInterrupt:
                os._exit(0)
            except Exception as e:
                print(e)
        return str(resp)
    

    async def Create(self, username, firstname):
        username = str(username).replace("\n", "")
        self._print("Solving Captcha...")
        captcha = await self.Solve_Captcha()
        self._print(f"Captcha Solved {C.LIGHTBLACK_EX}|{C.RED} {captcha[:35]}")
        #clen = 99 + len(username)
        headers = {
            'authority': 'backend.prod.thisapp.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.6',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://thisapp.com',
            'referer': 'https://thisapp.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }
        payload = {
            "email": f"{''.join(random.choice(string.ascii_lowercase+string.digits) for _ in range(10))}@gmail.com",
            "firstName": f"{firstname}",
            "lastName": "vast#1337",
            "username": f"{username}",
            "hCaptchaToken": f"{captcha}"
        }
        with httpx.Client() as client:
            req = client.post(
                "https://backend.prod.thisapp.com/v1/waitlist/signup", json=payload, headers=headers)
            if 'id' in req.json():
                self._print("%s (%s) | %s" % (req.status_code, req.json()['id'], username))
            else:
                self._print("%s (%s) | %s" % (req.status_code, req.text, username))



if __name__ == "__main__":
    x = str(input(C.RED + f"""
┌┬┐┬ ┬┬┌─┐ 
 │ ├─┤│└─┐ 
 ┴ ┴ ┴┴└─┘{C.LIGHTBLACK_EX}o    
 
[1] Checker
[2] Create
[0] See known issues
[X] Exit

 > """ + C.RESET))
    while True:
        if x == "0":
            input("Current Known Issues:\n - 'duck behind rocks' captcha unavailability\n")
            break
        if x == "1":
            print("integration soon.. for now just run checker.py lol")
            os._exit(0)
        if x == "2":
            break
        if x == "X":
            os._exit(0)
        else:
            break
    
    firstname = input(f"\n{C.LIGHTBLACK_EX}[{C.RED} ? {C.LIGHTBLACK_EX}]{C.RED} First Name (any) ->{C.LIGHTBLACK_EX} ")
    print(f"{C.RESET}")
    try:
        with open("./Input/available.txt") as usersfile:
            for username in usersfile:
                asyncio.get_event_loop().run_until_complete(ThisAPP().Create(username, firstname))
    except KeyboardInterrupt:
        os._exit(0)