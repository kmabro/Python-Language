class Vehicle:
  def __init__(self, type, engine_type, chassis_number):
    self.type = type
    self._engine_type = engine_type
    self.__chassis_number = chassis_number

  def vehicle_info(self):
    print("type:", self.type)
    print("engine_type:", self._engine_type)
    print("chassis_number:", self.__chassis_number)

class Car(Vehicle):
  def car_info(self):
    print("type:", self.type)
    print("engine_type:", self._engine_type)
    print("chassis_number:",     self._Vehicle__chassis_number)

obj = Car("SUV", "V8", 1234567890)
obj.vehicle_info()
obj.car_info()
print(obj.type)
print(obj._engine_type)
print(obj._Vehicle__chassis_number)