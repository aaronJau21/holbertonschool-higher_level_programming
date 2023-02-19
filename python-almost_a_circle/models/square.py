#!/usr/bin/python3
""" Module that contains class Square
inheritance of class Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class inherit from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Init instances"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str dunder method """
        str_rectangle = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}".format(self.width, self.width)

        return str_rectangle + str_id + str_xy + str_wh

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update method"""
        if args and len(args):
            attributessquare = ['id', 'x', 'size', 'y']
            for i in range(len(args)):
                if attributessquare == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, attributessquare[i], args[i])
            for k, v in kwargs.items():
                if k == 'size':
                    setattr(self, 'width', v)
                    setattr(self, 'height', v)
                else:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Function that returns the dict representation of Square"""
        dcty = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return dcty