# 111-111-1111
import re


def if_strict_telephone_num(input):
    """
    :param input:the telephone number
    :return: True/False
            True: strict
            False: not strict
    """
    if re.finditer(re.compile(r"\d{3}-\d{3}-\d{4}"), str(input)):
        print(True)
    else:
        print(False)


ask = str(input("enter phone num: "
                "...-...-...."
                ">>>"))
if_strict_telephone_num(ask)
