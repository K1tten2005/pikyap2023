class Computer:
    def __init__(self, _id, _name, _year, _classroom_id):
        self.id = _id
        self.name = _name
        self.year = _year
        self.classroom_id = _classroom_id

class Classroom:
    def __init__(self, id_number, _classroom_number):
        self.id = id_number
        self.classroom_number = _classroom_number


class ClassroomsComputers:
    def __init__(self, _computer_id, _classroom_id):
        self.computer_id = _computer_id
        self.classroom_id = _classroom_id

# Аудитории
classrooms = [
    Classroom(1, "254л"),
    Classroom(2, "253л"),
    Classroom(3, "306э"),
    Classroom(4, "362"),
    Classroom(5, "107л")
]

# Компьютеры
computers = [
    Computer(1, "Lenovo", 2022, 1),
    Computer(2, "Cisco", 2020, 1),
    Computer(3, "Acer", 2019, 2),
    Computer(4, "Lenovo", 2021, 3),
    Computer(5, "Cisco", 2018, 3),
    Computer(6, "Asus", 2017, 4),
    Computer(7, "Apple", 2020, 5)
]

# Связь многие ко многим
classrooms_computers = [
    ClassroomsComputers(1, 1),
    ClassroomsComputers(2, 1),
    ClassroomsComputers(3, 2),
    ClassroomsComputers(4, 3),
    ClassroomsComputers(5, 3),
    ClassroomsComputers(6, 4),
    ClassroomsComputers(7, 5)
]


def main():

    # Соединение данных один-ко-многим
    one_to_many = [(c.name, c.year, cc.classroom_number)
                   for cc in classrooms
                    for c in computers
                        if c.classroom_id == cc.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(cc.classroom_number, ccs.classroom_id, ccs.computer_id)
                         for cc in classrooms
                         for ccs in classrooms_computers
                         if cc.id == ccs.classroom_id]

    many_to_many = [(c.name, c.year, classroom_name)
                    for classroom_name, classroom_id, computer_id in many_to_many_temp
                    for c in computers if c.id == computer_id]

    #Фирмы компьютеров, заканчивающиеся на 'о', и их аудитории
    print('Запрос 1')
    res_11 = []
    for computer_name, year, classroom_num in one_to_many:
        if computer_name.endswith('o'):
            res_11.append((computer_name, classroom_num))
    print(res_11)
    # средний год создания компьютера в аудитории
    print('\nЗапрос 2')
    res_12 = {}
    for cc in classrooms:
        cc_computers = list(filter(lambda i: i[2] == cc.classroom_number, one_to_many))
        if len(cc_computers) > 0:
            l_books_years = [x for _, x, _ in cc_computers]
            res_12[cc.classroom_number] = int(sum(l_books_years)/len(l_books_years))
    print(sorted(res_12.items(), key=lambda item: item[1]))
    # кабинеты и их компьютеры, начинающиеся с цифры 2
    print('\nЗапрос 3')
    res_13 = {}
    for cc in classrooms:
        if cc.classroom_number[0] == '2':
            cc_computers = list(filter(lambda i: i[2] == cc.classroom_number, many_to_many))
            cc_computers_names = [x for x, _, _ in cc_computers]
            res_13[cc.classroom_number] = cc_computers_names
    print(res_13)

if __name__ == '__main__':
    main()