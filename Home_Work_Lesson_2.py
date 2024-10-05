
#task10.py
#Дано целое число A. Проверить истинность высказывания: «Число A является четным».
# a=int(input())
# print(bool(a%2==0))
# a=int(input())
# print(bool(a%2==1))
#task5.py
# Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат возведения в степень.
# number1=int(input())
# number2=int(input())
# print(number1+number2,number1-number2,number1*number2,number1/number2,number1//number2,number1%number2,number1**number1)
#task6.py
#Дана сторона квадрата a. Найти его площадь S = a²
# Примечание: сторону квадрата получаем через функцию input().
# a=int(input())
# print('S =' , a**2)
#task7.py
# Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC и их сумму.
# Примечание: все точки получаем через функцию input().
# a=int(input())
# b=int(input())
# c=int(input())
# print('AC = ',abs(a)+abs(c),'AC = ',abs(b) + abs(c),'summ = ',(abs(a)+abs(c))+(abs(b)+abs(c)))
# task8.py
# Проверить истинность высказывания: "Данное четырехзначное число читается одинаково слева направо и справа налево".
# number=1223
# print((bool(int(str(abs(number))[0]))==(int(str(abs(number))[3]))) and (int(str(abs(number))[1]))==(int(str(abs(number))[2])))
#task9.py
## todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты получаем через функцию input().
a = int(input())
b = int(input())
if a == 0:
    print('Решений нет!')
else:
    print('x = ',(-b)/a)




