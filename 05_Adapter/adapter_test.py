import unittest
import pickle as pic
import warnings

from multiprocessing.pool import ThreadPool as Pool

from adapter import Adapter, Adaptee, Target

# Python 2/3 compatibility
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    try:
        unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual
    except:
        print("Warning")

class AdapterTest(unittest.TestCase):
    """Adapter"""

    def test_adaptee(self):
        adaptee = Adaptee()
        self.assertEqual(adaptee.specificRequest_round(0.751683836273856564387),0.75)

    def test_target(self):
        target = Target()
        self.assertNotEqual(target.request__devide(3,11),0.27)


    def test_adapter(self):
        adaptee = Adaptee()
        adapter = Adapter(adaptee)
        self.assertEqual(adapter.request__devide(3,11),0.27)

if __name__ == '__main__':
    unittest.main()
