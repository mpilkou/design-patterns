from factories.factory import Factory, mySingletonFun
from elements.button import MediumButton
from elements.header import MediumHeader
from elements.image import MediumImage
from elements.text import MediumText


class MediumFactory(Factory):
    instanse = None

    @mySingletonFun
    def createButton(self):
        return MediumButton()

    @mySingletonFun
    def createHeader(self):
        return MediumHeader()

    @mySingletonFun
    def createImage(self):
        return MediumImage()

    @mySingletonFun
    def createText(self):
        return MediumText()
