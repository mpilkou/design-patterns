import unittest
import facade


class FacadeTest(unittest.TestCase):

    def test_facade_car_fuel_not_enouth(self):
        car = facade.Car()
        self.assertEqual(car.move(100), None)

    def test_facade_car_move(self):
        car = facade.Car()
        car.add_fuel(20)
        self.assertEqual(car.move(100), 10)

    def test_facade_car_lights(self):
        car = facade.Car()
        self.assertFalse(car.lights())
        self.assertTrue(car.lights(True))


if __name__ == '__main__':
    unittest.main()
