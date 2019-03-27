from factories.factory  import Factory
from elements.button    import LargeButton
from elements.header    import LargeHeader
from elements.image     import LargeImage
from elements.text      import LargeText

class LargeFactory(Factory):
    
    def createButton(self):
        return LargeButton()

    def createHeader(self):
        return LargeHeader()

    def createImage(self):
        return LargeImage()

    def createText(self):
        return LargeText()
    