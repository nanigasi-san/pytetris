from pytetris.field import Field
from pytetris.tetrimino import Tetrimino
import numpy as np
import pytest

def test_field_init_1():
    vaild_field = np.zeros((20, 10))
    field = Field()
    assert (field.field == vaild_field).all()


def test_field_del_line_1():
    vaild_field = np.zeros((20, 10))
    field = Field()
    field.field[-1] += 1
    field.update()
    assert (field.field == vaild_field).all()


def test_field_del_line_2():
    vaild_field = np.zeros((20, 10))
    field = Field()
    field.field[0] += 1
    field.field[-1] += 1

    field.update()
    assert (field.field == vaild_field).all()


@pytest.fixture
def O():
    cell = np.ones((2, 2))
    return Tetrimino(cell)


def test_add_tetrimino_1(O):
    valid_field = np.array([[0.0 for j in range(10)] for i in range(20)])
    valid_field[-1][0] = 1.0
    valid_field[-1][1] = 1.0
    valid_field[-2][0] = 1.0
    valid_field[-2][1] = 1.0
    field = Field()
    field.add((18, 0), O)
    assert (field.field == valid_field).all()


def test_add_update_tetrimino_1(O):
    valid_field = np.zeros((20, 10))
    field = Field()
    for i in range(5):
        field.add((18, 2*i), O)
    field.update()
    print(type(field.field), type(valid_field))
    assert (field.field == valid_field).all()