from factories.abstract_factory import Factory
from elements.button import MediumButton
from elements.header import MediumHeader
from elements.image import MediumImage
from elements.text import MediumText


class MediumFactory(Factory):

    def create_button(self):
        return MediumButton()

    def create_header(self):
        return MediumHeader()

    def create_image(self):
        return MediumImage()

    def create_text(self):
        return MediumText()
