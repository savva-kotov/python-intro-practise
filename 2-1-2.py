'''
Прочитайте число. Выведите -1 если оно отрицательное, 1 если оно положительное. Если число равно 0, то выведите 0. 

Sample Input:
7

Sample Output:
1
'''
a = int(input())
if a == 0:
    print(0)
elif a < 0:
    print(-1)
else:
    print(1)
