from elements.abstract_element import HTMLElement


class Header(HTMLElement):
    tag = "h"

    def __init__(self, parameters: str = ""):
        super().__init__(parameters)


class LargeHeader(Header):
    def __init__(self):
        Header.__init__(self, " size = 5 ")


class MediumHeader(Header):
    def __init__(self):
        Header.__init__(self, " size = 3 ")


class SmallHeader(Header):
    def __init__(self):
        Header.__init__(self, " size = 1 ")
