# encoding: utf8
import sys

import AccB as b
import user as u


# noinspection PyArgumentList
class AccountBook:
    def __init__(self):
        self.func_choose_answer = str

    def start(self):
        print('--- Welcome to the Account Book System ---')
        print('* 0 - Exit\n* 2 - New\t* 6 - Login')
        a = input('Your Choice: ')
        if a == '6':
            usrn = input('* Enter UserName(enter exit): ')
            if usrn == '':
                self.start()
            psw = input('* Enter Password(enter exit): ')
            if psw == '':
                self.start()
            aaa = u.User()
            aaa.search(usrn, psw)
            if aaa.stat == 'pass':
                print('---* Welcome, {} *---'.format(usrn))
                self.func_choose()
            elif aaa.stat == 'psw x':
                print('Password: Error')
                self.start()
            elif aaa.stat == 'none there':
                print('Account Not Find.')
                self.start()
        elif a == '0':
            sys.exit()
        elif a == '2':
            usrn = input('New UserName: ')
            psw = input('New Password: ')
            again = input('Again:')
            if psw != again:
                print('Password: Not the same')
                self.start()
            else:
                usr = u.User()
                usr.new(usrn, psw)
                self.start()
        else:
            self.error('KeyError', 'Invalid Choice', 'Please reenter')

    def func_choose(self):
        print(' -------- Easy Using --------')
        print('Function:')
        print('1. Create AccB\t2.Look for AccB')
        print('3. Search for AccB\t4. Delete AccB')
        print('5. Clear AccB\t6. Logout\n 0. Exit')
        self.func_choose_answer = input('Enter your choose(Number): ')
        if self.func_choose_answer == '1':
            self.create()
            self.func_choose()
        elif self.func_choose_answer == '2':
            self.see_all()
            self.func_choose()
        elif self.func_choose_answer == '3':
            self.search()
            self.func_choose()
        elif self.func_choose_answer == '4':
            self.delete()
            self.func_choose()
        elif self.func_choose_answer == '5':
            self.clear()
            self.func_choose()
        elif self.func_choose_answer == '6':
            self.logout()
        elif self.func_choose_answer == '0':
            sys.exit()
        else:
            self.error('KeyError', 'Invalid String While Input[FCN]', 'Please reenter')
            self.func_choose()

    def create(self):
        name = input('\n\nEnter name: ')
        if not name:
            self.error('KeyError', 'Invalid String While Input[N]', 'Please reenter')
        types = input('Income(I) or outcome(O): ')
        if types == 'O' or types == 'I':
            pass
        else:
            self.error('KeyError', 'Invalid String While Input[T]', 'Please reenter')
            self.create()
        money = input('How much money? ')
        try:
            int(money)
        except ValueError:
            self.error('KeyError', 'Invalid Integer While Input', 'Please reenter')
            self.create()
        use = input('Use: ')
        if use == '':
            self.error('KeyError', 'Invalid String While Input-- Cannot be NONE', 'Please reenter')
            self.create()
        description = input('Description[Opt]: ')
        if description == '':
            exp = b.AccB(name, types, money, use, None)
            exp.write()
            print(exp.a)
        else:
            exp = b.AccB(name, types, money, use, description)
            exp.write()

    def see_all(self):
        exp = u.User()
        exp.get()

    def search(self):
        pass

    def delete(self):
        pass

    def clear(self):
        pass

    def logout(self):
        pass

    def error(self, erroropt, str1, str2):
        print('\n*************** {} ***************'.format(erroropt))
        print('       {}'.format(str1))
        print('         {}'.format(str2))


a = AccountBook()
a.start()
