import datetime

class Person:
    def __init__(self, name, year, month, day):
        self.name = name
        self.year = year
        self.month = month
        self.day = day

    def get_age(self):
        birth_date = datetime.date(self.year, self.month, self.day)
        years = datetime.date(2018, 12, 31).year - birth_date.year
        if datetime.datetime(2018, 12, 31).date() >= birth_date.replace(year=datetime.datetime.now().year):
            age = years
        else:
            age = years - 1
        return age


p1 = Person('Bekbolot', 2018, 7, 21)
p2 = Person('Suberadam', 1990, 5, 15)
print('Bekbolot is ' + str(p1.get_age()) + ' y. o.')
print('Superadam is ' + str(p2.get_age()) + ' y. o.')
