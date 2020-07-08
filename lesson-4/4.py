from collections import Counter
old_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
counter = Counter(old_list)
single = [x for x,n in counter.items() if n==1]
print(single)