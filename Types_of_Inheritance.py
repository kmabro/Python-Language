############### Single Inheritance ###############

'''
Create a class `Vehicle` with attributes `brand` and `model`, and a method `start()` that prints "Vehicle started".
Now create a class `Car` that inherits from `Vehicle` and has an additional attribute `fuel_type`.
Override the `start()` method to print "Car started using <fuel_type>".
Create an object of `Car` and call the `start()` method.
'''
# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def start(self):
#     print("Vehicle started")

# class Car(Vehicle):
#   def __init__(self, brand, model, fuel_type):
#     super().__init__(brand, model)
#     self.fuel_type = fuel_type

#   def start(self):
#     print(f"Car started using {self.fuel_type}")

# car = Car("Toyota", "Camry", "Gasoline")
# car.start()

'''
Create a class `Person` with attributes `name` and `age`, and a method `show_info()` that prints them.
Now create a class `Student` that inherits from `Person` and adds a new attribute `student_id`.
Override the `show_info()` method to also include student_id in the output.
Create a `Student` object and call `show_info()`.
'''
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def show_info(self):
#     print(f"Name: {self.name}, Age: {self.age}")
    
# class Student(Person):
#   def __init__(self, name, age, student_id):
#     super().__init__(name, age)
#     self.student_id = student_id

#   def show_info(self):
#     print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")

# obj = Student("km_abro", 19, "S12345")
# obj.show_info()

'''
Create a class `Appliance` with method `power_on()` that prints "Appliance is on".
Create a subclass `WashingMachine` that inherits from `Appliance` and adds a method `wash()` that prints "Washing clothes...".
Create an object of `WashingMachine` and call both `power_on()` and `wash()`.
'''
# class Appliance:
#   def power_on(self):
#     print("Appliance is on")

# class WashingMachine(Appliance):
#   def wash(self):
#     print("Washing clothes...")

# obj = WashingMachine()
# obj.power_on()
# obj.wash()


############### Multiple Inheritance ###############


'''
Create a class `Writer` with a method `write()` that prints "Writing content...".
Create another class `Editor` with a method `edit()` that prints "Editing content...".
Now create a class `ContentCreator` that inherits from both `Writer` and `Editor`.
Create an object of `ContentCreator` and call both `write()` and `edit()` methods.
'''
# class Writer:
#   def write(self):
#     print("Writing content...")

# class Editor:
#   def edit(self):
#     print("Editing content...")

# class ContentCreator(Writer, Editor):
#   pass

# obj = ContentCreator()
# obj.write()
# obj.edit()

'''
Create a class `Camera` with an attribute `resolution` and method `take_photo()` that prints "Photo taken at <resolution> resolution".
Create another class `Phone` with an attribute `brand` and method `make_call()` that prints "Calling from <brand>".
Create a class `Smartphone` that inherits from both `Camera` and `Phone`.
Create an object of `Smartphone` and call both methods.
'''
# class Camera:
#   def __init__(self, resolution):
#     self.resolution = resolution

#   def take_photo(self):
#     print(f"Photo taken at {self.resolution} resolution")

# class Phone:
#   def __init__(self, brand):
#     self.brand = brand

#   def make_call(self):
#     print(f"Calling from {self.brand}")

# class Smartphone(Camera, Phone):
#   def __init__(self, resolution, brand):
#     Camera.__init__(self, resolution)  
#     Phone.__init__(self, brand)  

# obj = Smartphone("1080p", "Samsung")
# obj.take_photo()
# obj.make_call()

'''
Create a class `Person` with attribute `name` and method `introduce()` that prints "I am <name>".
Create a class `Employee` with attribute `employee_id` and method `show_id()` that prints "My ID is <employee_id>".
Create a class `Manager` that inherits from both `Person` and `Employee`.
Create an object of `Manager` and call both `introduce()` and `show_id()` methods.
'''
# class Person:
#   def __init__(self, name):
#     self.name = name

