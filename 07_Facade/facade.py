from abc import ABC, abstractclassmethod


class _Fuel:

    def __init__(self, liters=0, limit=30):
        self._liters = liters
        self._limit = limit

    @property
    def liters(self):
        return self._liters

    @liters.setter
    def liters(self, liters):
        if self._liters + liters <= self._limit:
            self._liters += liters
        else:
            self._liters = self._limit


class _Engine:

    def __init__(self, liters_per_С_kilometr=10, fuel=_Fuel()):

        if type(fuel) is _Fuel:
            self._fuel = fuel
        else:
            self._fuel = _Fuel

        self._liters_per_С_kilometr = liters_per_С_kilometr

    @property
    def fuel(self):
        return self._fuel

    def start(self, km=100):
        fuel_needed = ((self._liters_per_С_kilometr * km) / 100)

        if fuel_needed > self.fuel.liters:
            print("Not enouth fuel")
            return None

        self.fuel.liters = -fuel_needed

        return self.fuel.liters


class _Lights:

    def __init__(self):
        self._lights = False

    def light_status(self):
        return self._lights

    def on(self):
        self._lights = True
        print("Lights on")

    def off(self):
        self._lights = False
        print("Lights off")


class Car:

    def __init__(self):
        self._engine = _Engine()
        self._lights = _Lights()

    def move(self, km):
        return self._engine.start(km)

    def lights(self, turn_on=False):
        if turn_on:
            self._lights.on()
        else:
            self._lights.off()

        return self._lights.light_status()

    def add_fuel(self, liters):
        self._engine._fuel.liters = liters
