#Задача 4: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите число: "))
m = 1
counOfPower = 0
while m <= n:
    print(counOfPower, end=' ')
    m = m * 2
    counOfPower +=1