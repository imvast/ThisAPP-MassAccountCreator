import threading, random, requests


def check():
    _username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
    _check = requests.post(
        "https://api.ws.thisapp.so/graphql",
        json = {
               "operationName": "CheckUsername",
               "variables": {
                 "input": {
                   "username": _username
                 }
               },
               "query": "query CheckUsername($input: CheckUsernameInput!) {\n  checkUsername(input: $input) {\n    isAvailable\n    __typename\n  }\n}\n"
            },
        headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36",
                "origin": "https://thisapp.com"
            }
    )
    if '"isAvailable":true' in _check.text:
        print(_username, file=open('available.txt'))


while True:
    if threading.active_count() < 500:
        threading.Thread(target=check).start()
