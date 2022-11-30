import matplotlib.pyplot as plt

x = [i for i in range(3)]

quick_y = [0.072, 1.048, 4.739]
quick_y_parallel = [0.057, 0.512, 1.707]

merge_y = [0.147, 1.789, 5.987]
merge_y_parallel = [0.057, 0.489, 1.552]

plt.figure()

l2 = plt.plot(x, merge_y, color='green', marker='o',
              linestyle='solid', label='$MergeSort$')

l4 = plt.plot(x, quick_y, color='orange', marker='s',
              linestyle='solid', label='$QuickSort$')

l3 = plt.plot(x, quick_y_parallel, color='blue', marker='D',
              linestyle='solid', label='$QuickSort(Parrallel)$')

l1 = plt.plot(x, merge_y_parallel, color='red', marker='v', 
              linestyle='solid', label='$MergeSort(Parrallel)$')

plt.xticks(x, ['30k', '300k', '900k'])
plt.grid()
plt.xlabel('Sort Number')
plt.ylabel('Time')
plt.legend(loc='upper left')
plt.savefig('time.pdf', dpi=600)