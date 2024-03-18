# kelas induk
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def identity(self):
        return self.first_name + " " + self.last_name

# kelas turunan
class Employee(Person):
    def __init__(self, first_name, last_name, staff_number):
        super().__init__(first_name,last_name)
        self.staff_number = staff_number
        
    def identity(self):
        return super().identity() + " " + str(self.staff_number)
    
# membuat 2 objek dari kelas Person dan kelas Employee
person_budi = Person("Budi", "Purnama")
employee_budi = Employee("budi", "Purnomo", 19821)

# memanggil method identity dari kelas Person
identity_person_budy = person_budi.identity()
print(identity_person_budy)

# memanggil method identity dari kelas Employee
identity_employee_budi = employee_budi.identity()
print(identity_employee_budi)