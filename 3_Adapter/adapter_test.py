import unittest

import adapter_object
import adapter_two_way


class AdapterTest(unittest.TestCase):

    """Object Adapter"""
    def test_object_adaptee(self):
        adaptee = adapter_object.Adaptee()
        self.assertEqual(
            adaptee.specific_request_round(0.751683836273856564387, 2), 0.75)

    def test_object_target(self):
        target = adapter_object.Target()
        self.assertNotEqual(target.request__devide(3, 11), 0.27)

    def test_object_adapter(self):
        adaptee = adapter_object.Adaptee()
        adapter = adapter_object.Adapter(adaptee)
        self.assertEqual(adapter.request__devide(3, 11), 0.27)

    """Two-Way Adapter"""
    """string based adding"""
    def test_string_adapter(self):
        adapter = adapter_two_way.Adapter()
        self.assertEqual(adapter.request_add_string("111"), "1111")

    def test_string_to_int_adapter(self):
        adapter = adapter_two_way.Adapter()
        self.assertEqual(adapter.request_add_string(111), "1111")

    """integer based adding"""
    def test_int_adapter(self):
        adapter = adapter_two_way.Adapter()
        self.assertEqual(adapter.request_add_int(111), 112)

    def test_int_to_string_adapter(self):
        adapter = adapter_two_way.Adapter()
        self.assertEqual(adapter.request_add_int("111"), 112)


if __name__ == '__main__':
    unittest.main()
