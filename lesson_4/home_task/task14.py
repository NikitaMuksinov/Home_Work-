
#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.

# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]
#
#
# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.
#
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
# # print(minimum_distanse(mass))
#
# mass = [1, 2, 17, 54, 30, 89, 2, 1, 6, 2]
# hmap=dict()
# for key, value in enumerate(mass):
#     if mass.count(value)>1 and value in mass[key+1:]:
#         hmap.update({key : mass.index(value,key+1)})
# print(hmap)

#тут 2 решения