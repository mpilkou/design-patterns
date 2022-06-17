from abc import ABC, abstractclassmethod


class Target(ABC):
    @abstractclassmethod
    def request(self, number_1 : object, number_2 : int ) -> float:
        pass


class Adaptee():
    def specific_request(self, number : object) -> float:
        return number / 10


class Adapter(Target):
    _adaptee = None

    def __init__(self, adaptee : Adaptee):
        self._adaptee = adaptee

    def request(self, number_1 : object, number_2 : int ) -> float:
        number_1 = self._adaptee.specific_request(number = number_1) * 10
        return round(number_1, number_2)
