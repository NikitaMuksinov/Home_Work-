#todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.
from idlelib.iomenu import encoding

#Формат вывода:
# Количество букв a - 13
# Количество букв o - 12
# Количество букв e - 11
# .....................
#
vowels = "аеёиоуыэюя"
result = {}
with open('dump.txt', 'r',encoding="utf-8") as file:
    for line in file:
        for char in line:
            if char in vowels:
                result[char] = result.get(char, 0) + 1
print(result)