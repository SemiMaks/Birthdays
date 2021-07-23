# Функция change изменяет запись,
# уже существующую в словаре birtdays.

def change(birthdays):
    # Получить искомое имя.
    name = input('Введите имя, которе хотите изменить: ')

    if name in birthdays:
        # Получить новый день рождения.
        bday = input('Введите новую дату рождения: ')

        # Обновить запись.
        birthdays[name] = bday
    else:
        print('Такого имени нет.')
