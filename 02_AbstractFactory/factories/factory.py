from abc import abstractmethod

class Factory:
    @abstractmethod
    def createButton(self):
        pass

    @abstractmethod
    def createHeader(self):
        pass

    @abstractmethod
    def createImage(self):
        pass
    
    @abstractmethod
    def createText(self):
        pass