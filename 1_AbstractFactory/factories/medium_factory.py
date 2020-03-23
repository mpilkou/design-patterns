from factories.factory import Factory, my_singleton_fun
from elements.button import MediumButton
from elements.header import MediumHeader
from elements.image import MediumImage
from elements.text import MediumText


class MediumFactory(Factory):
    instanse = None

    @my_singleton_fun
    def create_button(self):
        return MediumButton()

    @my_singleton_fun
    def create_header(self):
        return MediumHeader()

    @my_singleton_fun
    def create_image(self):
        return MediumImage()

    @my_singleton_fun
    def create_text(self):
        return MediumText()
