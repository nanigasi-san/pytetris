import numpy as np
import pytest
from pytetris.tetrimino import Tetrimino


def test_tetrimino_init_1():
    cell = np.ones((4, 4))
    tetrimino = Tetrimino(cell)
    assert (tetrimino.cell == cell).all()


def test_tetrimino_init_2():
    cell = np.array([[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]])
    tetrimino = Tetrimino(cell)
    assert (tetrimino.cell == cell).all()


def test_tetrimino_init_3():
    cell = np.zeros((4, 4))
    with pytest.raises(ValueError):
        Tetrimino(cell)


def test_tetrimino_init_4():
    cell = np.full((4, 4), 5)
    with pytest.raises(ValueError):
        Tetrimino(cell)


def test_tetrimino_init_5():
    cell = np.random.randint(2, 10, (4, 4))
    with pytest.raises(ValueError):
        Tetrimino(cell)


@pytest.fixture
def rot_base_cell():
    return np.array([[0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1]])


def test_tetrimino_rot_1(rot_base_cell):
    tetrimino = Tetrimino(rot_base_cell)
    valid_cell = np.rot90(rot_base_cell, 1)
    tetrimino.rot90()
    assert (tetrimino.cell == valid_cell).all()


def test_tetrimino_rot_2(rot_base_cell):
    tetrimino = Tetrimino(rot_base_cell)
    valid_cell = np.rot90(rot_base_cell, 2)
    tetrimino.rot90()
    tetrimino.rot90()
    assert (tetrimino.cell == valid_cell).all()


def test_tetrimino_rot_3(rot_base_cell):
    tetrimino = Tetrimino(rot_base_cell)
    valid_cell = np.rot90(rot_base_cell, 3)
    tetrimino.rot90()
    tetrimino.rot90()
    tetrimino.rot90()
    assert (tetrimino.cell == valid_cell).all()


def test_tetrimino_rot_4(rot_base_cell):
    tetrimino = Tetrimino(rot_base_cell)
    valid_cell = np.rot90(rot_base_cell, 4)
    tetrimino.rot90()
    tetrimino.rot90()
    tetrimino.rot90()
    tetrimino.rot90()
    assert (tetrimino.cell == valid_cell).all()