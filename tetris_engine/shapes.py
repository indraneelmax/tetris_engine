

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

    def __repr__(self):
        return "Coordinate({},{})".format(self.row, self.col)

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col


class InShape(object):
    """
    Interface for a Shape in Tetris.
    """
    shape_type = ""

    def __init__(self, left_col=0):
        self.left_col = left_col

    def get_coordinates(self, pos_cord):
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
        raise NotImplementedError("Please implement!")

    def __repr__(self):
        return "InShape-{}{}".format(self.shape_type, self.left_col)


class QShape(InShape):

    shape_type = "Q"

    def __init__(self, left_col=0):
        super(QShape, self).__init__(left_col)

    def get_coordinates(self, pos_cord):
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
            Coordinate(row - 1, col + 1),
        ]


class ZShape(InShape):

    shape_type = "Z"

    def __init__(self, left_col=0):
        super(ZShape, self).__init__(left_col)

    def get_coordinates(self, pos_cord):
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
            Coordinate(row - 1, col + 1),
            Coordinate(row - 1, col + 2),
        ]


class SShape(InShape):

    shape_type = "S"

    def __init__(self, left_col=0):
        super(SShape, self).__init__(left_col)

    def get_coordinates(self, pos_cord):
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
            Coordinate(row, col + 1),
            Coordinate(row, col + 2),
            Coordinate(row - 1, col),
            Coordinate(row - 1, col + 1),
        ]


class TShape(InShape):

    shape_type = "T"

    def __init__(self, left_col=0):
        super(TShape, self).__init__(left_col)

    def get_coordinates(self, pos_cord):
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
            Coordinate(row, col + 2),
            Coordinate(row - 1, col + 1),
        ]


class IShape(InShape):

    shape_type = "I"

    def __init__(self, left_col=0):
        super(IShape, self).__init__(left_col)

    def get_coordinates(self, pos_cord):
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
            Coordinate(row, col + 2),
            Coordinate(row, col + 3),
        ]


class LShape(InShape):

    shape_type = "L"

    def __init__(self, left_col=0):
        super(LShape, self).__init__(left_col)

    def get_coordinates(self, pos_cord):
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
            Coordinate(row - 1, col),
            Coordinate(row - 2, col),
            Coordinate(row - 2, col + 1),
        ]


class JShape(InShape):

    shape_type = "J"

    def __init__(self, left_col=0):
        super(JShape, self).__init__(left_col)

    def get_coordinates(self, pos_cord):
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
            Coordinate(row, col + 1),
            Coordinate(row - 1, col + 1),
            Coordinate(row - 2, col),
            Coordinate(row - 2, col + 1),
        ]
