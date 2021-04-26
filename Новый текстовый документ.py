a = [0, 0, 0, 0, 0, 0]
a[0] = 1
a[-1] = 1
print(a)


a = [1, 0]
print(a*10)


a = []
for i in range(10):
	a.append(i%2)
print(a)


a = []
for i in range (1, 10, 2):
	a.append(i)
print(a)


a = []
x = int(input('введите первый элемент '))
d = int(input('введите разность '))
for i in range(x, x+100, d):
	a.append(i)
print(a)


a = []
num = 99
a = [num]
while num > 0:
	num -= 1
	if num%3 == 0:
		a.append(num)
print(a)


a = []










