class Employee:
    def __init__(self, lname, fname, addy, phone):
        self.last_name = lname
        self.first_name = fname
        self.address = addy
        self.phone_number = phone

    def display(self):
        return self.last_name + ", " + self.first_name + ", address: " + self.address + ", phone: " + self.phone_number


class SalariedEmployee(Employee):
    def __init__(self, lname, fname, addy, phone, start, salary):
        super().__init__(lname, fname, addy, phone)
        self.start_date = start
        self.salary = salary

    def display(self):
        return (self.last_name + ", " + self.first_name + ", address: " + self.address + ", phone:"
                + self.phone_number + ", start date: " + self.start_date + ", salary: " + str(self.salary))

    def give_raise(self, amt):
        self.salary += amt


class HourlyEmployee(Employee):
    def __init__(self, lname, fname, addy, phone, start, hourly):
        super().__init__(lname, fname, addy, phone)
        self.start_date = start
        self.hourly_pay = hourly

    def display(self):
        return (self.last_name + ", " + self.first_name + ", address: " + self.address + ", phone:"
                + self.phone_number + ", start date: " + self.start_date + ", wage/hr: " + str(self.hourly_pay))

    def give_raise(self, amt):
        self.hourly_pay += amt


if __name__ == "__main__":
    salaried_employee = SalariedEmployee(lname="vanblair", fname="chase", addy="77777 st", phone="555555", start="7/15",
                                         salary=40000)
    print(salaried_employee.display())
    salaried_employee.give_raise(5000)
    print(salaried_employee.display())
    del salaried_employee

    hourly_employee = HourlyEmployee(lname="vanblair", fname='chase', addy="7777777 st", phone="55555", start="7/15",
                                     hourly=10.0)
    print("\n" + hourly_employee.display())
    hourly_employee.give_raise(2)
    print(hourly_employee.display())
    del hourly_employee