#   def introduce(self):
#     print(f"I am {self.name}")

# class Employee:
#   def __init__(self, employee_id):
#     self.employee_id = employee_id

#   def show_id(self):
#     print(f"My ID is {self.employee_id}")

# class Manager(Person, Employee):
#   def __init__(self, name, employee_id):
#     Person.__init__(self, name)
#     Employee.__init__(self, employee_id)

# obj = Manager("km_abro", "M12345")
# obj.introduce()
# obj.show_id()


############### Multilevel Inheritance ###############


'''
Create a base class `Person` with attributes `name` and `age`. It should have a method `display_info()`.

Create a derived class `Student` that inherits from `Person` and adds an attribute `student_id`.

Then, create another derived class `GraduateStudent` that inherits from `Student` and adds an attribute `thesis_topic`.

Create an object of `GraduateStudent` and display all the details using a method.
'''
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def display_info(self):
#     print(f"Name: {self.name}, Age: {self.age}")

# class Student(Person):
#   def __init__(self, name, age, student_id):
#     super().__init__(name, age)
#     self.student_id = student_id

#   def display_info(self):
#     super().display_info()
#     print(f"Student ID: {self.student_id}")

# class GraduateStudent(Student):
#   def __init__(self, name, age, student_id, thesis_topic):
#     super().__init__(name, age, student_id)
#     self.thesis_topic = thesis_topic

#   def display_info(self):
#     super().display_info()
#     print(f"Thesis Topic: {self.thesis_topic}")

# obj1 = GraduateStudent("km_abro", 19, "S12345", "AI")
# obj1.display_info()

'''
Create a base class `Vehicle` with attributes `brand` and `model`, and a method `show_info()`.

Create a class `Car` that inherits from `Vehicle` and adds `engine_type` as an attribute.

Then, create another class `ElectricCar` that inherits from `Car` and adds an attribute `battery_range`.

Create an object of `ElectricCar` and call a method that shows all the details from all classes.
'''
# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def show_info(self):
#     print(f"Brand: {self.brand}, Model: {self.model}")

# class Car(Vehicle):
#   def __init__(self, brand, model, engine_type):
#     super().__init__(brand, model)
#     self.engine_type = engine_type

#   def show_info(self):
#     super().show_info()
#     print(f"Engine Type: {self.engine_type}")

# class ElectricCar(Car):
#   def __init__(self, brand, model, engine_type, battery_range):
#     super().__init__(brand, model, engine_type)
#     self.battery_range = battery_range

#   def show_info(self):
#     super().show_info()
#     print(f"Battery Range: {self.battery_range}")

# obj = ElectricCar("Tesla", "Model S", "Electric", "500 miles")
# obj.show_info()

'''
Create a base class `Employee` with attributes `name` and `position`, and a method `introduce()`.

Create a class `TeamLead` that inherits from `Employee` and adds an attribute `team_name`.

Then create a class `ProjectManager` that inherits from `TeamLead` and adds an attribute `project_budget`.

Create an object of `ProjectManager` and call a method that prints out all the data.
'''
# class Employee:
#   def __init__(self, name, position):
#     self.name = name
#     self.position = position

#   def introduce(self):
#     print(f"Name: {self.name}")
#     print(f"Position: {self.position}")

# class TeamLead(Employee):
#   def __init__(self, name, position, team_name):
#     super().__init__(name, position)
#     self.team_name = team_name

#   def introduce(self):
#     super().introduce()
#     print(f"Team Name: {self.team_name}")

# class ProjectManager(TeamLead):
#   def __init__(self, name, position, team_name, project_budget):
#     super().__init__(name, position, team_name)
#     self.project_budget = project_budget

#   def introduce(self):
#     super().introduce()
#     print(f"Project Budget: {self.project_budget}")

# obj = ProjectManager("km_abro", "Project Manager", "AI Team", "$100,000")
# obj.introduce()

 
############### Hybrid Inheritance ###############


