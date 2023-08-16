class BoardOutException(Exception):

    def __str__(self):
        return 'coordinate out of the field'


class Dot:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return [self.x, self.y] == other

    def __str__(self):
        return str([self.x, self.y])


class Ship:

    def __init__(self, length, coordinate, direction, spots):
        self.length = length
        self.direction = direction
        self.spots = spots
        self.coordinate = coordinate

    @property
    def coordinate(self):
        return self._coordinate

    @coordinate.setter
    def coordinate(self, coordinate):
        if self.direction == 'vertical':
            if self.length - 1 + coordinate[1] > 6 or coordinate[0] > 6:
                raise BoardOutException
        elif self.direction == 'horizontal':
            if self.length - 1 + coordinate[0] > 6 or coordinate[1] > 6:
                raise BoardOutException
        self._coordinate = coordinate

    def dots(self):
        if self.direction == 'vertical':
            return [[self.coordinate[0], self.coordinate[1] + i] for i in range(self.length)]
        elif self.direction == 'horizontal':
            return [[self.coordinate[0] + i, self.coordinate[1]] for i in range(self.length)]


class Board:

    sheet = [[i, j]]

    def __init__(self):


#s = Ship(3, [4, 5], 'horizontal', 3)
