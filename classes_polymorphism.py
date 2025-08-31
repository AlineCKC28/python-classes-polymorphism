# ==============================
# Assignment 1: Design Your Own Class
# ==============================

# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def make_call(self, number):
        return f"{self.brand} {self.model} is calling {number}..."

    def charge(self, hours):
        self.battery_life += hours
        return f"{self.brand} {self.model} charged for {hours} hours. Battery life: {self.battery_life}h"

# Derived class: Smartwatch (inheritance)
class Smartwatch(Smartphone):
    def __init__(self, brand, model, battery_life, step_count=0):
        super().__init__(brand, model, battery_life)
        self.step_count = step_count

    def track_steps(self, steps):
        self.step_count += steps
        return f"Steps tracked: {self.step_count}"

# ==============================
# Activity 2: Polymorphism Challenge
# ==============================

class Vehicle:
    def move(self):
        pass  # Base method to be overridden

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"

# ==============================
# Testing the classes
# ==============================

# Assignment 1
phone1 = Smartphone("Apple", "iPhone 14", 20)
watch1 = Smartwatch("Apple", "Watch Series 8", 18)

print(phone1.make_call("123-456-7890"))
print(phone1.charge(2))

print(watch1.track_steps(5000))
print(watch1.charge(1))

# Activity 2: Polymorphism
vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())
