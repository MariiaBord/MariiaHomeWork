def chek_seasons (month):
    seasons={
    'summer':(6,7,8),
    'fall':(9,10,11),
    'winter':(12,1,2),
    'spring':(3,4,5)
    }
    for k,v in seasons.items():
        if month in v:
            return k,'end'
    return 'eror'
while True:
    month = int(input('enter month number: '))
    res=chek_seasons(month)
    if res[1]=='end':
        print(res[0])
        break

