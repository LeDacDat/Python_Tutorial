#Date Time in Python
import datetime
from datetime import date
#Example 1
now = date.today()
print(now)

now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

#Example 2

birthday = date(2002,4,1)
age = now - birthday
print(age)
#Example 3
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
#example 4

from datetime import datetime

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("Time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)


