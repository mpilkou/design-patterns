import unittest

from multiprocessing.pool import ThreadPool as Pool

from prototype import TypeAPrototype, TypeBPrototype

def get_prototype_copy_thread_with_seted_value(prototype):
    """Help fun"""
    prototype.value = 10
    return prototype

def get_prototype_copy_thread(prototype):
    """Help fun"""
    return prototype.clone()

class PrototypeTest(unittest.TestCase):
    """Prototype"""

    def test_prototype_clone(self):
        type1 = TypeAPrototype(123)
        self.assertEqual(type(TypeAPrototype(321)), type(type1.clone()))

    def test_prototype_by_type_1(self):
        type1 = TypeAPrototype(111)
        self.assertNotEqual(type1.clone(), type1.clone())

    def test_prototype_by_type_2(self):
        type2_1 = TypeBPrototype(111)
        type2_2 = type2_1.clone()
        self.assertNotEqual(type2_1(), type2_2())
    
    def test_prototype_by_type_2(self):
        type2_1 = TypeBPrototype(111)
        type2_2 = type2_1.clone()
        type2_2.value = 222
        self.assertNotEqual(type2_1.value, type2_2.value)
    
    def test_relative_copy(self):
        pool1 = Pool(processes=1)
        pool2 = Pool(processes=1)
        type1 = TypeAPrototype(111)
        self.assertEqual(
            pool1.apply_async(get_prototype_copy_thread_with_seted_value, args = [type1, ]).get().value,
            pool2.apply_async(get_prototype_copy_thread, args = [type1, ]).get().value)
        pool1.close()
        pool2.close()


if __name__ == '__main__':
    unittest.main()
