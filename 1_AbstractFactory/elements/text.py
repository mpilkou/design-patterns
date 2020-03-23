

class Text():

    tag = "p"

    def __init__(self, parameters=""):
        self.parameters = parameters

    def get_html(self):
        return "<{0}{params}>  </{0}>".format(self.tag, params=self.parameters)


class LargeText(Text):
    def __init__(self):
        Text.__init__(self, " size = 5 ")


class MediumText(Text):
    def __init__(self):
        Text.__init__(self, " size = 3 ")


class SmallText(Text):
    def __init__(self):
        Text.__init__(self, " size = 1 ")
