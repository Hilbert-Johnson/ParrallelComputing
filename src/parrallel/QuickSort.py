import sys 
sys.path.append("..") 
from common import *
import random, time, sys
from multiprocessing import Process, Pipe


def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array.pop(random.randint(0, len(array)-1))
    return quicksort([x for x in array if x < pivot]) + [pivot] + quicksort([x for x in array if x >= pivot])

def quicksortParallel(array, conn, procNum):
    if procNum <= 0 or len(array) <= 1:
        conn.send(quicksort(array))
        conn.close()
        return

    pivot = array.pop(random.randint(0, len(array)-1))
    leftSide = [x for x in array if x < pivot]
    rightSide = [x for x in array if x >= pivot]

    pconnLeft, cconnLeft = Pipe()
    leftProc = Process(target=quicksortParallel, args=(leftSide, cconnLeft, procNum-1))

    pconnRight, cconnRight = Pipe()
    rightProc = Process(target=quicksortParallel, args=(rightSide, cconnRight, procNum-1))

    leftProc.start()
    rightProc.start()

    conn.send(pconnLeft.recv() + [pivot] + pconnRight.recv())
    conn.close()

    leftProc.join()
    rightProc.join()


if __name__ == '__main__':
    data = read_number(datapath[int(sys.argv[1])])
    T1 = time.time()

    worker = int(sys.argv[2])
    print("[QuickSort] create {} process".format(worker))
    pconn, cconn = Pipe()
    p = Process(target=quicksortParallel, args=(data, cconn, worker))
    p.start()
    data = pconn.recv()
    p.join()

    T2 = time.time()
    print('[QuickSort] running time: %s s' %(T2 - T1))