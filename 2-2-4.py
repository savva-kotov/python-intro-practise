'''
Простое число делится без остатка только на 1 и на само себя.
Напишите программу, которая прочитает число и выведет "prime" если число простое и "composite" в противном случае (без кавычек).

Sample Input:
4

Sample Output:
composite
'''
import math

n = int(input())

if n < 2:
    print("composite")
    quit()
elif n == 2:
    print("prime")
    quit()

i = 2
limit = int(math.sqrt(n))

while i <= limit:
    if n % i == 0:
        print("composite")
        quit()
    i += 1

print("prime")
