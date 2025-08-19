class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distance_from_Xcoordinate(self):
        """
        This method finds the distance between a point and its X coordinates.

        Args:
            No
        Returns:
            float or int: distance.
        """
        return abs(self.y)

    def distance_from_Ycoordinate(self):
        """
        This method finds the distance between a point and its Y coordinates.

        Args:
            No
        Returns:
            float or int: distance.
        """
        return abs(self.x)

    def getQuadrant(self):
        """
        This method finds which quadrant the point is in.

        Args:
            No
        Returns:
            int: quadrant.
        """
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        else:
            return None

    def on_Xcoordinate(self):
        """
        This method checks for a point on the X coordinate.

        Args:
            No
        Returns:
            bool: result.
        """
        return self.x == 0

    def on_Ycoordinate(self):
        """
        This method checks for a point on the Y coordinate.

        Args:
            No
        Returns:
            bool: result.
        """
        return self.y == 0

p = Point(5, 4)
print(p.distance_from_Xcoordinate(), p.distance_from_Ycoordinate(), p.getQuadrant(), p.on_Xcoordinate(), p.on_Ycoordinate())