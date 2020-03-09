from abc import abstractmethod
from threading import Lock


def mySingletonFun(function_to_do):

    lock = Lock()

    def executer_function(self, *args, **kwargs):
        with lock:
            print("with lock")
            if(self.__class__.instanse is None):
                self.__class__.instanse = self

            return function_to_do(self.__class__.instanse, *args, **kwargs)

    return executer_function


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
