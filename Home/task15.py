# #todo: Дописать игру "Поле чудес"
# Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
# words = ["оператор", "конструкция", "объект"]
# desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "..", ".." ]
# Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
# Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
# в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
# либо победы.
#
# Пример вывода:
#
# "Это слово обозначает наименьшую автономную часть языка программирования"
#
# ▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒
#
# Введите букву: O
#
# O  ▒  ▒  ▒  ▒  ▒  O  ▒
#
#
# Введите букву: Я
#
# Нет такой буквы.
# У вас осталось 9 попыток !
# Введите букву:


import random

words = ["оператор", "конструкция", "объект", "алгоритм", "программа", "переменная"]
desc = ["Это слово обозначает наименьшую автономную часть языка программирования",
        "Последовательность инструкций, выполняемых компьютером",
        "Основной элемент данных в программировании",
        "Последовательность шагов для решения задачи",
        "Набор инструкций, решающих задачу",
        "Место хранения данных в программе"]
attempt = 10

def get_word():
    index = random.randint(0, len(words) - 1)
    return {
        'word': words[index],
        'mystery': ['_'] * len(words[index]),
        'desc': desc[index]
    }

def update_mystery(mystery, word, letter):
    indices = [i for i, char in enumerate(word) if char == letter]
    for i in indices:
        mystery[i] = letter
    return mystery

def play_game(attempt):
    data = get_word()
    print("Добро пожаловать в игру 'Поле Чудес'!")
    while attempt > 0:
        print(f"\nОписание загаднного слова: {data['desc']}")
        print(" ".join(data['mystery']))
        letter = input("Введите букву: ").lower()
        if len(letter) != 1 or not letter.isalpha():
            print("Пожалуйста, введите одну букву.")
            continue
        if letter in data['word']:
            data['mystery'] = update_mystery(data['mystery'], data['word'], letter)
            if '_' not in data['mystery']:
                print("\nВы победили!")
                print(" ".join(data['mystery']))
                return
            print(" ".join(data['mystery']))
        else:
            attempt -= 1
            print(f"\nНеверно! Осталось попыток: {attempt}")
    print("\nВы проиграли! Слово было:", data['word'])

play_game(attempt)
