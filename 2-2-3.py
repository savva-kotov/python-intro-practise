'''
Посчитайте сумму первых k нечетных чисел. Число k подается на вход программы.

Sample Input:
2

Sample Output:
4
'''
a = int(input())
res = 0
nez = 1
for i in range(a):
    res += nez
    nez += 2
print(res)

