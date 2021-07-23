# Функция add добавляет новую запись
# в словарь birthdays.

def add(birthdays):
    name = input('Введите имя: ')

    if name not in birthdays:
        bday = input('Введите дату рождения(день месяц год): ')
        birthdays[name] = bday
        print('Добавлено: ', name, '-', bday)
    else:
        print('Такое имя в базе уже есть.', name)
