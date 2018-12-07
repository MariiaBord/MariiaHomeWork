#сумма четных чисел массива
list_chet = (1,5,6,9,8,3,4,6,8,7,6)
summ_1 = 0
for i in list_chet:
    if i%2 == 0:
        summ_1+=i
print ('Sum of even numbers: ',summ_1)

#сумма максимального и минимального чисел
sum_max_min=max(list_chet)+min(list_chet)
print('Sum of max and min: ',sum_max_min)

# количество различных элементов в массиве
a=(1,2,2,7,7,5,6,8,9,9,9,9,4,3)
list_dif = set(a)
print('Number of different in list ',a,'is: ',len(list_dif))

#опеределение повторяющихся элементов
b=[]
for i in a:
    x=a.count(i)#Возвращает количество раз, когда i отображается в списке.
    b.append(x)#добавление в массив каждое различное
if max(b)>1:
    print('Max repetitions : ',max(b))
    print('Number of repeating: ',len(set(b)))
else:
    print('All numbers in ',a, ' are different')

#удаление первого и последнего элемента в массиве
c=[7,6,8,'qwert',9.2,3]
c_n=c[1:-1]

#обратная сортировка
c_n.reverse()
print(c_n)













