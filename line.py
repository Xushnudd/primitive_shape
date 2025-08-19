class Line:
    def __init__(self, x1, y1, x2, y2) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_length(self):
        """
        This method finds the length of line.

        Args:
            No
        Returns:
            float or int: distance.
        """
        x = self.x1 + abs(self.x2)
        y = self.y1 + abs(self.y2)
        return f"X = {x} sm | Y = {y} sm"
l = Line(5, 4, -5, -4)
line = l.get_length()
print(line)