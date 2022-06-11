from elements.base_element import HTMLElement

class Image(HTMLElement):

    tag = "image"

    def __init__(self, parameters: str = ""):
        super().__init__(parameters)


class LargeImage(Image):
    def __init__(self):
        Image.__init__(self, " size = 5 ")


class MediumImage(Image):
    def __init__(self):
        Image.__init__(self, " size = 3 ")


class SmallImage(Image):
    def __init__(self):
        Image.__init__(self, " size = 1 ")
