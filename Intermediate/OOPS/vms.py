from abc import ABC, abstractmethod

class Vehicle:
    counter = 0

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        Vehicle.counter += 1

    def display_info(self):
        print(f"Vehicle make is {self.make}")
        print(f"Vehicle Model is {self.model}")
        print(f"year made is {self.year}")
        print(f"color of the vehicle is {self.color}")

    @staticmethod
    def show_count():
        print(Vehicle.counter)

    @classmethod
    def class_count(cls):
        print(cls.counter)

    @abstractmethod
    def start_engine(self):
        print(f"ENGINE STARTED")

    @abstractmethod
    def move(self):
        print("Car started to move")

    @abstractmethod
    def stop(self):
        print("stopped the car")

class Car(Vehicle):

    def __init__(self, make, model, year, color, no_of_doors, price):
        self.no_of_doors = no_of_doors
        self.__price = price
        super().__init__(make, model, year, color)

    @property
    def price(self):
        print("getting the price of the car")
        return self.__price

    @price.setter
    def price(self, amount):
        if self.__price < 0:
            raise ValueError("Price should not be less than zero")
        else:
            self.__price = amount

    @price.deleter
    def price(self):
        print("deleting the price...")
        del self.__price

    def display_info(self):
        print(f"Vehicle make is {self.make} "
              f"Vehicle Model is {self.model}"
              f"year made is {self.year}"
              f"color of the vehicle is {self.color}"
              f"no of doors of the vehicle is {self.no_of_doors}")

    def show_price(self):
        return self.__price

    def calculate_discount(self, discount_percentage):
        actual_price = self.__price
        discounted_amount = (discount_percentage/100) * self.__price
        final_price = round(actual_price - discounted_amount, 2)
        return final_price

car = Car("Japan", "Hyundai",2025,"white",5, 1100000)
car.display_info()



