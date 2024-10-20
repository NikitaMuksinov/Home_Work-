#todo: Модифицировать программу таким образом чтобы она выводила
#  приветствие "Hello", которое до этого записано в файл text.txt
#  через метод write()

f = open("text.txt", "w+t")
f.write("Hello\n")
f.close()
f = open("text.txt", "r")
print(f.read())
f.close()