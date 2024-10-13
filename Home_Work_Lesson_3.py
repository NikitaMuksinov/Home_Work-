# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.
#from multiprocessing.managers import Value
from operator import index

# year=int(input("Enter year:"))
# if year > 0 and year != bool and 10000>year>999:
#     century=(int(str(year)[0:2]))+1
#     print(century)
# elif  year > 0 and year != bool and 1000>year>100:
#     century = (int(str(year)[0:1])) + 1
#     print(century)
# elif  year > 0 and year != bool and 100>year>0:
#     print('1')
# else:
#     print('Номер столетия не действителен')
#
#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
#Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)


# Пример:
# Введите единицу массы тела
#       1 - килограмм
#       2 — миллиграмм
#       3 — грамм
#       4 — тонна
#       5 — центнер
#>4

#Введите  массу тела
#>1

#Ответ: 1000 кг

#import math
# ed_massa=abs(round(int(input('Введите единицу массы тела:'))))
# massa=abs(round(int(input('Введите массу тела:'))))
# if ed_massa ==1:
#     print('Масса тела =',massa,'кг')
# elif ed_massa ==2:
#     print('Масса тела =',massa / pow(10,-6),'кг') # 1кг = 10**6мг
# elif ed_massa == 3:
#     print('Масса тела =', massa / pow(10, 3), 'кг')
# elif ed_massa == 4:
#     print('Масса тела =', massa * pow(10, 3), 'кг')
# elif ed_massa == 5:
#     print('Масса тела =', massa * pow(10, 2), 'кг')
#Преобразовать массив, увеличить каждый его элемент на единицу.
# massive=[1,2,3,4,5,6]
# for i in massive:
#     massive[i-1]+=1
# print(massive)
# #todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.
#
# Пример:
#mass = [1,2,17,54,30,89,2,1,6,2]
#
#
# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.

# def minimum_distanse(mass):
#     hmap = dict()
#     pervios_index = 0
#     current_index = 0
#     for i in range(len(mass)):
#         if mass[i] in hmap:
#             current_index=i
#             pervios_index=hmap[mass[i]]
#         hmap[mass[i]] = i
#
#     return pervios_index,current_index
#
# mass = [1, 2, 17, 54, 30, 89, 2, 1, 6, 2]
# print(minimum_distanse(mass))

# mass = [1, 2, 17, 54, 30, 89, 2, 1, 6, 2]
# hmap=dict()
# for key, value in enumerate(mass):
#     if mass.count(value)>1 and value in mass[key+1:]:
#         hmap.update({key : mass.index(value,key+1)})
# print(hmap)
