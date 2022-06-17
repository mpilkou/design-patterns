import unittest

import adapter_object
import adapter_two_way


class AdapterTest(unittest.TestCase):

    """Object Adapter"""
    def test_object_adapler(self):
        adaptee = adapter_object.Adaptee()

        self.assertEqual(
            adapter_object.Adapter(adaptee).request(0.751683836273856564387, 2), 
            round(0.751683836273856564387, 2))


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
