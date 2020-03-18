from abc import ABC, abstractclassmethod


class Component(ABC):

    @abstractclassmethod
    def action_getCost(self):
        pass

    @abstractclassmethod
    def action_getIngridients(self):
        pass


class Coffe_component(Component):
    def action_getCost(self):
        return 3

    def action_getIngridients(self):
        return " espresso "


class Decorator(Component):

    def __init__(self, component):
        self._component = component

    def action_getCost(self):
        return self._component.action_getCost()

    def action_getIngridients(self):
        return self._component.action_getIngridients()


class Coffe_Decorator(Decorator):
    def __init__(self, component):
        self._component = component

    def action_getCost(self):
        return self._component.action_getCost()

    def action_getIngridients(self):
        return self._component.action_getIngridients()


class Whiped_Milk(Coffe_Decorator):
    def __init__(self, component):
        Coffe_Decorator.__init__(self, component)

    def action_getCost(self):
        return self._component.action_getCost() + 2

    def action_getIngridients(self):
        return self._component.action_getIngridients() + ", whiped milk "


class Vanilla(Coffe_Decorator):
    def __init__(self, component):
        Coffe_Decorator.__init__(self, component)

    def action_getCost(self):
        return self._component.action_getCost() + 1

    def action_getIngridients(self):
        return self._component.action_getIngridients() + ", vanilla "
