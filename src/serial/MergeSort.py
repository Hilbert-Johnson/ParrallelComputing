import sys 
sys.path.append("..") 
from common import *
import time


def merge(array, l, m, r):
    n1, n2 = m-l+1, r-m
    L, R = [0]*n1, [0]*n2

    for i in range(0, n1):
        L[i] = array[l + i]
    for j in range(0, n2):
        R[j] = array[m + 1 + j]

    i, j, k = 0, 0, l 

    while i<n1 and j<n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    while i<n1:
        array[k] = L[i]
        i += 1; k += 1
    while j<n2:
        array[k] = R[j]
        j += 1; k += 1

def mergeSort(array, l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(array, l, m)
        mergeSort(array, m+1, r)
        merge(array, l, m, r)
    

if __name__=='__main__':
    data = read_number(datapath[int(sys.argv[1])])
    size = len(data)

    T1 = time.time()
    mergeSort(data, 0, size-1)
    T2 = time.time()
    print('[MergeSort] running time: %s s' %(T2 - T1))