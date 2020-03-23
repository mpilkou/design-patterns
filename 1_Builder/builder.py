from abc import abstractmethod
from parts import Vehicle


class Builder:

    @abstractmethod
    def build_frame(self):
        pass

    @abstractmethod
    def build_engine(self):
        pass

    @abstractmethod
    def build_wheels(self):
        pass

    @abstractmethod
    def build_doors(self):
        pass


class MotorcycleBuilder(Builder):

    def __init__(self):
        self.vehicle = Vehicle("MotorCycle")

    def build_frame(self):
        self.vehicle.frame = "MotorCycle frame"
        return self.vehicle.frame

    def build_engine(self):
        self.vehicle.engine = 500
        return self.vehicle.engine

    def build_wheels(self):
        self.vehicle.wheels = 2
        return self.vehicle.wheels

    def build_doors(self):
        self.vehicle.doors = 0
        return self.vehicle.doors


class CarBuilder(Builder):

    def __init__(self):
        self.vehicle = Vehicle("Car")

    def build_frame(self):
        self.vehicle.frame = "Car frame"
        return self.vehicle.frame

    def build_engine(self):
        self.vehicle.engine = 2500
        return self.vehicle.engine

    def build_wheels(self):
        self.vehicle.wheels = 4
        return self.vehicle.wheels

    def build_doors(self):
        self.vehicle.doors = 4
        return self.vehicle.doors


class ScooterBuilder(Builder):
    def __init__(self):
        self.vehicle = Vehicle("Scooter")

    def build_frame(self):
        self.vehicle.frame = "Scooter frame"
        return self.vehicle.frame

    def build_engine(self):
        self.vehicle.engine = 50
        return self.vehicle.engine

    def build_wheels(self):
        self.vehicle.wheels = 2
        return self.vehicle.wheels

    def build_doors(self):
        self.vehicle.doors = 0
        return self.vehicle.doors
