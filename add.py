# Функция add добавляет новую запись
# в словарь birthdays.

def add(birthdays):
    name = input('Введите имя: ')

    if name not in birthdays:
        bday = input('Введите дату рождения(день месяц год): ')
        birthdays[name] = bday
        print('Добавлено: ', name, '-', bday)
        with open('birthdays.txt', 'a') as f:
            f.write(name + ' : ')
            f.write(bday + '\n')
            f.close()
    else:
        print('Такое имя в базе уже есть.', name)
