import random

num = 2000000
data = []
for i in range(num):
    data.append(random.randint(1, 10000))

with open("testcase3.txt", 'w') as f:
    f.write(' '.join(map(str, data)))