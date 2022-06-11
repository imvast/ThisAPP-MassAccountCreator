import httpx


class ThisAPP:
    
    def __init__(self) -> None:
        pass
    
    def Create(username, email, firstname):
        username = str(username).replace("\n","")
        headers={
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            #"content-type": "application/json",
            "origin": "https://thisapp.com",
            "referer": "https://thisapp.com/",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.99 Safari/537.36"
        }
        payload={"email": f"{email}", "firstName": f"{firstname}", "lastName": "vast#1337", "username": f"{username}"}
        with httpx.Client() as client:
            req = client.post("https://api.ws.thisapp.so/v1/auth/presignup", json=payload, headers=headers)
            print("[%s] %s" % (req.status_code, username))
            


if __name__ == "__main__":
    email = input("[ ? ] Your Email -> ")
    firstname = input("[ ? ] First Name (any) -> ")
    with open("available.txt") as usersfile:
        for username in usersfile:
            ThisAPP.Create(username, email, firstname)
