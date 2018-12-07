import datetime
a = ''
current_year = datetime.date.today().year
while not a:
   try:
       a = input('Imput your birth year:')
       if len(a) == 4 and int(a) <= current_year:
           print('Underage') if (current_year - int(a)) < 18 else print('Adult')
       else:
           print('No more four numbers and no more than {} year, please'.format(current_year))
           a = ''
   except:
       print('Only numbers,'
             ' please')