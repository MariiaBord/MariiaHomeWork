a = [3, 6, 8, 95, 6, 58, 8, 9, 13, 15, 16, 17, 18, 19, 20]
b = []
for i, v in enumerate(a):
    if v not in (13, 14, 17, 18, 19):
        b.append(v)
    else:
        print(f'{v}is equal zero')

print(b, 'sum is', sum(b))