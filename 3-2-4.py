'''
Прочитайте две строки и создайте список, в котором будут чередоваться символы из первой и второй строк.
Строки, которые подаются на вход в этой задаче, одинаковой длины.

Sample Input:
hello
world
Sample Output:
['h', 'w', 'e', 'o', 'l', 'r', 'l', 'l', 'o', 'd']
'''
a, b = input(), input()
res = []
for i in range(len(a)):
    res.append(a[i])
    res.append(b[i])
print(res)

