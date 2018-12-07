import datetime
date_birth = input('Укажите ГОД рождения: ')
date_today = datetime.date.today().year
date_delta = int(date_today)-int(date_birth)
if date_delta < 18:
    print ('Underage')
else:
    print('Adult')