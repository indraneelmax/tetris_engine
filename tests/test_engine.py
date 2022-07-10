import pytest
import mock

from tetris_engine.engine import TetrisEngine
from tetris_engine.engine import State
from tetris_engine.engine import HEIGHT_INIT
from tetris_engine.shapes import Coordinate, InShape

TEST_MAX_ROWS = TEST_MAX_COLS = 3


@pytest.fixture(scope='module')
def grid():
    test_grid = []
    for row in range(TEST_MAX_ROWS):
        test_grid.append([State.UNOCCUPIED for col in range(TEST_MAX_COLS)])
    return test_grid


@pytest.fixture(scope='function')
def engine():
    test_engine = TetrisEngine(TEST_MAX_ROWS, TEST_MAX_COLS)
    return test_engine


def test_engine_initialize_grid_is_unoccupied(grid, engine):
    """
    Test on engine initialize the grid is unoccupied.
    """

    # Check if the grid is empty first!
    assert not engine._grid
    engine.initialize()
    # post initialize it should be unoccupied.
    assert engine._grid == grid
    # max height is 0
    assert engine.height == (HEIGHT_INIT + 1)


def test_is_coord_out_of_bounds_returns_true_for_out_coord(engine):
    """
    An out of bound coordinate tests false for is_coord_out_of_bounds.
    """
    out_of_row_coord = Coordinate(TEST_MAX_ROWS, TEST_MAX_COLS - 1)
    assert engine.is_coord_out_of_bounds(out_of_row_coord)
    out_of_col_coord = Coordinate(TEST_MAX_ROWS - 1, TEST_MAX_COLS)
    assert engine.is_coord_out_of_bounds(out_of_col_coord)
    in_bound_cord = Coordinate(0, 0)
    assert not engine.is_coord_out_of_bounds(in_bound_cord)


def test_is_unoccupied_returns_true_for_unoccupied(engine):
    """
    Test an unoccupied coordinate returns true for is_unoccupied.
    """
    all_coords = [Coordinate(row, col) for row in range(
        TEST_MAX_ROWS) for col in range(TEST_MAX_COLS)]
    engine.initialize()
    assert engine.is_unoccupied(all_coords)


def test_update_height_updates_height(engine):
    """
    Test update_height updates height.
    """
    assert engine.height == 0
    input_shape_coord = Coordinate(1, 0)
    engine.update_height(input_shape_coord)
    assert engine.height == input_shape_coord.row + 1

    # Test a newer height less than previous does not
    # change the engine height
    prev_height = engine.height
    input_shape_coord = Coordinate(0, 0)
    engine.update_height(input_shape_coord)
    assert engine.height == prev_height


def test_mark_coords_occupied_by_shape_marks_occupied(engine):
    """
    Test mark_coords_occupied_by_shape marks the coordinates as
    occupied.
    """
    engine.initialize()
    coords = [
        Coordinate(1, 0),
        Coordinate(1, 1),
        Coordinate(1, 2),
        Coordinate(0, 1),
    ]
    # Test that initially its UNOCCUPIED
    for coord in coords:
        row = coord.row
        col = coord.col
        assert engine._grid[row][col] == State.UNOCCUPIED

    engine.mark_coords_occupied_by_shape(coords)

    # Test that its now OCCUPIED
    for coord in coords:
        row = coord.row
        col = coord.col
        assert engine._grid[row][col] == State.OCCUPIED


def test_mark_coords_occupied_by_shape_marks_blocked(engine):
    """
    Test that mark_coords_occupied_by_shape marks coordinate under
    the shape coordinates as blocked if they are not already occupied.
    """
    engine.initialize()
    coords = [
        Coordinate(1, 0),
        Coordinate(1, 1),
    ]
    # Test that initially its UNOCCUPIED
    assert engine._grid[1][0] == State.UNOCCUPIED
    assert engine._grid[1][1] == State.UNOCCUPIED

    engine.mark_coords_occupied_by_shape(coords)

    # Test that its now OCCUPIED
    assert engine._grid[1][0] == State.OCCUPIED
    assert engine._grid[1][1] == State.OCCUPIED

    # Test that coordinates lower to it are now blocked.
    assert engine._grid[0][0] == State.BLOCKED
    assert engine._grid[0][1] == State.BLOCKED

    coords = [
        Coordinate(2, 1),
        Coordinate(2, 2),
    ]

    # Test that initially its UNOCCUPIED
    assert engine._grid[2][1] == State.UNOCCUPIED
    assert engine._grid[2][2] == State.UNOCCUPIED

    engine.mark_coords_occupied_by_shape(coords)

    # Test that its now OCCUPIED
    assert engine._grid[2][1] == State.OCCUPIED
    assert engine._grid[2][2] == State.OCCUPIED

    # Test that it lower one are blocked except which
    # were already occupied.
    assert engine._grid[1][1] == State.OCCUPIED
    assert engine._grid[1][2] == State.BLOCKED
    assert engine._grid[0][2] == State.BLOCKED


def test_remove_rows_shifts_rows_below(engine):
    """
    Test that remove_row copies rows to lower rows.
    """
    engine.initialize()
    coords = [
        Coordinate(2, 1),
        Coordinate(1, 0),
        Coordinate(1, 1),
        Coordinate(1, 2),
        Coordinate(0, 0),
    ]

    # set the coords to occupied
    for coord in coords:
        row = coord.row
        col = coord.col
        engine._grid[row][col] = State.OCCUPIED
    # set the expect coords to blocked.
    engine._grid[0][1] = State.BLOCKED
    engine._grid[0][2] = State.BLOCKED
    # keep a copy of the row that will be shifted down
    row_idx2 = engine._grid[2][:]
    # keep a copy of the row that is not to be shifted
    row_idx0 = engine._grid[0][:]

    # make sure to update the height
    engine.update_height(Coordinate(2, 1))
    old_height = engine.height
    engine.check_and_remove_filled_rows()
    assert engine._grid[1] == row_idx2
    assert engine._grid[0] == row_idx0
    # make sure the height is reduced as well.
    assert engine.height == old_height - 1


def test_process_input_place_shape(engine):
    """
    Test that process_input places a shape and returns
    the top left coordinate (of its bbox).
    """
    engine.initialize()
    input_shape = mock.Mock(spec=InShape)
    coords = [
        Coordinate(2, 1),
        Coordinate(1, 0),
        Coordinate(1, 1),
    ]
    mock_highest_unoccupied_row = mock.Mock()
    input_shape.get_coordinates.return_value = coords
    mock_highest_unoccupied_row.return_value = 2
    # This should make it place at row 2
    engine.get_highest_unoccupied_row = mock_highest_unoccupied_row
    # Try to place this shape at col 0
    place_col = 0
    input_shape.left_col = place_col
    placed_coord = engine.process_input(input_shape)
    assert placed_coord == Coordinate(2, place_col)
    assert engine.height == 3
