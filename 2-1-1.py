'''
Напишите программу, которая считывает два числа и выводит то из них, которое больше.

Sample Input:
436
337

Sample Output:
436
'''
a, b = int(input()), int(input())
if a > b:
    print(a)
else:
    print(b)
