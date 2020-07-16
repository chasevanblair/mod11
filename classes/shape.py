class Shape:
    """Shape class"""
    colors = ['BLUE', 'GREEN', 'ORANGE', 'PURPLE', 'RED', 'YELLOW']

    def __init__(self, color='BLUE'):
        if color not in self.colors:
            raise InvalidColorError
        self.color = color

    def change_color(self, new_color):
        if new_color not in self.colors:
            raise InvalidColorError
        self.color = new_color

    def __str__(self):
        return str(self.color)


class InvalidColorError(Exception):
    """InvalidColorError is derived class of Excpetion base class"""
    pass