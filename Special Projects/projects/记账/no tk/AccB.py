# encoding = utf8
import json
import os


class AccB:
    def __init__(self, name, types, money, use, *description):
        self.name = name
        self.types = types
        self.money = money
        self.use = use
        self.description = description
        self.a = str

    def write(self):
        with open('accountbook.json', 'r') as j:
            self.a = j.readline()
            self.a = self.a[:-1]
            j.close()
        os.remove('accountbook.json')

        with open('accountbook.json', 'a+') as fp:
            fp.write(', ')
            fp.write(self.a)
            data = {'name': self.name, 'types': self.types, 'money': self.money,
                    'use': self.use, 'description': self.description}
            json.dump(data, fp)


    def get(self):
        with open('accountbook.json', 'r') as fp:
            a = fp.readlines()
            fp.close()
        for i in a:
            self.name = i['name']
            self.types = i['types']
            self.money = i['money']
            self.use = i['use']
            self.description = i['description']
            return 'Name: {}, Type: {}, Money: {}, Usage: {}, Description: {};\n'.format(self.name, self.types,
                                                                                      self.money, self.use,
                                                                                      self.description)


