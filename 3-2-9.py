'''
Прочитайте последовательность целых чисел. Выведите список в котором сначала будут числа, которые меньше трех, 
а потом те, что больше или равны трем.

Sample Input:
-1
6
2
4
.
Sample Output:
[-1, 2, 6, 4]
'''
a = input()
res = []
ans = []
if a != '.':
    while a != '.':
        res.append(int(a))
        a = input()
b = []
s = []
for i in res:
    if i < 3:
        s.append(i)
    else:
        b.append(i)
print(s + b)
