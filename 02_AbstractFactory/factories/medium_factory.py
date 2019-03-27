from factories.factory  import Factory
from elements.button    import MediumButton
from elements.header    import MediumHeader
from elements.image     import MediumImage
from elements.text      import MediumText

class MediumFactory(Factory):
    
    def createButton(self):
        return MediumButton()

    def createHeader(self):
        return MediumHeader()

    def createImage(self):
        return MediumImage()

    def createText(self):
        return MediumText()
    