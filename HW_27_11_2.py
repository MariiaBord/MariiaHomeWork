import datetime
birth_year = input('Enter your birth year: ' )
def adult_one(x):
    if x in '1234567890':
        current_date = datetime.date.today()
        current_year = current_date.year
        if (current_year - int(x)) >= 18:
            print('Adult')
        else:
            print ('Uderage')
    else:
        print('Go out bro!')
adult_one(birth_year)