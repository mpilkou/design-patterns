from abc import ABC, abstractmethod
import copy


class Prototype(ABC):

    def __init__(self):
        self.__name = None
        self.__value = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @abstractmethod
    def clone(self):
        return copy.copy(self)


class TypeAPrototype(Prototype):

    def __init__(self, value):
        self.name = "Type_1"
        self.value = value

    def __call__(self):
        return self.clone()

    def clone(self):
        return super().clone()


class TypeBPrototype(Prototype):

    def __init__(self, value):
        self.name = "Type_2"
        self.value = value

    def __call__(self):
        return self.clone()

    def clone(self):
        return super().clone()


class TypeBAPrototype(TypeBPrototype):

    def __init__(self, value):
        self.name = "Type_2_1"
        self.value = value

    def __call__(self):
        return self.clone()

    def clone(self):
        return super().clone()


class TypeBBPrototype(TypeBPrototype):

    def __init__(self, value):
        self.name = "Type_2_2"
        self.value = value

    def __call__(self):
        return self.clone()

    def clone(self):
        return super().clone()
