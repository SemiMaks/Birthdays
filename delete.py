# Функция delete находит и удалфет существующую
# запись в словаре birthdays.

def delete(birthdays):
    # Получить искомое имя.
    name = input('Введите имя, которое хотите удалить: ')

    # Если имя найдено, то удалить эту запись.
    if name in birthdays:
        del birthdays[name]
    else:
        print('Имя не найдено.')
