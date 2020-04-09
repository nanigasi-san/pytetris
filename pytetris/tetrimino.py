import numpy as np
class Tetrimino:
    def __init__(self, cell):
        if (cell < 0).all() or (cell > 1).all():
            raise ValueError
        elif cell.shape != (4, 4):
            raise ValueError
        self.cell = cell

    def rot90(self):
        self.cell = np.rot90(self.cell)