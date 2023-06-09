#!/usr/bin/python3
"""defining a base class"""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented, error is raise"""
        raise Exception("area() is not implemented")
