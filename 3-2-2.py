'''
Сделайте список чисел из строки так же как в предыдущей задаче. 
Сделайте новый список с куммулятивной суммой чисел из исходной строки.

Sample Input:
12345
Sample Output:
[1, 3, 6, 10, 15]
'''
a = input()
res = [int(a[0])]
for i in a[1:]:
    res.append(int(i) + res[-1])
print(res)
