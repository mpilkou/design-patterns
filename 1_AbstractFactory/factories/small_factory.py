from factories.abstract_factory import Factory
from elements.button import SmallButton
from elements.header import SmallHeader
from elements.image import SmallImage
from elements.text import SmallText


class SmallFactory(Factory):

    def create_button(self):
        return SmallButton()

    def create_header(self):
        return SmallHeader()

    def create_image(self):
        return SmallImage()

    def create_text(self):
        return SmallText()
