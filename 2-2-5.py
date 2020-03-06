'''
Последовательность Фибонначи -- это числовая последовательность в которой каждый член равен сумме двух предыдущих.
Подробнее можно почитать про нее на википедии: Числа Фибоначчи. Эта информация не поможет Вам решить задачу.
Напишите программу, которая будет вычислять n-ое число Фибоначчи. Число n, которое подается на вход программе, может принимать значения от 0 до 20.
'''
x = 0
y = 1
a = int(input())
for i in range(a):
    x, y = y, x + y
print(x)