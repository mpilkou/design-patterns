from factories.factory  import Factory, mySingletonFun
from elements.button    import LargeButton
from elements.header    import LargeHeader
from elements.image     import LargeImage
from elements.text      import LargeText

class LargeFactory(Factory):
    instanse = None

    @mySingletonFun
    def createButton(self):
        return LargeButton()

    @mySingletonFun
    def createHeader(self):
        return LargeHeader()

    @mySingletonFun
    def createImage(self):
        return LargeImage()

    @mySingletonFun
    def createText(self):
        return LargeText()
    