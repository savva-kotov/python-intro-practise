'''
Напишите программу, которая считывает два числа и выводит номер того из них, которое больше.
Если первое больше, то выводится "1". Если второе, то - "2". Если числа равны, то "0".

Sample Input:
8
11

Sample Output:
2
'''
a, b = int(input()), int(input())
if a == b:
    print(0)
elif a > b:
    print(1)
else:
    print(2)