from Patronymic import Patronymer
import re

names = []
with open('names.txt', encoding='UTF-8') as inf:
    for line in inf.readlines():
        for i in re.findall(r'\b[А-Я]\w+\b', line):
            names.append(i)

p = Patronymer()
for name in names:
    print(name + ' : ' + p.get_patro(name) + ', ' + p.get_patro(name, True))
