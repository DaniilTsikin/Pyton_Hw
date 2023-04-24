def read_file(filename):
    with open(filename, 'r') as data:
        data_array = []
        for line in data:
            item = line.replace('\n','').split(sep = ',')
            data_array.append(item)
    return data_array

def write_file(filename, data_array):
    with open(filename, 'w') as data:
        for i in data_array:
            write_element = ', '.join(i)
            data.write(f'{write_element}\n')
        

def add_item(filename, lastname = '', firstname = '', secondname = '', phone = ''):
    data_array = read_file(filename)
    max_id = 0
    for i in range(1, len(data_array)):
        if max_id < int(data_array[i][0]):
            max_id = int(data_array[i][0])
    next_id = max_id + 1
    lastname = input("Фамилия: ")
    firstname = input("Имя: ")
    secondname = input("Отчество: ")
    phone= input("Телефон: ")
    new_item = []
    new_item.append(str(next_id))
    new_item.append(lastname)
    new_item.append(firstname)
    new_item.append(secondname)
    new_item.append(phone)
    data_array.append(new_item)
    write_file(filename, data_array)
    print('Запись добавлена!')

def show_all_item(filename):
    data_array = read_file(filename)
    for i in range(1, len(data_array)):
        print("ID:", data_array[i][0], "Фамилимя:", data_array[i][1], "Имя:", data_array[i][2], "Отчество:", data_array[i][3], "Телефон:", data_array[i][4])

def change_item(filename, lastname = '', firstname = '', secondname = '', phone = ''):
    show_all_item(filename)
    data_array = read_file(filename)
    user_operations = input('Какой ID вы хотите поменять?: ')
    for i in range(1, len(data_array)):
        if data_array[i][0] == str(user_operations):
            print('Введите новые данные')
    needed_id = data_array[i]
    print(needed_id)
    lastname = input("Фамилия: ")
    firstname = input("Имя: ")
    secondname = input("Отчество: ")
    phone= input("Телефон: ")
    new_item = []
    new_item.append(str(i))
    new_item.append(lastname)
    new_item.append(firstname)
    new_item.append(secondname)
    new_item.append(str(phone))
    data_array[i] = new_item
    
    write_file(filename, data_array)

def delete_item(filename):
    show_all_item(filename)
    data_array = read_file(filename)
    user_operations = input('Какой ID вы хотите удалить?: ')
    for i in range(1, len(data_array)):
        if data_array[i][0] == str(user_operations):
            data_array[i] = []
    print('Запись удалена!')
    write_file(filename, data_array)


def menu():

    print('Добро пожаловать в телефонный справочник!')
    print('1 - показать все записи')
    print('2 - добавить запись')
    print('3 - изменить запись')
    print('4 - удалить запись')
    
    user_operations = int(input())

    if user_operations == 1:
        show_all_item(filename)
    elif user_operations == 2:
        add_item(filename)
    elif user_operations == 3:
        change_item(filename)
    elif user_operations == 4:
        delete_item(filename)

filename = 'file.txt'
menu()