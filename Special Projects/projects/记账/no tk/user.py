# encoding = utf8
import json
import os


class User:
    def __init__(self):
        self.usrn = str
        self.psw = str
        self.data = str
        self.stat = ''

    def get(self):
        with open('user.json', 'r') as fp:
            a = fp.readline()
            fp.close()
        self.data = json.loads(a)

    def search(self, usrn, psw):
        self.get()
        for i in self.data:
            self.usrn = i['Name']
            self.psw = i['Password']
            if self.usrn == usrn and psw == self.psw:
                self.stat = 'pass'
            elif self.usrn == usrn and psw != self.psw:
                self.stat = 'psw x'
            elif self.usrn != usrn and psw != self.psw:
                self.stat = 'none there'

    def new(self, usrn, psw):
        with open('user.json', 'r') as fp:
            a = fp.readline()
            a = a[:-1]
            fp.close()
        os.remove('user.json')
        with open('user.json', 'a+') as u:
            u.write(', ')
            u.write(a)
            di = {"Name": usrn, "Password": psw}
            json.dump(di, u)

