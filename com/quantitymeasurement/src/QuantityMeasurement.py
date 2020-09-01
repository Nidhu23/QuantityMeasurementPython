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
        if isinstance(self.__unit, Lengths) and isinstance(other.__unit, Lengths):
            if Lengths.convert(self.__unit, self.__value) == Lengths.convert(other.__unit, other.__value):
                return True
        return False


class Lengths(enum.Enum):
    FEET = 12.0
    INCH = 1.0
    YARD = 36.0

    def __init__(self, unit):
        self.unit = unit

    def convert(self, value):
        return self.unit * value
