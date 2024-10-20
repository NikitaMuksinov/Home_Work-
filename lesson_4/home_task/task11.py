# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.
year=int(input("Enter year:"))
if year > 0 and year != bool and 10000>year>999:
    century=(int(str(year)[0:2]))+1
    print(century)
elif  year > 0 and year != bool and 1000>year>100:
    century = (int(str(year)[0:1])) + 1
    print(century)
elif  year > 0 and year != bool and 100>year>0:
    print('1')
else:
    print('Номер столетия не действителен')