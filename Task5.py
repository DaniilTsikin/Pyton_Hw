#Задача 1. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, 
#а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей,
#а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
#Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза




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

    
