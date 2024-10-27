#todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ', ', '!' ]

input=(' 8 5 12 12 15 ,  0 23 15 18 12 4 !')
input_=input.split(' ')
sdict={}
text=[]
for i,number in enumerate(alphabet):
    sdict[i]=number
print(input_)
print(sdict)
for i in input_:
    for key, value in sdict.items():
        if i == str(key+1):
            text.append(value)
    if i == ',' or i =='!':
        text.append(i)
my_string=''.join(text)
new_string=my_string.replace(',',', ')
print(new_string)


