'''
Надите максимум последовательности. Последовательность не пустая.

Sample Input:
10.1
2.0
9.1
.

Sample Output:
10.1
'''
a = input()
c = []

while a != '.':
    c.append(float(a))
    a = input()

print(max(c))
