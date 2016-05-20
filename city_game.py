from collections import defaultdict

cities = defaultdict(set)  # Словарь с городами: 'первая буква' : {set городов на эту букву}
used = set()  # Множество уже названных городов
current_char = ''  # Буква, с которой должен начинаться следующий город

with open('ru_cities', encoding='UTF-8') as inf:  # Чтение городов из файла
    for line in inf:
        cities[line[0]].add(line.rstrip())  # Добавление города в словарь

print('Привет! Поиграем в города? Ты начинаешь! (Если надоест, просто введи: \'сдаюсь\')')
print('Назови любой российский город:')
while True:
    city = input().lower()  # Ввод города пользователем

    if city == 'сдаюсь':  # Условие выхода игрока
        print('Ура, я победил!')
        break

    if current_char and not city.startswith(current_char):  # Если город начинается не с той буквы
        print('Тебе нужно назвать город, начинающийся с \'{}\'! Попробуй ещё раз:'.format(current_char.upper()))
        continue

    if city in used:  # Проверка повторения городов
        print('Такой город уже был! Назови другой!')
        continue

    if city[0] not in cities or city not in cities[city[0]]:  # Если город не найден в списке, ввести повторно
        print('Что-то я такого города не знаю... Попробуешь ещё раз?')
    else:  # Город введён корректно
        used.add(city)
        cities[city[0]].remove(city)
        if city[-1] in cities:  # Последняя или предпоследняя буква города становится новой первой буквой
            current_char = city[-1]
        else:
            current_char = city[-2]
        # Формирование ответа от компьютера:
        print('Отлично! Мне на \'{}\':'.format(current_char.upper()))
        if not cities[current_char]:  # Условие победы игрока
            print('Ну и ну! Кажется, городов на букву \'{}\' не осталось, а значит, я проиграл, поздравляю!'.format(current_char.upper()))
            break
        answer = cities[current_char].pop()  # Вабор ответа
        used.add(answer)
        print(answer.title())
        if answer[-1] in cities:  # Ответ получен и задаётся новая первая буква
            current_char = answer[-1]
        else:
            current_char = answer[-2]
        print('Твоя очередь! Тебе на \'{}\':'.format(current_char.upper()))

    if current_char and not cities[current_char]:  # Условие победы компьютера
        print('Ну и ну! Кажется, городов на букву \'{}\' не осталось, а значит, я победил!'.format(current_char.upper()))
        break
