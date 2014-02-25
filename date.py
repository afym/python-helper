import datetime
import time
from datetime import date

# time actual time
now = time.time()
birthday = datetime.date(1989, 6, 14)

print (now)
print (type(birthday))

birthdayString = "Your birthday is : " + birthday.strftime('%d / %m / %Y')

print (birthdayString)

deltaDate = datetime.timedelta(2) # delta in date
someDate = datetime.date(2005, 6, 4)

print ("Some date is : " + someDate.strftime('%Y-%m-%d'))

newDateA = someDate + deltaDate

print ("Some date + 2 is :" + newDateA.strftime('%Y-%m-%d'))

newDateB = someDate - deltaDate

print ("Some date - 2 is :" + newDateB.strftime('%Y-%m-%d'))