class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color= color
        self.for_sale = for_sale

    def drive(self):
        print("Driving")
    def stop(self):
        print("stopping")

Car1 = Car("Mustang", 2024, "Red", False)

print(Car1.model)
print(Car1.year)
print(Car1.color)
print(Car1.for_sale)
Car1.drive()