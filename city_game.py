from re import match
import random

cities = {}
used = set()
current_char = ''

with open('ru_cities', encoding='UTF-8') as inf:
    for line in inf:
        line = line.strip()
        if cities.get(line[0]):
            cities[line[0]].add(line)
        else:
            cities[line[0]] = {line}

print('Привет! Поиграем в города? Ты начинаешь! (Если надоест, просто введи: \'сдаюсь\')')
print('Назови любой российский город:')
while True:
    if current_char and not cities[current_char]:
        print('Ну и ну! Кажется, городов на эту букву не осталось, а значит, я выиграл!')
        break

    city = input().lower()

    # if current_char:
    #     city = str(random.choice(list(cities[current_char])))
    # else:
    #     city = str(random.choice(list(cities['а'])))
    # print(city.title())

    if city == 'сдаюсь':
        print('Ура, я победил!')
        break

    if current_char and not city.startswith(current_char):
        print('Тебе нужно назвать город, начинающийся с \'{}\'! Попробуй ещё раз:'.format(current_char.upper()))
        continue

    if not match(r'[а-я]+\-*[а-я]+', city):
        print('Что-то я такого города не знаю... Попробуешь ещё раз?')
        continue

    if city in used:
        print('Такой город уже был! Назови другой!')
        continue

    if city in cities[city[0]]:
        used.add(city)
        cities[city[0]].remove(city)
        if city[-1] in cities:
            current_char = city[-1]
        else:
            current_char = city[-2]
        print('Отлично! Мне на \'{}\':'.format(current_char.upper()))
        if not cities[current_char]:
            print('Ну и ну! Кажется, городов на эту букву не осталось, а значит, я проиграл, поздравляю!')
            break
        answer = cities[current_char].pop()
        used.add(answer)
        print(answer.title())
        if answer[-1] in cities:
            current_char = answer[-1]
        else:
            current_char = answer[-2]
        print('Твоя очередь! Тебе на \'{}\':'.format(current_char.upper()))
        continue
    else:
        print('Что-то я такого города не знаю... Попробуешь ещё раз?')
        continue

