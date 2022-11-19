none = True
while none:
    ask1, ask2, ask3, ask4 = ask()
    if_(ask1, ask2, ask3, ask4)


    def ask():
        ask1 = input('请输入您的性别(男生 或 女生)(如输入0，退出程序):')
        ask2 = float(input('请输入您的身高(cm)(如输入0，退出程序):'))
        ask3 = float(input('请输入您的体重(kg)(如输入0，退出程序):'))
        ask4 = int(input('请输入您的年龄:'))
        return ask1, ask2, ask3, ask4


    def if_(ask1, ask2, ask3, ask4):
        if ask1 == '男生':
            print('您的基础代谢为：', (13.7 * ask3) + (5.0 * ask2) - (6.8 * ask4) + 66)
        elif ask1 == '女生':
            print('您的基础代谢为：', (9.6 * ask3) + (5.0 * ask2) - (6.8 * ask4) + 665)
        elif ask1 == 0 or ask4 == 0 or ask3 == 0 or ask2 == 0:
            global none
            none = False
            print('已退出程序！')
        else:
            print('输入错误！\n请输入男生 或 女生！')
