import random



numberOfWatermelons = list(range(int(input("количество арбузов: "))))



for i in range(len(numberOfWatermelons)):
    numberOfWatermelons[i] = int(input("масса арбуза: "))
    print(numberOfWatermelons[i])
    
max = numberOfWatermelons[0]
min = numberOfWatermelons[0]

for i in range(1, len(numberOfWatermelons)):
    if max < numberOfWatermelons[i]:
        max = numberOfWatermelons[i]
    if min > numberOfWatermelons[i]:
        min = numberOfWatermelons[i]

print(f'Самый легкий арбуз: {min}')
print(f'Самый тяжелый арбуз: {max}')

    
