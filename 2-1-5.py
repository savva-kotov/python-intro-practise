'''
Напишите программу, которая будет получать на вход количество,  а выводить это число и правильное склонение слова "студент" латиницей ("student", "studenta", "studentov").
Между числом и словом должен быть ровно один пробел.

Sample Input:
3

Sample Output:
3 studenta
'''
s = int (input())
n1 =" studentov"
n2 =" student"
n3 =" studenta"
if  s>=0:
    if s==0:
        print(str(s) + n1)
    elif s%100>=10 and s%100<=20:
        print(str(s) + n1)
    elif s%10==1:
        print(str(s) + n2)
    elif s%10>=2 and s%10<=4:
        print(str(s) + n3)
    else:
        print(str(s) + n1)

