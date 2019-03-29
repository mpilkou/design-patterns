from parts import Vehicle

class Director:
    _builder = None

    def __init__(self, builder):
        self._builder = builder

    def build(self):
        vehicle = Vehicle(self._builder.vehicle)

        vehicle.engine = self._builder.BuildEngine()
        vehicle.frame = self._builder.BuildFrame()
        vehicle.wheels = self._builder.BuildWheels()
        vehicle.doors = self._builder.BuildDoors()

        return vehicle