# from abc import abstractmethod


class Image():

    tag = "image"

    def __init__(self, parameters=""):
        self.parameters = parameters

    def get_html(self):
        return "<{0}{params}>  </{0}>".format(self.tag, params=self.parameters)


class LargeImage(Image):
    def __init__(self):
        Image.__init__(self, " size = 5 ")


class MediumImage(Image):
    def __init__(self):
        Image.__init__(self, " size = 3 ")


class SmallImage(Image):
    def __init__(self):
        Image.__init__(self, " size = 1 ")
