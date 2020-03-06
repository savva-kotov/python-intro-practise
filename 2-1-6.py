'''
Напишите программу, которая прочитает 3 числа и выведет максимум из них троих.

Sample Input:
8
11
9

Sample Output:
11
'''
res = [int(input()),int(input()),int(input())]
print(sorted(res)[-1])

