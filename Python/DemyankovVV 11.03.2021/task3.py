a = int(input("Введите 1-ое число:"))
b = int(input("Введите 2-ое число:"))
c = int(input("Введите 3-е число:"))
if a+b < c or a+c < b or b+c < a:
    print("Такого треугольника не существует")
else:
    print("Такой треугольник существует")