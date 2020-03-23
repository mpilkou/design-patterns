from abc import abstractmethod


class Button():

    tag = "button"

    def __init__(self, parameters=""):
        self.parameters = parameters

    @abstractmethod
    def get_html(self):
        return "<{0}{params}>  </{0}>".format(self.tag, params=self.parameters)


class LargeButton(Button):
    # def RedButton(self):
    #     self.tag = "button"
    def __init__(self):
        Button.__init__(self, " size = 5 ")


class MediumButton(Button):
    def __init__(self):
        Button.__init__(self, " size = 3 ")


class SmallButton(Button):
    def __init__(self):
        Button.__init__(self, " size = 1 ")
