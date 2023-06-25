from mimesis import Person
from mimesis.enums import Gender

person = Person('en')
print(person.full_name())

email = person.email(domains=['embarcadero.com'])
print(email)

phone = person.telephone(mask='1-3##-5##-7##9')
print(phone)

# Localizations & Genders
de = Person('de')
deFemale = de.full_name(gender=Gender.FEMALE)
deMale = de.full_name(gender=Gender.MALE)
print(deFemale)
print(deMale)

en = Person('en')
enFemale = en.full_name(gender=Gender.FEMALE)
enMale = en.full_name(gender=Gender.MALE)
print(enFemale)
print(enMale)

ru = Person('ru')
ruFemale = ru.full_name(gender=Gender.FEMALE)
ruMale = ru.full_name(gender=Gender.MALE)
print(ruFemale)
print(ruMale)
