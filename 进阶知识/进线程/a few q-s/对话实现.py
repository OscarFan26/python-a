import threading
import queue
import time


q = queue.Queue(maxsize=2)


class QuestionGiver(threading.Thread):
    def __init__(self, cond: threading.Condition):
        super().__init__()
        self.c = cond
        self.s = QuestionSolver(self.c)

    def run(self):
        while (True):
            inp = str(input("ur maths problem >"))
            if inp == "结束":
                return
            q.put(inp)
            self.s.run()
            self.c.acquire()
            


class QuestionSolver(threading.Thread):
    def __init__(self, cond: threading.Condition):
        super().__init__()
        self.c = cond
        

    def run(self):
        self.c.acquire()
        prob = q.get()
        try:
            exec("print({})".format(prob))
        except SyntaxError as e:
            print("error occured: {}".format(e))
        except NameError as e:
            print("error occured: {}".format(e))
        self.c.notify()
        self.c.release()


if __name__ == "__main__":
    c = threading.Condition()
    g = QuestionGiver(c)
    g.start()
