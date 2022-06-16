

class Target():
    def request__devide(self, number_1, number_2):
        return number_1 / number_2


class Adaptee():
    def specific_request_round(self, number_1, number_2):
        return round(number_1, number_2)


class Adapter(Target):
    _adaptee = None

    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request__devide(self, number_1, number_2):
        return self._adaptee.specific_request_round(
            super().request__devide(number_1, number_2), 2)
