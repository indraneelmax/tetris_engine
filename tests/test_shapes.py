from tetris_engine.shapes import Coordinate, IShape
from tetris_engine.shapes import JShape
from tetris_engine.shapes import LShape
from tetris_engine.shapes import QShape
from tetris_engine.shapes import SShape
from tetris_engine.shapes import TShape
from tetris_engine.shapes import ZShape


def test_qshape_get_coordinate():
    """
    Test QShape get_coordinate
    """
    qshape = QShape(0)
    assert qshape.get_coordinates(Coordinate(1, 0)) == [
        Coordinate(1, 0),
        Coordinate(1, 1),
        Coordinate(0, 0),
        Coordinate(0, 1),
    ]


def test_zshape_get_coordinate():
    """
    Test ZShape get_coordinate
    """
    zshape = ZShape(0)
    assert zshape.get_coordinates(Coordinate(1, 0)) == [
        Coordinate(1, 0),
        Coordinate(1, 1),
        Coordinate(0, 1),
        Coordinate(0, 2),
    ]


def test_sshape_get_coordinate():
    """
    Test SShape get_coordinate
    """
    sshape = SShape(0)
    assert sshape.get_coordinates(Coordinate(1, 0)) == [
        Coordinate(1, 1),
        Coordinate(1, 2),
        Coordinate(0, 0),
        Coordinate(0, 1),
    ]


def test_tshape_get_coordinate():
    """
    Test TShape get_coordinate
    """
    tshape = TShape(0)
    assert tshape.get_coordinates(Coordinate(1, 0)) == [
        Coordinate(1, 0),
        Coordinate(1, 1),
        Coordinate(1, 2),
        Coordinate(0, 1),
    ]


def test_ishape_get_coordinate():
    """
    Test IShape get_coordinate
    """
    ishape = IShape(0)
    assert ishape.get_coordinates(Coordinate(1, 0)) == [
        Coordinate(1, 0),
        Coordinate(1, 1),
        Coordinate(1, 2),
        Coordinate(1, 3),
    ]


def test_lshape_get_coordinate():
    """
    Test LShape get_coordinate
    """
    lshape = LShape(0)
    assert lshape.get_coordinates(Coordinate(1, 0)) == [
        Coordinate(1, 0),
        Coordinate(0, 0),
        Coordinate(-1, 0),
        Coordinate(-1, 1),
    ]


def test_jshape_get_coordinate():
    """
    Test JShape get_coordinate
    """
    jshape = JShape(0)
    assert jshape.get_coordinates(Coordinate(1, 0)) == [
        Coordinate(1, 1),
        Coordinate(0, 1),
        Coordinate(-1, 0),
        Coordinate(-1, 1),
    ]


def test_coordinate():
    """
    Test Coordinate for row, col
    """
    row = 1
    col = 0
    coord = Coordinate(row, col)
    assert coord.row == row
    assert coord.col == col
