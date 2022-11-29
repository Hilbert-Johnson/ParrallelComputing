import sys 
sys.path.append("..") 
from common import *

def generate(muliplier):
    data = read_number(datapath)
    data = data*muliplier
    save_number(data, '../../data/random-{}k.txt'.format(30*muliplier))

if __name__ == '__main__':
    generate(10)
    generate(30)