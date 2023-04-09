import random

a = list(range(int(input("количество элементов списка а: "))))

for i in range(len(a)):
    a[i] = random.randint(1, 10)
print(a)

a_count = list()
for i in range(len(a) -1):
    a_count.append(a[i-1] + a[i] + a[i+1])
a_count.append(a[-2] + a[-1] + a[0])



print(max(a_count))