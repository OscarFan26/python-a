# encoding: utf-8 #
"""
==========
File Name:              main
Author:                 Oscar Fan
Date:                   2021/11/27

==========
"""
import datetime
import sys
import os
import csv
from datetime import datetime as dt


class Server:
    def __init__(self):
        self.user = User()
        self.accb = Book()
        # ---------------- CAUTION LINE -------------- #
        self.usrn = str
        self.t = str
        self.mt = str
        self.num_for_range = 11

    def init_print(self):
        print('***** Welcome to Oscar\'s Account Book System')
        self.login()

    def login(self):
        print('*** Please Enter Your Account ***')
        print('NOTE: If you don\'t a account, enter 0, else enter 1, exit for 9')
        choice = input('* Choice: ')
        if choice == '1':
            print('NOTE: This is a Sign in Option.')
            print('You can exit by typing 0.')
            choice = input('Choice for exit or not (go on for 1): ')
            if choice == '1':
                self.usrn = input('* Your User Name: ')
                psw = input('* Your Password: ')
                self.user.search(self.usrn, psw)
                if self.user.stat == 'pass':
                    print('Welcome, {}, to AccountBook System. '.format(self.usrn))
                    self.choose_func()
                else:
                    self.error('AccountError', 'No This Account or Password Wrong', 'Please retry.')
                    self.login()
            elif choice == '0':
                self.login()
            else:
                self.error('ChoiceIncorrectError', 'Incorrect Choice', 'Please enter a valid choice number.')
                self.login()
        elif choice == '0':
            print('NOTE: This is a Sign up Option.')
            print('You can exit by typing 0.')
            choice = input('Choice for exit or not (go on for 1): ')
            if choice == '0':
                self.login()
            elif choice == '1':
                new_usrn = input('* Your new User Name: ')
                new_password = input('* Your new Password: ')
                if new_password == '':
                    print('ERROR: PASSWORD!')
                    self.login()
                elif new_usrn == '':
                    print('ERROR: USRN!')
                    self.login()
                elif new_usrn[-1] == ' ':
                    print('ERROR: System does not support space at the last pos of str.')
                    self.login()
                else:
                    self.user.add(new_usrn, new_password)
                    self.usen = new_usrn
                    print('\n* Creating User *\n...')
                    print('$ Complete. Please Login.\n')
                    self.login()
            else:
                self.error('ChoiceIncorrectError', 'Incorrect Choice', 'Please enter a valid choice number.')
                self.login()
        elif choice == '9':
            sys.exit()
        else:
            self.error('ChoiceIncorrectError', 'Incorrect Choice', 'Please enter a valid choice number.')
            self.login()

    def choose_func(self):
        print('----------- AccountBook SYSTEM List. -----------')
        print('$ Choose by typing numbers before the functions.')
        print('==>')
        print('**** (0. Exit) (1. Logout) (2. Create Book) ****')
        print('**** (3. See All Book) (4. Search for Book) ****')
        print('**** (5. Delete A Book) (9. Help for Using) ****')
        ask_choice = input('$ Enter Your Choice: ')
        if ask_choice == '0':
            self.exit()
        elif ask_choice == '1':
            self.logout()
        elif ask_choice == '2':
            self.create()
        elif ask_choice == '3':
            self.see_all()
        elif ask_choice == '4':
            self.search_book()
        elif ask_choice == '5':
            self.delete()
        elif ask_choice == '9':
            self.help()
        else:
            self.error('ChoiceError', 'Invalid Number', 'Please ReEnter.')
            self.choose_func()

    def logout(self):
        choice = input('?- Are you sure to LOGOUT? \n<0 for NO, 1 for YES> \nEnter: ')
        if choice == '0':
            print('\n')
            self.choose_func()
        elif choice == '1':
            print('I- [Logging out... Complete.')
            self.login()

    def exit(self):
        choice = input('Are you sure to exit?(0 for yes, 1 for no) \n?- > ')
        if choice == '0':
            sys.exit()
        elif choice == '1':
            self.choose_func()
        else:
            self.error('ChoiceError', 'Invalid Choice', 'Please Reenter.')
            print('\n\n')
            self.choose_func()

    def create(self):
        print('ADD A NEW ACCOUNT BOOK.')
        print('You can exit by typing 0')
        choice = input('Choice for exit or not (go on for 1): ')
        if choice == '0':
            self.choose_func()
        elif choice == '1':
            print('AccB base Info -----')
            n = input('Enter Book Name: ')
            if n == '':
                print('ERROR: NAME! ')
                self.create()
            u = input('Enter Use: ')
            if u == '':
                print('ERROR: USE! ')
            io = input('Income or Outcome? (enter i/o): ')
            if io == 'i' or io == 'o':
                pass
            else:
                self.error('ValueError', 'Invalid String at pos.', 'Please check it out and reenter!')
                self.create()
            mt = input('Enter MoneyType ($ for 1/￥ for 2) : ')
            if mt == '1' or mt == '2':
                pass
            else:
                self.error('ValueError', 'Invalid String at pos.', 'Please check it out and reenter!')
                self.create()
            m = input('Enter Money (num, no $/￥, eg.: 2000): ')
            try:
                int(m)
            except ValueError:
                self.error('Type Error', 'Invalid num at pos.', 'Please check it out and reenter.')
                self.create()
            note = input('Enter Note for this: ')
            t = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
            self.accb.add(self.usrn, n, u, io, mt, m, note, t)
            self.choose_func()
        else:
            self.error('ChoiceIncorrectError', 'Incorrect Choice',
                       'Please enter a valid choice number.')
            self.choose_func()

    def see_all(self):
        print('I-  Info getting... Alright.!')
        print('-------------------------------'
              '--------------------------------'
              '----- List of Books ------------'
              '--------------------------------'
              '------------------------')
        print('--| Name |--------------------'
              '| Use |-----------------------------------------| In/Out '
              'Come |---| Money |---| Type |---| '
              'Note |------------------| Time |---'
              '----------------')
        self.accb.get()
        for i in self.accb.li:
            if i[0] == self.usrn:
                if i[3] == 'i':
                    if i[4] == '1':
                        print('--| Name: {} |--'
                              '| Use: {} |--| In/Out come: {} |----| Money: {} |-------| Type:{} |--| Note: '
                              '{} |---| Time: {} |-------'
                              '----'.format(i[1], i[2], 'Income', i[5], '$', i[6], i[7]))
                    else:
                        print('--| Name: {} |--'
                              '| Use: {} |--| In/Out come: {} |----| Money: {} |-------| Type:{} |--| Note: '
                              '{} |---| Time: {} |-------'
                              '----'.format(i[1], i[2], 'Income', i[5], '￥', i[6], i[7]))
                if i[3] == 'o':
                    if i[4] == '1':
                        print('--| Name: {} |--'
                              '| Use: {} |--| In/Out come: {} |----| Money: {} |-------| Type:{} |--| Note: '
                              '{} |---| Time: {} |-------'
                              '----'.format(i[1], i[2], 'Outcome', i[5], '$', i[6], i[7]))
                    else:
                        print('--| Name: {} |--'
                              '| Use: {} |--| In/Out come: {} |----| Money: {} |-------| Type:{} |--| Note: '
                              '{} |---| Time: {} |-------'
                              '----'.format(i[1], i[2], 'Outcome', i[5], '￥', i[6], i[7]))
        self.choose_func()

    def search_book(self):
        print('----- Search Session -----')
        print('* Enter Book Name to Search:')
        self.accb.search()
        num_for_range = 11
        print('[Maybe you mean:')
        if len(self.accb.li) < 11:
            num_for_range = len(self.accb.li)
        for i in range(num_for_range):
            if i == 0:
                pass
            else:
                print(self.accb.li[i][1], '; ', end=' ')
        print(']')
        name = input('Input Name HERE> ')
        if name == '':
            self.error('NameError', 'Invalid Search value <Name>', 'Please check your spelling.')
            self.choose_func()
        stat = ''
        print('SEARCHing...')
        for j in self.accb.li:
            if j[1] == name:
                print('*'*50)
                print('Name: {}'.format(j[1]))
                print('Use: {}'.format(j[2]))
                if j[3] == 'i':
                    print('CCD: Income')
                else:
                    print('CCD: Outcome')
                if j[4] == 1:
                    print('Money: {} $'.format(j[5]))
                else:
                    print('Money: {} ￥'.format(j[5]))
                print('Note: {}'.format(j[6]))
                print('Time Edit: {}'.format(j[7]))
                print('*'*50, '\n')
                stat = 'g'
        if stat != 'g':
            print('Not Found Any record. Please check your name if you miss enter the name.')
        self.choose_func()

    def delete(self):
        pass

    def help(self):
        print('I- [Help of Using -- AccountBookSystem ---]')
        print('   [You can TYPE numbers of the functions ')
        print('    which is before the functions.')
        print('    TYPE 0 refers to exit this system and shutdown.')
        print('    TYPE 1 refers to LOGOUT THIS ACCOUNT ')
        print('           and come back to login window.')
        print('    TYPE 2 refers to CREATE A NEW ACCOUNT BOOK')
        print('           and you need to enter some info about it.')
        print('    TYPE 3 refers to SEE ALL ACCOUNT BOOKS that you')
        print('           have right now.')
        print('    TYPE 4 refers to SEARCH FOR A ACCOUNT BOOK.')
        print('           (ONLY BY NAME! )')
        print('    TYPE 5 refers to DELETE A ACCOUNT BOOK.')
        print('    TYPE 9 refers to HELP PAGE, which is this page.]')
        print('   [Enter any Key to continue.]]')
        choice = input('?- Input: ')
        self.choose_func()

    def error(self, error_name: str, error_info1: str, error_info2: str):
        print('\n\n')
        print('****** {} ******'.format(error_name))
        print('**     {}     **'.format(error_info1))
        print('*   {}   *'.format(error_info2))
        print('\n')


