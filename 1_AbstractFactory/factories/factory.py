from abc import abstractmethod
from threading import Lock


def my_singleton_fun(function_to_do):

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
    def create_button(self):
        pass

    @abstractmethod
    def create_header(self):
        pass

    @abstractmethod
    def create_image(self):
        pass

    @abstractmethod
    def create_text(self):
        pass
