#todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# гласных букв в тексте.


#Формат вывода:
# Количество букв a - 13
# Количество букв o - 12
# Количество букв e - 11
# .....................
#
vowels=['а','о','э','е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
found=[]
with open ('dump.txt', 'r', encoding='utf-8') as f:
    for line in f:
        for char in line:
            if char in vowels:
                found.append(char)
for i in range(0,len(vowels)):
    print('Количество букв',vowels[i],'-',found.count(vowels[i]))

