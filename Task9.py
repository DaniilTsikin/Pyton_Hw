# Требуется вычислить, сколько раз встречается некоторое
#число X в массиве A[1..N]. Пользователь в первой строке вводит
#натуральное число N – количество элементов в массиве. В последующих
#строках записаны N целых чисел Ai
#Последняя строка содержит число X

N = int(input("Введите число N: "))
A = [] #заполним список
for i in range(1, N+1):
    A.append(i)

X = int(input("Введите число X: ")) #пользователь вводит число, количество вхождений которого нужно подсчитать
print(A)
print(f'В массиве А встречается: {A.count(X)} чисел X') #выводим количество вхождений числа X в список A

