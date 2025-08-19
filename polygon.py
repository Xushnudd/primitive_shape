class Polygon:
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

    def getArea(self):
        """
        This method finds the area of the Polygon.

        Args:
            No
        Returns:
            float or int: return perimeter of the polygon.
        """
        return self.height * self.width

    def getPerimeter(self):
        """
        This method finds the perimeter of the Polygon.

        Args:
            No
        Returns:
            float or int: return perimeter of the polygon.
        """
        return 2 * (self.height + self.width)
p = Polygon(12, 24)
#print(p.getArea(), p.getPerimeter())