def test_1():
    print('函数作为参数')


def main(func):
    func()


if __name__ == '__main__':
    main(test_1)
    print('文件名字是{}'.format(__name__))
