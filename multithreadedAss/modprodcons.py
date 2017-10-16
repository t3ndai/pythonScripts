#!/usr/bin/env

from random import randrange
from time import sleep
from queue import Queue
from myThread import MyThread
import multiprocessing
from multiprocessing.dummy import Pool as ThreadPool

def writeQ(queue):
    print('producing object for Q...',)
    queue.put('xxx', 1)
    print("size now", queue.qsize())

def readQ(queue):
    val = queue.get(1)
    print('consumed object from Q... size now', queue.qsize())

def writer(queue, loops):
    #for i in range(loops):
    #   writeQ(queue)
    #   sleep(randrange(1, 4))

    #sleep(randrange(1, 4))

    pool = ThreadPool(loops)
    res = pool.map(writeQ, queue)
    return res
    #pool.map(readQ,loops)
    #sleep(randrange(1, 4))
    #pool.close()
    #pool.join()



def reader(queue, loops):
    #for i in range(loops):
    #    readQ(queue)
    #    sleep(randrange(2, 6))

    #pool = multiprocessing.Pool(processes=loops)
    #res =pool.apply_async(readQ, args=(queue,), callback = log_result)
    #return res
    
    pool = ThreadPool(loops)
    res = pool.map(readQ, queue)
    return res

    #pool.map(readQ,loops)
    #sleep(randrange(1, 4))
    #pool.close()
    #pool.join()

def log_result(result):
     result_list.append(result)

funcs = [writer,reader]
nfuncs = range(len(funcs))

def main():
    nloops = randrange(2, 6)
    #number_of_consumers = int(input('enter the number of consumers ->'))
    manager = multiprocessing.Manager()
    q = manager.Queue(32)
    #q = Queue(32)

    
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), \
            funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
    

    
    

    print('all DONE')

if __name__ == '__main__':
    main()