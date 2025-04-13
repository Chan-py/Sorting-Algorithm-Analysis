import random

num = 100000
data = []
left = 0
right = num
for i in range(num):
    if i % 2 == 0:
        data.append(left)
        left += 1
    else:
        data.append(right)
        right -= 1
    # data.append(random.randint(1, 10000))

with open("testcase_lib.txt", 'w') as f:
    f.write(' '.join(map(str, data)))