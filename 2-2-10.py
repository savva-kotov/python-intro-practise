'''
Посчитайте сумму квадратов последовательности. Числа в ней могут быть вещественными.

Sample Input:
2
4
.

Sample Output:
20.0
'''
a = input()
c = 0
while a != '.':
    c += float(a)**2
    a = input()
print(c)

