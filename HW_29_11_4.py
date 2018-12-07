#конкатенация (склеивание) строк
str_1=input('Enter first string:')
str_2=input('Enter second string:')
#str_1=str_1[1:] удаление первых n символов из строки
print(str_1[1:]+str_2)

#три повторения двух последних букв
str_3=(str_1[(len(str_1)-2):])*3
print(str_3)

#сортировка списка в обратном порядке
a= [2,5,8,4,9,2,6]
b=[]
i=len(a)-1
while i >= 0:
    b.append(a[i])
    i-=1
print('reverse list ',a,' in' , b)

#найти максимальное и вывести список из максимального числа*длина исходного списка
c=list()
for i in a:
    c.append(max(a))
print(c)

#сумма чисел массива, с 13 до 19 =0, исключая 15 и 16
d=(10,11,12,13,14,15,16,17,18,19,20)
e=(13,14,17,18,19)
print(sum(d)-sum(e))

a = (3, 6, 8, 95, 6, 58, 8, 9, 13, 15, 16, 17, 18, 19, 20)
b = []
for i, v in enumerate(a):
    if v not in (13, 14, 17, 18, 19):
        b.append(v)
    else:
        print(f'{v}is equal zero')

print(b, ' ', sum(b))





