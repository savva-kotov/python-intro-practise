'''
Найдите второй максимум последовательности, т.е. второе по величине. В последовательности есть хотя бы два числа.
Числа могут быть вещественные.

Sample Input 1:
3
3
2
.

Sample Output 1:
3.0

Sample Input 2:
5
3
7
.

Sample Output 2:
5.0
'''
a = input()
c = []

while a != '.':
    c.append(float(a))
    a = input()


print(sorted(c)[-2])
