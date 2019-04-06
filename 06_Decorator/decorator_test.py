import unittest
import decorator

# Python 2/3 compatibility
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    try:
        unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual
    except:
        print("Warning")

class DecoratorTest(unittest.TestCase):
    def test_decorator_fun1(self):
        coffe = decorator.Coffe_component()
        coffee_milk = decorator.Whiped_Milk(coffe)
        coffee_milk_vanilla = decorator.Vanilla(coffee_milk)
        self.assertEqual(coffee_milk_vanilla.action_getCost(), 6)

    def test_decorator_fun2(self):
        coffe = decorator.Coffe_component()
        coffee_milk = decorator.Whiped_Milk(coffe)
        coffee_milk_vanilla = decorator.Vanilla(coffee_milk)
        self.assertEqual(coffee_milk_vanilla.action_getIngridients(), ' espresso , whiped milk , vanilla ')
    

if __name__ == '__main__':
    unittest.main()
