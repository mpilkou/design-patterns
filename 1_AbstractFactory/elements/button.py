from elements.abstract_element import HTMLElement

class Button(HTMLElement):
    tag = "button"

    def __init__(self, parameters: str = ""):
        super().__init__(parameters)

class LargeButton(Button):
    def __init__(self):
        Button.__init__(self, " size = 5 ")


class MediumButton(Button):
    def __init__(self):
        Button.__init__(self, " size = 3 ")


class SmallButton(Button):
    def __init__(self):
        Button.__init__(self, " size = 1 ")
