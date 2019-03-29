import unittest
import pickle as pic
import warnings

from multiprocessing.pool import ThreadPool as Pool

from director import Director
from builder import CarBuilder, MotorcycleBuilder, ScooterBuilder
from parts import Vehicle

# Python 2/3 compatibility
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    try:
        unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual
    except:
        print("Warning")

class BuilderTest(unittest.TestCase):
    """Builder"""

    def test_car_builder(self):

        builder = CarBuilder()
        director = Director(builder)

        car = director.build()
        car.print()

        dictionary = car.get()

        print(dictionary)

        self.assertEqual(dictionary["name"].name, "Car")
        self.assertEqual(dictionary["frame"], "Car frame")
        self.assertEqual(dictionary["engine"], 2500)
        self.assertEqual(dictionary["wheels"], 4)
        self.assertEqual(dictionary["doors"], 4)

    def test_motorcycle_builder(self):

        builder = MotorcycleBuilder()
        director = Director(builder)

        car = director.build()
        car.print()

        dictionary = car.get()

        print(dictionary)

        self.assertEqual(dictionary["name"].name, "MotorCycle")
        self.assertEqual(dictionary["frame"], "MotorCycle frame")
        self.assertEqual(dictionary["engine"], 500)
        self.assertEqual(dictionary["wheels"], 2)
        self.assertEqual(dictionary["doors"], 0)

    def test_scooter_builder(self):

        builder = ScooterBuilder()
        director = Director(builder)

        car = director.build()
        car.print()

        dictionary = car.get()

        print(dictionary)

        self.assertEqual(dictionary["name"].name, "Scooter")
        self.assertEqual(dictionary["frame"], "Scooter frame")
        self.assertEqual(dictionary["engine"], 50)
        self.assertEqual(dictionary["wheels"], 2)
        self.assertEqual(dictionary["doors"], 0)

if __name__ == '__main__':
    unittest.main()
