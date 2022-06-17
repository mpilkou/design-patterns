import unittest
from bridge import PC, Laptop, Windows, Linux


class DecoratorTest(unittest.TestCase):

    def test_bridge(self):
        computer1 = PC(Windows())
        computer2 = PC(Windows())
        self.assertEqual(computer1.show_default_folder(), computer2.show_default_folder())
        computer1 = Laptop(Windows())
        computer2 = Laptop(Windows())
        self.assertEqual(computer1.show_default_folder(), computer2.show_default_folder())
        computer1 = PC(Linux())
        computer2 = PC(Linux())
        self.assertEqual(computer1.show_default_folder(), computer2.show_default_folder())
        computer1 = Laptop(Linux())
        computer2 = Laptop(Linux())
        self.assertEqual(computer1.show_default_folder(), computer2.show_default_folder())
        
    def test_abstract_in_bridge(self):
        computer1 = PC(Windows())
        computer1.connect_to_charge()
        computer2 = Laptop(Windows())
        self.assertEqual(computer1.show_default_folder(), computer2.show_default_folder())

        computer1 = PC(Linux())
        computer1.connect_to_charge()
        computer2 = Laptop(Linux())
        self.assertEqual(computer1.show_default_folder(), computer2.show_default_folder())

    def test_abstract(self):
        computer1 = PC(Windows())
        computer2 = Laptop(Windows())
        self.assertNotEqual(computer1.show_default_folder(), computer2.show_default_folder())
        computer1 = PC(Linux())
        computer2 = Laptop(Linux())
        self.assertNotEqual(computer1.show_default_folder(), computer2.show_default_folder())

        computer1 = Laptop(Windows())
        computer2 = Laptop(Linux())
        self.assertNotEqual(computer1.show_default_folder(), computer2.show_default_folder())

        computer1 = PC(Linux())
        computer2 = Laptop(Windows())
        self.assertNotEqual(computer1.show_default_folder(), computer2.show_default_folder())

    # def test_bridge_fun2(self):
    #     computer1 = Computer(Linux())
    #     computer2 = Computer(Linux())
    #     self.assertEqual(computer1.show_default_folder(), computer2.show_default_folder())

    # def test_bridge_fun3(self):
    #     computer1 = Computer(Windows())
    #     computer2 = Computer(Windows())
    #     self.assertEqual(computer1.show_default_folder(), computer2.show_default_folder())

if __name__ == '__main__':
    unittest.main()
