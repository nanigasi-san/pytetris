import numpy as np
from pytetris.tetrimino import Tetrimino


def test_tetrimino_cell_1():
    cell = np.ones((4, 4))
    tetrimino = Tetrimino(cell)
    assert (tetrimino.cell == cell).all()


def test_tetrimino_cell_2():
    cell = np.zeros((4, 4))
    tetrimino = Tetrimino(cell)
    assert (tetrimino.cell == cell).all()


def test_tetrimino_cell_3():
    cell = np.full((4, 4), 5)
    tetrimino = Tetrimino(cell)
    assert (tetrimino.cell == cell).all()


def test_tetrimino_cell_4():
    cell = np.random.randint(0, 10, (4, 4))
    tetrimino = Tetrimino(cell)
    assert (tetrimino.cell == cell).all()
