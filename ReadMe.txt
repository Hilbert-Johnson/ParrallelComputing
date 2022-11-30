# README

## Requirements

ubuntu == 20.04
python == 3.7.10
matplotlib == 3.4.2

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
    ├── utils  # misc function
    |   ├── analyse.py  # plot running time
    |   └── generate.py  # generate random array and save in {root}/data/
    ├── common.py  # common utility functions used by all algorithm
    ├── run.sh  # run test demo
```