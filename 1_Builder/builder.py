from abc import abstractmethod
from parts import Vehicle


class Builder:

    @abstractmethod
    def BuildFrame(self):
        pass

    @abstractmethod
    def BuildEngine(self):
        pass

    @abstractmethod
    def BuildWheels(self):
        pass

    @abstractmethod
    def BuildDoors(self):
        pass


class MotorcycleBuilder(Builder):

    def __init__(self):
        self.vehicle = Vehicle("MotorCycle")

    def BuildFrame(self):
        self.vehicle.frame = "MotorCycle frame"
        return self.vehicle.frame

    def BuildEngine(self):
        self.vehicle.engine = 500
        return self.vehicle.engine

    def BuildWheels(self):
        self.vehicle.wheels = 2
        return self.vehicle.wheels

    def BuildDoors(self):
        self.vehicle.doors = 0
        return self.vehicle.doors


class CarBuilder(Builder):

    def __init__(self):
        self.vehicle = Vehicle("Car")

    def BuildFrame(self):
        self.vehicle.frame = "Car frame"
        return self.vehicle.frame

    def BuildEngine(self):
        self.vehicle.engine = 2500
        return self.vehicle.engine

    def BuildWheels(self):
        self.vehicle.wheels = 4
        return self.vehicle.wheels

    def BuildDoors(self):
        self.vehicle.doors = 4
        return self.vehicle.doors


class ScooterBuilder(Builder):
    def __init__(self):
        self.vehicle = Vehicle("Scooter")

    def BuildFrame(self):
        self.vehicle.frame = "Scooter frame"
        return self.vehicle.frame

    def BuildEngine(self):
        self.vehicle.engine = 50
        return self.vehicle.engine

    def BuildWheels(self):
        self.vehicle.wheels = 2
        return self.vehicle.wheels

    def BuildDoors(self):
        self.vehicle.doors = 0
        return self.vehicle.doors
