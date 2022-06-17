from abc import ABC, abstractclassmethod
from turtle import st

class OperatingSystem(ABC):
    
    @abstractclassmethod
    def get_user_folder(self) -> str:
        pass

class Linux(OperatingSystem):
    
    def get_user_folder(self) -> str:
        return '/home/newuser/'


class Windows(OperatingSystem):
    
    def get_user_folder(self) -> str:
        return 'C:\\Users\\NewUser\\'


class Computer:
    _is_charging = False
    def __init__(self, operating_system : OperatingSystem) -> None:
        self._operating_system = operating_system
    
    def show_default_folder(self):
        return self._operating_system.get_user_folder()

class Laptop(Computer):
    def __init__(self, operating_system : OperatingSystem) -> None:
        super().__init__(operating_system)

    def show_default_folder(self):
        return self._operating_system.get_user_folder()
    
class PC(Computer):
    def __init__(self, operating_system : OperatingSystem) -> None:
        super().__init__(operating_system)

    def connect_to_charge(self):
        self._is_charging = True

    def show_default_folder(self):
        return self._operating_system.get_user_folder() if self._is_charging else None
    
