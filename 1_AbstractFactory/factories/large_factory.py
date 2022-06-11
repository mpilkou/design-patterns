from factories.abstract_factory import Factory
from elements.button import LargeButton
from elements.header import LargeHeader
from elements.image import LargeImage
from elements.text import LargeText


class LargeFactory(Factory):

    def create_button(self):
        return LargeButton()

    def create_header(self):
        return LargeHeader()

    def create_image(self):
        return LargeImage()

    def create_text(self):
        return LargeText()
