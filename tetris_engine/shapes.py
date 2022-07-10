

from turtle import left


class Coordinate(object):
    """
    Represents a cell in the Grid.
    """

    def __init__(self, row, col):
        """
        Args:
            row (int): The row.
            col (int): The column.
        """
        self.row = row
        self.col = col


class IShape(object):
    """
    Interface for a Shape in Tetris.
    """
    shape_type = ""

    def __init__(self, left_col=0):
        self.left_col = left_col
        pass

    def get_occupied_cells(pos_cord):
        """
        Retruns a list of coordinates that are occupied by
        the shape based on the input coordinate representing
        the position of the shape.

        Args:
            pos_cord (Coordinate): Top left coordinate representing
              the position of the shape.
        Returns:
            list(Coordinate): List of Coordinates occupied by the
              shape.
        """
        raise NotImplementedError("")


class QShape(IShape):

    shape_type = "Q"

    def __init__(self, left_col=0):
        super(QShape, self).__init__(left_col)

    def get_occupied_cells(pos_cord):
        """
        Args:
            pos_cord (Coordinate): Top left coordinate representing
              the position of the shape.
        Returns:
            list(Coordinate): List of Coordinates occupied by the
              shape.
        """
        row = pos_cord.row
        col = pos_cord.col
        return [
            Coordinate(row, col),
            Coordinate(row, col + 1),
            Coordinate(row - 1, col),
            Coordinate(row - 1, col - 1),
        ]


class ZShape(IShape):

    shape_type = "Z"

    def __init__(self, left_col=0):
        super(ZShape, self).__init__(left_col)


class SShape(IShape):

    shape_type = "S"

    def __init__(self, left_col=0):
        super(SShape, self).__init__(left_col)


class TShape(IShape):

    shape_type = "T"

    def __init__(self, left_col=0):
        super(TShape, self).__init__(left_col)


class IShape(IShape):

    shape_type = "I"

    def __init__(self, left_col=0):
        super(IShape, self).__init__(left_col)


class JShape(IShape):

    shape_type = "J"

    def __init__(self, left_col=0):
        super(JShape, self).__init__(left_col)
