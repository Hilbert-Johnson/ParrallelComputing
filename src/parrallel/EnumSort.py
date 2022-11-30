import sys 
sys.path.append("..") 
from common import *
import time
from multiprocessing import Manager, Pool, Queue


def enumParallel(q, array , i):
    count = 0
    size = len(ret)
    for j in range(size):
        if array[i]>array[j]:
            count += 1
        if array[i]==array[j] and i>j:
            count += 1
    q.put((count,i))


if __name__=='__main__':
    data = read_number(datapath[int(sys.argv[1])])
    worker = int(sys.argv[2])
    size = len(data)
    T1 = time.time()

    q = Manager().Queue()
    ret = [0] * size

    pool = Pool(worker)
    print("[EnumSort] create {} process".format(worker))

    for i in range(size):
        pool.apply_async(enumParallel, (q, data, i,))

    pool.close()
    pool.join()

    for _ in range(size):
        count, i = q.get()
        ret[count] = data[i]

    T2 = time.time()
    print('[EnumSort] running time: %s s' %(T2 - T1))
    save_number(ret, "../out/order6.txt")