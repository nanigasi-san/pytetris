import numpy as np
class Tetrimino:
    def __init__(self, cell):
        if (cell < 0).all() or (cell > 1).all():
            raise ValueError
        else:
            line, column = cell.shape
            for i in range(line):
                if sum(cell[i]) == 0:
                    raise ValueError
            for i in range(column):
                if np.sum([cell[:][i]]) == 0:
                    raise ValueError
            self.cell = cell

    def rot90(self):
        self.cell = np.rot90(self.cell)