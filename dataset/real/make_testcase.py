import random

num = 1000000
m1 = num // 3
m2 = num // 3 * 2
data = []
for i in range(num):
    data.append(random.randint(1, 10000))
# data[0:m1+1] = sorted(data[0:m1+1])
# data[m1+1:m2+1] = sorted(data[m1+1:m2+1])
data[m2+1:num] = sorted(data[m2+1:num])

with open("1M_partially_sorted_3.txt", 'w') as f:
    f.write(' '.join(map(str, data)))