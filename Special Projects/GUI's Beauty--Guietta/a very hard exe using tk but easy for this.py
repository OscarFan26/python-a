# encoding: utf-8 #
"""
==========
File Name:              a very hard exe using tk but easy for this                    
Author:                 Oscar Fan
Date:                   2021/11/7
                        
==========
"""
from guietta import _, Gui, Quit

gui = Gui(['Enter numbers:', '__a__', '+', '__b__', ['Calc']],
          ['Result --->', 'result', _, _, _],
          [_, _, _, _, Quit])
with gui.Calc:
    gui.result = float(gui.a) + float(gui.b)
gui.run()
