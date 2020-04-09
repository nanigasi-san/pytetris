import numpy as np
import pytest
from pytetris.tetrimino import Tetrimino


def test_tetrimino_init_1():
    cell = np.ones((4, 4))
    tetrimino = Tetrimino(cell)
    assert (tetrimino.cell == cell).all()


def test_tetrimino_init_2():
    cell = np.zeros((4, 4))
    tetrimino = Tetrimino(cell)
    assert (tetrimino.cell == cell).all()


def test_tetrimino_init_3():
    cell = np.array([[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]])
    tetrimino = Tetrimino(cell)
    assert (tetrimino.cell == cell).all()


def test_tetrimino_init_4():
    cell = np.full((4, 4), 5)
    with pytest.raises(ValueError):
        Tetrimino(cell)


def test_tetrimino_init_5():
    cell = np.random.randint(2, 10, (4, 4))
    with pytest.raises(ValueError):
        Tetrimino(cell)
