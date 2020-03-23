from factories.factory import Factory, my_singleton_fun
from elements.button import SmallButton
from elements.header import SmallHeader
from elements.image import SmallImage
from elements.text import SmallText


class SmallFactory(Factory):
    instanse = None

    @my_singleton_fun
    def create_button(self):
        return SmallButton()

    @my_singleton_fun
    def create_header(self):
        return SmallHeader()

    @my_singleton_fun
    def create_image(self):
        return SmallImage()

    @my_singleton_fun
    def create_text(self):
        return SmallText()
