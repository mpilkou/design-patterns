import unittest
import decorator


class DecoratorTest(unittest.TestCase):

    def test_decorator_fun1(self):
        coffe = decorator.CoffeComponent()
        coffee_milk = decorator.Whiped_Milk(coffe)
        coffee_milk_vanilla = decorator.Vanilla(coffee_milk)
        self.assertEqual(coffee_milk_vanilla.action_get_cost(), 6)

    def test_decorator_fun2(self):
        coffe = decorator.CoffeComponent()
        coffee_milk = decorator.Whiped_Milk(coffe)
        coffee_milk_vanilla = decorator.Vanilla(coffee_milk)

        self.assertEqual(
            coffee_milk_vanilla.action_get_ingridients(),
            ' espresso , whiped milk , vanilla ')


if __name__ == '__main__':
    unittest.main()
