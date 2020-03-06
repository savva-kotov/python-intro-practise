'''
Посчитайте среднее арифметическое всех элементов целочисленной последовательности. Последовательность непустая.

Sample Input:
5
2
.

Sample Output:
3.5
'''
a = input()
c = []
while a != '.':
    c.append(int(a))
    a = input()
print(sum(c)/len(c))

