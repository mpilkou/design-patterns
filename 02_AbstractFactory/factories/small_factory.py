from factories.factory import Factory, mySingletonFun
from elements.button import SmallButton
from elements.header import SmallHeader
from elements.image import SmallImage
from elements.text import SmallText


class SmallFactory(Factory):
    instanse = None

    @mySingletonFun
    def createButton(self):
        return SmallButton()

    @mySingletonFun
    def createHeader(self):
        return SmallHeader()

    @mySingletonFun
    def createImage(self):
        return SmallImage()

    @mySingletonFun
    def createText(self):
        return SmallText()
