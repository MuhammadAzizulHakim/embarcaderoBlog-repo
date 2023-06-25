import fauxfactory
import datetime

string = fauxfactory.gen_string('alphanumeric', 15)
print(string)
print(string.isalnum())
print(len(string))

numeric = fauxfactory.gen_string('numeric', 5)
print(numeric)
print(numeric.isnumeric())
print(len(numeric))

date = fauxfactory.gen_date()
print(date)
datetime = fauxfactory.gen_datetime()
print(datetime)

email = fauxfactory.gen_email(domain='embarcadero')
print(email)
print('@embarcadero' in email)
