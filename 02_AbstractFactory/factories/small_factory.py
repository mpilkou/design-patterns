from factories.factory  import Factory
from elements.button    import SmallButton
from elements.header    import SmallHeader
from elements.image     import SmallImage
from elements.text      import SmallText

class SmallFactory(Factory):
    
    def createButton(self):
        return SmallButton()

    def createHeader(self):
        return SmallHeader()

    def createImage(self):
        return SmallImage()

    def createText(self):
        return SmallText()
    