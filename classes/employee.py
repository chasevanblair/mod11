"""

Program: employee.py

Author: Chase Van Blair

Last date modified: 7/15/20


The purpose of this program is to use polymorphism to have different kinds of employees:salaried and hourly

"""


class Employee:

    def __init__(self, lname, fname, addy, phone):
        """
        base constructor
        :param lname: last name
        :param fname: first name
        :param addy: address
        :param phone: phone number
        """
        self.last_name = lname
        self.first_name = fname
        self.address = addy
        self.phone_number = phone

    def display(self):
        """
        display employee values
        :return: values
        """
        return self.last_name + ", " + self.first_name + ", address: " + self.address + ", phone: " + self.phone_number


class SalariedEmployee(Employee):
    def __init__(self, lname, fname, addy, phone, start, salary):
        """
        employee with salaried pay
        :param lname: last name
        :param fname: first name
        :param addy: address
        :param phone: phone number
        :param start: start date
        :param salary: salary
        """
        super().__init__(lname, fname, addy, phone)
        self.start_date = start
        self.salary = salary

    def display(self):
        """
        print salaried employee values
        :return: salaried employee values
        """
        return (self.last_name + ", " + self.first_name + ", address: " + self.address + ", phone:"
                + self.phone_number + ", start date: " + self.start_date + ", salary: " + str(self.salary))

    def give_raise(self, amt):
        """
        adds to employees salary
        :param amt: amt to raise the salary by
        :return:
        """
        self.salary += amt


class HourlyEmployee(Employee):
    def __init__(self, lname, fname, addy, phone, start, hourly):
        """
        employee with hourly pay
        :param lname: last name
        :param fname: first name
        :param addy: address
        :param phone: phone number
        :param start: start date
        :param hourly: hourly pay
        """
        super().__init__(lname, fname, addy, phone)
        self.start_date = start
        self.hourly_pay = hourly

    def display(self):
        """
        shows values of hourly employee
        :return: values of hourly employee
        """
        return (self.last_name + ", " + self.first_name + ", address: " + self.address + ", phone:"
                + self.phone_number + ", start date: " + self.start_date + ", wage/hr: " + str(self.hourly_pay))

    def give_raise(self, amt):
        """
        raises hourly pay by a given amt
        :param amt: amt to add to hourly wage
        :return:
        """
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
