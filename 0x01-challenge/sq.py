#!/usr/bin/python3
"""Define a model for a Square class"""


class square():
    """A Square class"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """initilaize data for the squar"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ return parametars of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ print the param of the square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ Create a square object """
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
