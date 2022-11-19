# encoding: utf-8 #
"""
==========
File Name:              main                    
Author:                 Oscar Fan
Date:                   2022/2/27
requirements:                         
==========
"""
import sys
import time
#
#
# def progress_bar():
#     for i in range(1, 101):
#         print("\r", end="")
#         print("Download progress: {}%: ".format(i), "▋" * (i // 2), end="")
#         sys.stdout.flush()
#         time.sleep(0.05)
#
# if __name__ == '__main__':
#     progress_bar()
from progressbar import *

print("\033[0;36;1m正在复制文件”main.cpp“从”WSL Console“到”桌面“······\033[0m")
widgets = ["进度：", Percentage(), Bar("▓"), " ",  ETA(), " ",
           FileTransferSpeed()]
progress = ProgressBar(widgets=widgets)
things = ["#include <iostream>", 'using namespace std;', 'int main(){',
          '    cout << "Hello World! "<< endl;', '    return 0;', '}']


with open("main.cpp", "w") as fp:
    for i in progress(range(6)):
        sys.stdout.flush()
        fp.write(things[i]+"\n")
        time.sleep(0.6)
    fp.close()
print("\033[0;36;1m完成！ \033[0m")
