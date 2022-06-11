from elements.base_element import HTMLElement

class Text(HTMLElement):
    tag = "p"

    def __init__(self, parameters: str = ""):
        super().__init__(parameters)


class LargeText(Text):
    def __init__(self):
        Text.__init__(self, " size = 5 ")


class MediumText(Text):
    def __init__(self):
        Text.__init__(self, " size = 3 ")


class SmallText(Text):
    def __init__(self):
        Text.__init__(self, " size = 1 ")
