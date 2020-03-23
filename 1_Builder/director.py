from parts import Vehicle
from builder import Builder


class Director:
    _builder = None

    def __init__(self, builder: type(Builder)):
        self._builder = builder

    def build(self):
        vehicle = Vehicle(self._builder.vehicle)

        vehicle.engine = self._builder.BuildEngine()
        vehicle.frame = self._builder.BuildFrame()
        vehicle.wheels = self._builder.BuildWheels()
        vehicle.doors = self._builder.BuildDoors()

        return vehicle
