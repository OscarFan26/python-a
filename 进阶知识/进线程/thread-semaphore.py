import threading
import time

class HtmlSpider(threading.Thread):
    def __init__(self, url: str, sem: threading.Semaphore):
        super().__init__()
        self.url = url
        self.sem = sem
    
    def run(self):
        time.sleep(2)
        print("suc")
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self, sem: threading.Semaphore):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            html_spider = HtmlSpider("https://baidu.com/{}".format(i), self.sem)
            html_spider.start()
            


if __name__ == "__main__":
    sem = threading.Semaphore(3)
    urlp = UrlProducer(sem)
    urlp.start()
