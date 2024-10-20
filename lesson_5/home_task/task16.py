# todo: База данных пользователя.
# Задан массив объектов пользователя


users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]

# Написать фильтр который будет выводить отсортированные объекты по возрасту(больше введеного)
# ,первой букве логина, и заданной группе.
#
# #Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе
#
# тип сортировки: 1
#
# #Затем сообщение для ввода
# Ввидите критерии поиска: 16

# Результат:
#Пользователь: 'Piter' возраст 23 года , группа  "admin"
#Пользователь: 'Dasha' возраст 30 лет , группа  "master"

def sort_login(a):
    return a['login']
def sort_age(a):
    return a['age']
def sort_group(a):
    return a['group']


def user_filter(users,sort_type,criteriy):
    if sort_type == 1:
        user_filter=[filter for filter in users if filter['login']==criteriy]
        user_filter.sort(key=sort_login)
    if sort_type == 2:
        user_filter = [filter for filter in users if filter['age'] == criteriy]
        user_filter.sort(key=sort_age)
    if sort_type == 3:
        user_filter = [filter for filter in users if filter['group'] == criteriy]
        user_filter.sort(key=sort_group)
    return user_filter
sort_type = int(input("Введите тип сортировки:"))

if sort_type == 1 :
    criteriy=int(input("Введите  возрас:"))
if sort_type == 2 :
    criteriy=input("Введите первую букву:").capitalize()
if sort_type == 3 :
    criteriy=input("Введите группу :")
print(user_filter(users,sort_type,criteriy))


