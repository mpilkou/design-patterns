from factories.factory import Factory, my_singleton_fun
from elements.button import LargeButton
from elements.header import LargeHeader
from elements.image import LargeImage
from elements.text import LargeText


class LargeFactory(Factory):

    instanse = None

    @my_singleton_fun
    def create_button(self):
        return LargeButton()

    @my_singleton_fun
    def create_header(self):
        return LargeHeader()

    @my_singleton_fun
    def create_image(self):
        return LargeImage()

    @my_singleton_fun
    def create_text(self):
        return LargeText()
