import time
import multiprocessing
import string
from collections import Counter
import os
import sys
from timeit import Timer

pool = multiprocessing.Pool(10)

def byte_counter(bytevalue, filename):
    '''Count number of lines and occurence of byte in file'''
    linecount=0
    bytecount=0
    with open(filename, mode = 'b') as nop:
        byte = nop.read(1)
        while byte:
            if byte == bytevalue:
                bytecount += 1

    return bytecount


def log_result(result):
     result_list.append(result)


def main():
    '''main function for the async operation using thread in multiprocessing module'''
    filename = sys.argv[1]
    bytevalue = input("Enter byte value -> ")
    processes = 10
    pool = multiprocessing.Pool(processes=processes)
    pool.apply_async(byte_counter, args=(bytevalue,filename,), callback = log_result)
    pool.close()
    pool.join()


if __name__ == "__main__":
    t1 = Timer("byte_counter", "from __main__ import byte_counter")
    t2 = Timer("main", "from __main__ import main")
    main()
    print("Single thread time = " + " " + str(t1.timeit()))
    print("Mulitthread thread time = " + " " + str(t2.timeit()))
    

