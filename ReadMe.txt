# README

## Requirements

ubuntu >= 18.04  
python >= 3.6

## Run

under project root directory:
```shell
cd src/
bash run.sh
```

## Code Tree

```shell
├── data  # input unsorted array 
│   ├── random-30k.txt
│   ├── random-300k.txt
│   └── random-900k.txt
├── out  # output sorted array
│   ├── order1.txt
│   ├── order2.txt
│   ├── order3.txt
│   ├── order4.txt
│   ├── order5.txt
│   └── order6.txt
├── ReadMe.txt
└── src  # source code
    ├── parrallel  # three parrallel sort algorithm
    │   ├── EnumSort.py
    │   ├── MergeSort.py
    │   └── QuickSort.py
    ├── serial  # three serial sort algorithm
    │   ├── EnumSort.py
    │   ├── MergeSort.py
    │   └── QuickSort.py
    ├── utils  # generate random array and save in {root}/data/
    |   └── generate.py
    ├── common.py  # common utility functions used by all algorithm
    ├── run.sh  # run test demo
```