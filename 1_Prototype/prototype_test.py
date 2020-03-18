import unittest
import pickle as pic
import warnings

from multiprocessing.pool import ThreadPool as Pool

from prototype import Prototype, Type_1_Prototype, Type_2_Prototype
from prototype import Type_2_1_Prototype, Type_2_2_Prototype

# Python 2/3 compatibility
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    try:
        unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual
    except:
        print("Warning")


class PrototypeTest(unittest.TestCase):
    """Prototype"""

    def test_prototype_clone(self):
        type1 = Type_1_Prototype(123)
        self.assertEqual(type(Type_1_Prototype(321)), type(type1.clone()))

    def test_prototype_by_type_1(self):
        type1 = Type_1_Prototype(111)
        self.assertNotEqual(type1(), type1())

    def test_prototype_by_type_2(self):
        type2_1 = Type_2_1_Prototype(111)
        self.assertNotEqual(type2_1(), type2_1())


if __name__ == '__main__':
    unittest.main()
