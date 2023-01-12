import threading
threading.Semaphore
threading.Lock
# 通过condition实现通话

class Server(threading.Thread):
    def __init__(self, condition: threading.Condition) -> None:
        super().__init__(name="server")
        self.condition = condition
            
    def run(self):
        with self.condition:
            self.condition.wait()
            print(self.name, "try2: <--- ack")
            self.condition.notify()
            self.condition.wait()
            print(self.name, "suc: don")
            self.condition.notify()

class Client(threading.Thread):
    def __init__(self, condition: threading.Condition) -> None:
        super().__init__(name="client")
        self.condition = condition
    
    def run(self):
        with self.condition: 
            print(self.name, "try1: ---> seq ")
            self.condition.notify()
            self.condition.wait()
            
            
            print(self.name, "try3: ---> seq+ack")
            self.condition.notify()
            self.condition.wait()
            
            
            print(self.name, "suc: don")
            self.condition.notify()
            # self.condition.wait()
            


cl = threading.Condition()
client = Client(cl)
server = Server(cl)
server.start()
client.start()

# test like me