class Feet:
    def __init__(self, feet):
        self.feet = feet

    def __eq__(self, other):
        if isinstance(other, Feet):
            return self.feet == other.feet
        return False


class Inch:
    def __init__(self, inch):
        self.inch = inch

    def __eq__(self, other):
        return self.inch == other
