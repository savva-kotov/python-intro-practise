'''
Посчитайте сумму первых k натуральных чисел. Число k подается на вход программы.
Да, вы все не глупее Гаусса, но попробуйте воспользоваться циклом while.
В этом модуле натуральные числа начинаются с 1.

Sample Input:
3

Sample Output:
6
'''
a= int(input())
res = 0
while a != 0:
    res += a
    a -= 1
print(res)

