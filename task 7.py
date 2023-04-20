
n = int(input("Номер элемента ряда Фибоначчи: "))

a = 1
b = 1

while n>2:
    a, b = b, a+b
    n-=1

print(b)
