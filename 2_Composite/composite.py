from abc import ABC, abstractclassmethod

class Graphic(ABC):
    _figure = [
        [' ',' ',' ',],
        [' ',' ',' ',],
        [' ',' ',' ',],
    ]
    @abstractclassmethod
    def draw(self):
        pass

class Line(Graphic):
    _figure = [
        [' ',' ','/',],
        [' ','/',' ',],
        ['/',' ',' ',],
    ]

    def draw(self):
        return self._figure

class Squere(Graphic):
    _figure = [
        ['+','-','+',],
        ['|',' ','|',],
        ['+','-','+',],
    ]

    def draw(self):
        return self._figure

class Text(Graphic):
    _figure = [
        [' ',' ',' ',],
        ['T','X','T',],
        [' ',' ',' ',],
    ]
    def draw(self):
        return self._figure

class Picture(Graphic):
    _graphics_list = []

    def __generate_compose_figure(self, graphic_item_top):
        for row in range(3):
            for col in range(3):
                if graphic_item_top[row][col] != ' ':
                    self._figure[row][col] = graphic_item_top[row][col]

    def draw(self):
        if len(self._graphics_list) == 0:
            return self._figure

        for graphic_item in self._graphics_list:
            self.__generate_compose_figure(graphic_item.draw())
        return self._figure
            

                
    def add(self, component : Graphic) -> None:
        self._graphics_list.append(component)

    def remove(self, component : Graphic) -> None:
        self._graphics_list.remove(component)

    def get_child(self, component_key : int) -> Graphic:
        return self._graphics_list[component_key]