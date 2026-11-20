from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car has started")


class Bike(Vehicle):
    def start(self):
        print("Bike has started")


c = Car()
b = Bike()

c.start()
b.start()
