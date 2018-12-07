from datetime import datetime
name_user = input('Enter your name, please: ')
print ('Thank you')


date_now=datetime.today().year
date_user = input('Enter your Year of birth in format YYYY, please: ')
int_date=0
if len(date_user)==4:
    for i in date_user:

        if i in '1234567890':
            int_date = 1
        else:
            int_date = 0

if (int_date == 1) and (int(date_now)-int(date_user))>21:
    age_user = int(date_now)-int(date_user)
    print (name_user+', you are '+str(age_user)+' and can visit our Nightclub')
elif (int_date == 1) and (int(date_now)-int(date_user))<=21:
    age_user = int(date_now) - int(date_user)
    print(name_user + ', you are ' + str(age_user) + ' and cannot visit our Nightclub')
elif (int_date == 0):
    print ('Your year of birth is in not correct format')
