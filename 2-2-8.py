'''
Посчитайте теперь сумму членов последовательности. Все числа в ней целые.

Sample Input:
1
4
-2
.

Sample Output:
3
'''
a = input()
c = 0
while a != '.':
    c += int(a)
    a = input()
print(c)
