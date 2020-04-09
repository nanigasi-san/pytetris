from pytetris.field import Field
import numpy as np


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
