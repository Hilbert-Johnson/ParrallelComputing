import sys 
sys.path.append("..") 
from common import *
import time


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i+1], array[high]) = (array[high], array[i+1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi-1)
        quickSort(array, pi+1, high)


if __name__=='__main__':
    data = read_number(datapath[int(sys.argv[1])])
    size = len(data)

    T1 = time.time()
    quickSort(data, 0, size-1)
    T2 = time.time()
    print('[QuickSort] running time: %s s' %(T2 - T1))