'''
Create a base class `Employee` with attributes `name` and `age`. Then create a class `FullTime` that inherits from `Employee` and adds a `salary` attribute.

Create another class `Department` (not related to `Employee`) that has `dept_name` and `location`.

Now create a class `Manager` that inherits from `FullTime` and also accepts a `Department` object as an attribute.

Create a `Manager` object and print all related details using a method.
'''
# class Employee:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# class FullTime(Employee):
#   def __init__(self, name, age, salary):
#     super().__init__(name, age)
#     self.salary = salary

# class Department:
#   def __init__(self, dept_name, location):
#     self.dept_name = dept_name
#     self.location = location

# class Manager(FullTime):
#   def __init__(self, name, age, salary, department):
#     super().__init__(name, age, salary)
#     self.department = department

# obj = Manager("km_abro", 19, 100000, Department("AI", "New York"))
# print(obj.name, obj.age, obj.salary, obj.department.dept_name, obj.department.location)

'''
Create a base class `Appliance` with attributes `brand` and `wattage`. Then create a class `KitchenAppliance` that inherits from `Appliance` and adds `purpose`.

Also create a separate class `Warranty` that holds `duration` and `coverage` details.

Create a class `Microwave` that inherits from `KitchenAppliance` and associates with `Warranty`.

Create an object of `Microwave` and display all details clearly using a method.
'''
# class Appliance:
#   def __init__(self, brand, wattage):
#     self.brand = brand
#     self.wattage = wattage

# class KitchenAppliance(Appliance):
#   def __init__(self, brand, wattage, purpose):
#     super().__init__(brand, wattage)
#     self.purpose = purpose

# class Warranty:
#   def __init__(self, duration, coverage):
#     self.duration = duration
#     self.coverage = coverage

# class Microwave(KitchenAppliance):
#   def __init__(self, brand, wattage, purpose, warranty):
#     super().__init__(brand, wattage, purpose)
#     self.warranty = warranty

# obj = Microwave("Samsung", 1000, "Cooking", Warranty("2 years", "Full coverage"))
# print(obj.brand, obj.wattage, obj.purpose, obj.warranty.duration,obj.warranty.coverage)


############## Hierarchical Inheritance ##############


'''
Create a base class `Employee` with an attribute `name`.

Create two classes `Manager` and `Developer` that inherit from `Employee`.

Add an attribute `department` to `Manager`, and `language` to `Developer`.

Create one object of each class and display all their details.
'''
# class Employee:
#   def __init__(self, name):
#     self.name = name

# class Manager(Employee):
#   def __init__(self, name, department):
#     super().__init__(name)  
#     self.department = department

# class Developer(Employee):
#   def __init__(self, name, language):
#     super().__init__(name)
#     self.language = language

# obj1 = Manager("km_abro", "AI")
# print(obj1.name, obj1.department)
# obj2 = Developer("km_abro", "Python")
# print(obj2.name, obj2.language)

'''
Create a class `Shape` with an attribute `name`.

Now create two classes `Rectangle` and `Circle` that inherit from `Shape`.

Add appropriate attributes: `length` and `width` to `Rectangle`, and `radius` to `Circle`.

Print area of each shape along with its name.
(You can use simple area formulas: area = length * width, area = 3.14 * radius * radius)
'''
# class Shape:
#   def __init__(self, name):
#     self.name = name

# class Rectangle(Shape):
#   def __init__(self, name, length, width):
#     super().__init__(name)
#     self.length = length
#     self.width = width

# class Circle(Shape):
#   def __init__(self, name, radius):
#     super().__init__(name)
#     self.radius = radius
#     self.area = 3.14 * radius * radius

# obj1 = Rectangle("Rectangle", 10, 20)
# print(obj1.name, obj1.length * obj1.width)
# obj2 = Circle("Circle", 10)
# print(obj2.name,obj2.area)