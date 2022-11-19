# -*- encoding = utf-8 -*-
# Author: pc
# Create Time: 2021/4/10 20:19
# Project name: nct lv1.py
# IDE: PyCharm
# File name: 只包含字母和数字的行.py
import re

text = '''1Withflagsloweredtohalf
-staffJohnson said the news of Philip’s death was received "with great sadness"
2andhonoredhismemoryasoneofthelastsurvivors
 to have served in World War II.

"From that conflict, he took an ethic of service that he applied throughout the unprecedented changes of the post-War era," Johnson said, adding: "He helped steer the Royal Family and the monarchy so that it remains an institution indisputably vital to the balance and happiness of our national life."'''

def line_with_words_or_number(put_in):
    a = re.findall("([0-9a-zA-Z]+\n)+", put_in)
    if a:
        print("match result:", a)
    else:
        print("error.")


line_with_words_or_number(text)