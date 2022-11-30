from contextlib import contextmanager
from multiprocessing import Pool

datapath = ['../../data/random-30k.txt', '../../data/random-300k.txt', '../../data/random-900k.txt']

def read_number(filename):
    with open(filename, 'r') as f:
        numbers = f.readline()
    numbers = numbers.split()
    numbers = [int(number) for number in numbers]
    return numbers

def save_number(data, filename):
    data = [str(i) for i in data]
    with open(filename, 'w') as f:
        string = ' '.join(data)
        f.write(string)

def test_sort(raw_data, sorted_data):
    raw_data.sort()
    if raw_data == sorted_data:
        print("sort algorithm runs right!")
    else:
        print("sort algorithm runs wrong!")
        assert(0)

@contextmanager
def process_pool(size):
    pool = Pool(size)
    yield pool
    pool.close()
    pool.join()

if __name__=='__main__':
    test_sort([5,1,-1,1,0,3],[-1,0,1,1,3,5])
    test_sort([5,1,-1,1,0,3],[-1,0,0,1,3,5])