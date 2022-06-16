from abc import ABC, abstractmethod
from product import Vehicle


class Builder(ABC):

    def __init__(self) -> None:
        self.vehicle = None
        
    @abstractmethod
    def build_frame(self) -> None:
        pass

    @abstractmethod
    def build_engine(self) -> None:
        pass

    @abstractmethod
    def build_wheels(self) -> None:
        pass

    @abstractmethod
    def build_doors(self) -> None:
        pass

    def get_result(self):
        return self.vehicle


class MotorcycleBuilder(Builder):

    def __init__(self) -> None:
        self.vehicle = Vehicle("MotorCycle")

    def build_frame(self) -> None:
        self.vehicle.frame = "MotorCycle frame"

    def build_engine(self) -> None:
        self.vehicle.engine = 500

    def build_wheels(self) -> None:
        self.vehicle.wheels = 2

    def build_doors(self) -> None:
        self.vehicle.doors = 0


class CarBuilder(Builder):

    def __init__(self) -> None:
        self.vehicle = Vehicle("Car")

    def build_frame(self) -> None:
        self.vehicle.frame = "Car frame"

    def build_engine(self) -> None:
        self.vehicle.engine = 2500

    def build_wheels(self) -> None:
        self.vehicle.wheels = 4

    def build_doors(self) -> None:
        self.vehicle.doors = 4


class ScooterBuilder(Builder):
    def __init__(self) -> None:
        self.vehicle = Vehicle("Scooter")

    def build_frame(self) -> None:
        self.vehicle.frame = "Scooter frame"

    def build_engine(self) -> None:
        self.vehicle.engine = 50

    def build_wheels(self) -> None:
        self.vehicle.wheels = 2

    def build_doors(self) -> None:
        self.vehicle.doors = 0
