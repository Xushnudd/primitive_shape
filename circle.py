import math
class Circle:
    def __init__(self, r) -> None:
        self.r = r

    def getArea(self):
        """
        This method finds the area of the Circle.

        Args:
            No
        Returns:
            float or int: result.
        """
        return round(math.pi * self.r ** 2, 2)

    def getLength(self):
        """
        This method finds the length of the cirle.

        Args:
            No
        Returns:
            float or int: result..
        """
        return round(2 * math.pi * self.r, 2)

c = Circle(5)
print(c.getArea(), c.getLength())