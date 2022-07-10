
from enum import Enum

from tetris_engine.exceptions import TetrisEngineException
from tetris_engine.log import get_logger
from tetris_engine.shapes import Coordinate


logger = get_logger(__name__)


class State(Enum):
    # for coordinates that are used by a shape.
    OCCUPIED = 1
    # for coordinates that are free to use.
    UNOCCUPIED = 0
    # for coordinates that cannot be used a shape.
    BLOCKED = -1


GRID_MAX_ROWS = 10
GRID_MAX_COLS = 10
HEIGHT_INIT = -1


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
        self.__height = HEIGHT_INIT  # The current max height
        self._grid = []

    def initialize(self):
        """
        Reset/Initialize the Engine.
        """
        logger.info("Initializing Engine...")
        self._grid = []
        self.__height = HEIGHT_INIT
        for _row in range(self.rows):
            cols = [State.UNOCCUPIED for col in range(self.cols)]
            self._grid.append(cols)

    @property
    def height(self):
        """Return the current max height of the grid"""
        # we start row with index 0 hence one extra
        return self.__height + 1

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
        raise TetrisEngineException(
            "Cannot find highest onoccupied row for col {}".format(col))

    def process_input(self, input_shape):
        """
        Process a new input.

        Args:
            input_shape (InShape): An instance of InShape.

        Returns:
            Coordinate : The Coordinate at which the input shape
              is placed.
        """
        start_col = input_shape.left_col
        start_row = self.get_highest_unoccupied_row(start_col)
        coords_to_occupy = input_shape.get_coordinates(
            Coordinate(start_row, start_col))
        can_occupy = self.is_unoccupied(coords_to_occupy)
        row = start_row
        while not can_occupy and row < GRID_MAX_ROWS:
            row += 1
            coords_to_occupy = input_shape.get_coordinates(
                Coordinate(row, start_col))
            can_occupy = self.is_unoccupied(coords_to_occupy)
        if row == GRID_MAX_ROWS:
            raise TetrisEngineException(
                "{} - Input cannot be placed".format(input_shape))
        # We have found the row where it can be placed, so now mark the
        # coords occupied. Also mark all coordinates underneath the shape
        # as blocked if not already occupied.
        self.mark_coords_occupied_by_shape(coords_to_occupy)
        # print(self._grid)
        input_shape_coord = Coordinate(row, start_col)
        logger.info("Placed {} at {}".format(input_shape, input_shape_coord))
        self.update_height(input_shape_coord)
        self.check_and_remove_filled_rows()
        return input_shape_coord

    def update_height(self, input_shape_coord):
        """
        Calculate and Update the max height of the grid.

        Args:
            input_shape_coord (Coordinate): The Coordinate at which
              the last input shape was placed.
        """
        row = input_shape_coord.row
        if self.__height < row:
            self.__height = row

    def mark_coords_occupied_by_shape(self, coords):
        """
        Mark the given coordinates occupied by an input in the grid.

        Args:
            coords (list(Coordinate)): A list of Coordinate to mark occupied.
        """
        # Also mark all coordinates underneath the shape
        # as blocked if not already occupied.
        for coord in coords:
            row = coord.row
            col = coord.col
            while(row >= 0):
                if self._grid[row][col] != State.OCCUPIED:
                    # do not overwrite the one used by an input.
                    self._grid[row][col] = State.BLOCKED
                    # print("Marked {} BLOCKED".format(Coordinate(row, col)))
                row = row - 1
            # mark the current input's coordinate as occupied.
            self._grid[coord.row][coord.col] = State.OCCUPIED
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
            if self.is_coord_out_of_bounds(coord):
                return False
            if self._grid[row][col] != State.UNOCCUPIED:
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

    def check_and_remove_filled_rows(self):
        """
        Check and remove a row which has all cells
        occupied.
        """
        # we only check till the max height of the grid
        for row in range(self.height):
            all_occupied = all(
                [self._grid[row][col] == State.OCCUPIED for col in range(self.cols)])
            if all_occupied:
                logger.info("Row - {} to be removed".format(row))
                self.remove_row(row)

    def remove_row(self, row):
        """
        Remove a given row from the grid.

        Args:
            row (int): The row.
        """
        # We copy the higher row to lower row until max height.
        for cur_row in range(row + 1, self.height):
            self._grid[cur_row - 1] = self._grid[cur_row]

        # Now just reinitialize the height row with unoccupied.
        self._grid[self.__height] = [
            State.UNOCCUPIED for col in range(self.cols)]
        # reduce the max height too.
        self.__height -= 1