class User:
    def __init__(self):
        self.usrname = str
        self.psw = str
        self.txt = str
        self.stat = str

    def add(self, usrn, psw):
        with open('users.csv', 'a+', newline='') as fp:
            fp.write('\n')
            obj = csv.writer(fp)
            obj.writerows([[usrn, psw]])
            fp.close()

    def search(self, usrn, psw):
        with open('users.csv', 'r+') as fp:
            data = csv.DictReader(fp)
            for i in data:
                if i['U'] == usrn and i['P'] == psw:
                    self.stat = 'pass'
                    break
                else:
                    continue
            fp.close()


class Book:
    def __init__(self):
        self.li = []
        self.belongings = str
        self.name = str
        self.use = str
        self.income_or_outcome = str
        self.money_type = str
        self.money = str
        self.note = str
        self.time = str

    def add(self, b, n, u, io, mt, m, note, t):
        with open('accb.csv', 'a+', newline='') as fp:
            fp.write('\n')
            obj = csv.writer(fp)
            obj.writerow([b, n, u, io, mt, m, note, t])
            fp.close()

    def del_book(self):
        pass

    def search(self):
        with open('accb.csv', 'r+') as fp:
            obj = csv.reader(fp)
            for rows in obj:
                if rows == []:
                    pass
                else:
                    self.li.append(rows)

    def get(self):
        with open('accb.csv', 'r+') as fp:
            obj = csv.reader(fp)
            for i in obj:
                self.li.append(i)


if __name__ == '__main__':
    oscar = Server()
    oscar.init_print()
else:
    pass
