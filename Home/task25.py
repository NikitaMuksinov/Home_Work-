#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.
#
#
# grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin.

text = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
dict_='abcdefghijklmnopqrstuvwxyz'
#dict_='a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'

def ceaser_ (text: str):
    shifr = []
    text = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
    for shift in range(len(dict_)):
        result_=''
        for i in text:

            if i in dict_:
                result_+=(dict_[(dict_.index(i))-shift])
            else:
                result_+=i
        shifr.append((result_))
    return shifr

for message in (ceaser_(text)):
    print(message)


