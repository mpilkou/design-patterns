from abc import abstractmethod


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
