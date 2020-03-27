from abc import ABC, abstractclassmethod


class Component(ABC):

    @abstractclassmethod
    def action_get_cost(self):
        pass

    @abstractclassmethod
    def action_get_ingridients(self):
        pass


class CoffeComponent(Component):
    def action_get_cost(self):
        return 3

    def action_get_ingridients(self):
        return " espresso "


class Decorator(Component):

    def __init__(self, component):
        self._component = component

    def action_get_cost(self):
        return self._component.action_get_cost()

    def action_get_ingridients(self):
        return self._component.action_get_ingridients()


class CoffeDecorator(Decorator):
    def __init__(self, component):
        self._component = component

    def action_get_cost(self):
        return self._component.action_get_cost()

    def action_get_ingridients(self):
        return self._component.action_get_ingridients()


class Whiped_Milk(CoffeDecorator):
    def __init__(self, component):
        CoffeDecorator.__init__(self, component)

    def action_get_cost(self):
        return self._component.action_get_cost() + 2

    def action_get_ingridients(self):
        return self._component.action_get_ingridients() + ", whiped milk "


class Vanilla(CoffeDecorator):
    def __init__(self, component):
        CoffeDecorator.__init__(self, component)

    def action_get_cost(self):
        return self._component.action_get_cost() + 1

    def action_get_ingridients(self):
        return self._component.action_get_ingridients() + ", vanilla "
