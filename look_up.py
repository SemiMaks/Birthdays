# Функция look_up находит имя
# в словаре birthdays.

def look_up(birthdays):
    # Получить искомое имя
    name = input('Введите имя: ')

    print(birthdays.get(name, 'Такого имени в словаре нет.'))
