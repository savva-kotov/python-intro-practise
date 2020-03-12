'''
Прочитайте число k. Нарисуйте квадрат из символов # размера k×kk \times kk×k, как в примере.
Гарантируется, что k целое и больше 0.

Sample Input:
3
Sample Output:
['#', '#', '#']
['#', '#', '#']
['#', '#', '#']
'''
a = int(input())
for i in range(a):
    print(['#' for i in range(a)])


