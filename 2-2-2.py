'''
Посчитайте сумму квадратов первых k натуральных чисел. Число k подается на вход программы.

Sample Input:
3

Sample Output:
14
'''
a= int(input())
res = 0
while a != 0:
    res += a**2
    a -= 1
print(res)
