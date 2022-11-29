import sys 
sys.path.append("..")
from common import *
import time


def enumSort(array):
    size = len(array)
    ret = [0]*size
    for i in range(size):
        count = 0
        for j in range(size):
            if array[i]>array[j]:
                count += 1
            if array[i]==array[j] and i>j:
                count += 1
        ret[count] = array[i]
    return ret


if __name__=='__main__':
    data = read_number(datapath[int(sys.argv[1])])
    size = len(data)

    T1 = time.time()
    data = enumSort(data)
    T2 = time.time()
    print('[EnumSort] running time: %s s' %(T2 - T1))
    save_number(data, "../out/order3.txt")