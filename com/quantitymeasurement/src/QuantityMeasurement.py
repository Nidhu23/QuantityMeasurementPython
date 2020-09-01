class QuantityMeasurer:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, QuantityMeasurer):
            return self.value == other.value
        return False
