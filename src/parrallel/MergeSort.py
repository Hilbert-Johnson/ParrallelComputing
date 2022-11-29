import sys 
sys.path.append("..") 
from common import *
import time
from multiprocessing import Manager


def merge_sort_multiple(results, array):
  results.append(merge_sort(array))

def merge_multiple(results, array_part_left, array_part_right):
  results.append(merge(array_part_left, array_part_right))

def merge_sort(array):
    array_length = len(array)

    if array_length <= 1:
        return array

    middle_index = int(array_length / 2)
    left = array[0:middle_index]
    right = array[middle_index:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    sorted_list = []

    left = left[:]
    right = right[:]

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))
        elif len(left) > 0:
            sorted_list.append(left.pop(0))
        elif len(right) > 0:
            sorted_list.append(right.pop(0))
    return sorted_list

def parallel_merge_sort(array, process_count):
    step = int(len(array) / process_count)
    manager = Manager()
    results = manager.list()

    with process_pool(process_count) as pool:
        for n in range(process_count):
            if n < process_count - 1:
                chunk = array[n * step:(n + 1) * step]
            else:
                chunk = array[n * step:]
            pool.apply_async(merge_sort_multiple, (results, chunk))

    while len(results) > 1:
        with process_pool(process_count) as pool:
            pool.apply_async(merge_multiple, (results, results.pop(0), results.pop(0)))

    final_sorted_list = results[0]
    return final_sorted_list


if __name__ == '__main__':
    data = read_number(datapath[int(sys.argv[1])])
    worker = int(sys.argv[2])
    size = len(data)
    T1 = time.time()

    print("[MergeSort] create {} process".format(worker))

    parallel_merge_sort(data, worker)

    T2 = time.time()
    print('[MergeSort] running time: %s s' %(T2 - T1))