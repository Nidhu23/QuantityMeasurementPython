import enum


class QuantityMeasurer:
    def __init__(self, unit, value):
        self.__value = value
        self.__unit = unit

    def __eq__(self, other):
        if isinstance(other, QuantityMeasurer):
            return self.__value == other.__value
        return False

    def compare(self, other):
        if self.__unit.__class__ == other.__unit.__class__:
            if self.__unit.__class__.convert(self.__unit, self.__value) == other.__unit.__class__.convert(other.__unit,
                                                                                                          other.__value):
                return True
        return False

    def add(self, other):
        if isinstance(self.__unit, Lengths) and isinstance(other.__unit, Lengths):
            return Lengths.convert(self.__unit, self.__value) + Lengths.convert(other.__unit, other.__value)
        return 0


class Lengths(enum.Enum):
    FEET = 12.0
    INCH = 1.0
    YARD = 36.0
    CM = 0.4

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        return self.unit * value


class Volumes(enum.Enum):
    LITRE = 1.0
    GALLON = 3.78
    ML = 0.001

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        return self.unit * value
