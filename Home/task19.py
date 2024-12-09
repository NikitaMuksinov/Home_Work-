# #todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# – id - номер по порядку (от 1 до 10);
# – текст из списка algoritm
#
algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ]
# "EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]
#
# Каждое значение из списка должно находится на отдельной строке.
# Выход:
# 1 % "C4.5"
# 2 % "k - means"
# и т.д.




csv_string = ""
for i, algo in enumerate(algoritm):
    csv_string += f"{i+1}%{algo}\n"

with open('algoritm.csv', 'w') as f:
    f.write(csv_string)