import time

import threading


class BankProc(threading.Thread):
    def __init__(self, name: str, semaphore: threading.Semaphore):
        super().__init__(name="BankProc")
        self.name = name
        self.sem = semaphore
    
    def start(self):
        print("start handle proc: {}".format(self.name))
        time.sleep(2)
        print("end handle proc: {}".format(self.name))
        self.sem.release()
        return


class BankArranger(threading.Thread):
    def __init__(self, number: int, semaphore: threading.Semaphore):
        super().__init__(name="BankArranger")
        self.number = number
        self.sem = semaphore
    
    def start(self):
        for i in range(self.number):
            self.sem.acquire()
            proc = BankProc(i, self.sem)
            proc.start()
            

if __name__ == '__main__':
    sem = threading.Semaphore(5)
    ba = BankArranger(24, sem)
    ba.start()
