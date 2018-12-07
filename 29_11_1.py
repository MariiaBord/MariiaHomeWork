a=[1,2,3,4,5,6,7]
b=list()
#умножение в цикле ледующего числа на предыдущее, первое число без изменений
for i,v in enumerate(a):
    if i==0:
        b.append(v)
        continue
    b.append(a[i]*a[i-1])
    if i==4:
        break
print(b)





