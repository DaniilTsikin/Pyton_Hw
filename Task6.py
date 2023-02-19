#Задача 2: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, 
#которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.

import random

numberOfCoins = list(range(int(input("количество монет: "))))

for i in range(len(numberOfCoins)):
    numberOfCoins[i] = random.randint(0, 1)
    print(numberOfCoins[i])

countOfOne = 0        #Решка
countOfZero = 0       #Орел
minNeedToFlip = 0
for i in range(len(numberOfCoins)):
    if numberOfCoins[i] == 0:
        countOfOne += 1
    else: countOfZero += 1
if countOfOne <= countOfZero:
    minNeedToFlip = countOfOne
    print(f'Нужно перевернуть монет: {minNeedToFlip}')
elif countOfZero <= countOfOne:
    minNeedToFlip = countOfZero
    print(f'Нужно перевернуть монет: {minNeedToFlip}')



