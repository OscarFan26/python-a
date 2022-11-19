import re


def if_start_with_number(put_in):
    a = re.match("[0-9]*", put_in)
    if a.group():
        print(put_in)
        print(a.group())
        print("a key in input:num")
    else:
        print("no key:num")
        print(a)


ask = input("enter sth.\n>>>"
            ">>>")
if_start_with_number(ask)