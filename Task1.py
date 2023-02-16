#Задача 1: Найдите сумму цифр трехзначного числа.

n = int(input("Введите трехзначное число"))
 
suma = 0
 
while n > 0:
    digit = n % 10
    suma = suma + digit
    n = n // 10
 
print("Сумма:", suma)