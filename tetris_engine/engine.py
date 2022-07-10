
from tetris_engine.shapes import Coordinate

# for coordinates that are used by a shape.
OCCUPIED = 1
# for coordinates that are free to use.
UNOCCUPIED = 0
# for coordinates that cannot be used a shape.
BLOCKED = -1

GRID_MAX_ROWS = 10
GRID_MAX_COLS = 10


class TetrisEngine(object):
    """
    Implements a Simple Tetris Engine that takes
    six types of shapes (Q,Z,S,T,I,J).
    """

    def __init__(self, tot_rows=GRID_MAX_ROWS, tot_cols=GRID_MAX_COLS):
        """
        Args:
            tot_rows (int): Tot rows in the Grid.
            tot_cols (int): Tot columns in the Grid.
        """
        self.rows = tot_rows
        self.cols = tot_cols
        self.__height = 0  # The current max height
        self._grid = []

    def initialize(self):
        """
        Reset/Initialize the Engine.
        """
        print("\n Initializing Engine...")
        self._grid = []
        for _row in range(self.rows):
            cols = [UNOCCUPIED for col in range(self.cols)]
            self._grid.append(cols)
        # print(self._grid)

    @property
    def height(self):
        """Return the current max height of the grid"""
        return self.__height

    def get_highest_unoccupied_row(self, col):
        """
        Returns the highest unoccupied row for the given
        column in the grid.

        Args:
            col (int): The column value.

        Returns:
            int: The highest unoccupied row for given column.
        """
        for row in range(self.rows):
            coord = Coordinate(row, col)
            if self.is_unoccupied([coord]):
                return row
        raise Exception(
            "Cannot find highest onoccupied row for col {}".format(col))

    def process_input(self, input_shape):
        """
        Process a new input.

        Args:
            input_shape (InShape): An instance of InShape.
        """
        start_col = input_shape.left_col
        start_row = self.get_highest_unoccupied_row(start_col)
        # print("Highes row - {}".format(start_row))
        coords_to_occupy = input_shape.get_coordinates(
            Coordinate(start_row, start_col))
        can_occupy = self.is_unoccupied(coords_to_occupy)
        row = start_row
        while not can_occupy and row < GRID_MAX_ROWS:
            row += 1
            coords_to_occupy = input_shape.get_coordinates(
                Coordinate(row, start_col))
            can_occupy = self.is_unoccupied(coords_to_occupy)
            # print(
            #     "{} Coord to occupy - {}".format(Coordinate(row, start_col), coords_to_occupy))
        if row == GRID_MAX_ROWS:
            raise Exception("{} - Input cannot be placed".format(input_shape))
        # We have found the row where it can be placed, so now mark the
        # coords occupied. Also mark all coordinates underneath the shape
        # as blocked.
        self.mark_coords_occupied_by_shape(coords_to_occupy)
        # print(self._grid)
        return Coordinate(row, start_col)

    def mark_coords_occupied_by_shape(self, coords):
        """
        Mark the given coordinates occupied by an input in the grid.

        Args:
            coords (list(Coordinate)): A list of Coordinate to mark occupied.
        """
        for coord in coords:
            row = coord.row
            col = coord.col
            while(row >= 0):
                if self._grid[row][col] != OCCUPIED:
                    # do not overwrite the one used by an input.
                    self._grid[row][col] = BLOCKED
                    # print("Marked {} BLOCKED".format(Coordinate(row, col)))
                row = row - 1
            # mark the current input's coordinate as occupied.
            self._grid[coord.row][coord.col] = OCCUPIED
            # print("Marked {} OCCUPIED".format(coord))

    def is_unoccupied(self, coords):
        """
        Args:
            coords (list(Coordinate)): A list of Coordinates to check.

        Returns:
            bool: True if they can be occupied in the Grid else False.
        """

        for coord in coords:
            row = coord.row
            col = coord.col
            # print("Checking for occupancy - {}".format(coord), end=' ')
            if self.is_coord_out_of_bounds(coord):
                return False
            # print(self._grid[row][col])
            if self._grid[row][col] != UNOCCUPIED:
                return False
        return True

    def is_coord_out_of_bounds(self, coord):
        """
        Check if the given coordinate is within bounds.

        Args:
            coord (Coordinate): A coordinate to check.
        Returns:
            bool: True if within bounds else False.
        """
        row = coord.row
        col = coord.col
        if row >= self.rows or row < 0:
            return True
        if col >= self.cols or col < 0:
            return True
        return False
