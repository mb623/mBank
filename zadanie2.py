

class Person:

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))


class Manager(Person):

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)


if __name__ == '__main__':
    stach = Person(name="Stanisław Pająk", job='Kierowca', pay=8000)
    print(stach.name, stach.pay)
    stach.giveRaise(.10)
    print(stach.pay)
    ania = Manager("Anna Dolna", 'manager', 8000)
    ania.giveRaise(.10)
    print(ania.lastName(), ania.pay)
    print(ania)