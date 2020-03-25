import unittest

from multiprocessing.pool import ThreadPool as Pool

from prototype import TypeAPrototype, TypeBPrototype
from prototype import TypeBAPrototype, TypeBBPrototype


class PrototypeTest(unittest.TestCase):
    """Prototype"""

    def test_prototype_clone(self):
        type1 = TypeAPrototype(123)
        self.assertEqual(type(TypeAPrototype(321)), type(type1.clone()))

    def test_prototype_by_type_1(self):
        type1 = TypeAPrototype(111)
        self.assertNotEqual(type1(), type1())

    def test_prototype_by_type_2(self):
        type2_1 = TypeBAPrototype(111)
        self.assertNotEqual(type2_1(), type2_1())


if __name__ == '__main__':
    unittest.main()
