# encoding: utf-8 #
"""
==========
File Name:              random now!                    
Author:                 Oscar Fan
Date:                   2022/1/13
requirements:                         
==========
"""
import random as r

li = [21, 27, 29, 46, 18]
print('HELLO WELCOME TO THE RANDOM TIME FOR OSCAR FAN\'S BIRTHDAY.')
print('LET\'S SEE WHO WILL BE THE LUCKY MAN.')
print('RANDOM START!')


for i in range(40):
    print('Times: {}, lucky man: {}'.format(1+i, r.choice(li)))

print('Alright! Random is over let\'s see who will be the lucky boy!')
print('Oscar, Please check it out the 26 times of which will be the lucky one!')
print('Good luck.')
