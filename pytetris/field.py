import numpy as np

class Field:
    def __init__(self):
        self.field = np.zeros((20, 10))

    def update(self):
        self.field = np.array(([line if sum(line) < 10 else [0] * 10 for line in self.field]))

    def add(self, start, tetrimino):
        if not self.is_deployable(start, tetrimino):
            raise TetriminoExistError
        l, c = tetrimino.cell.shape
        x, y = start
        for i in range(l):
            for j in range(c):
                self.field[x+i][y+j] += tetrimino.cell[i][j]

    def is_deployable(self, start, tetrimino):
        l, c = tetrimino.cell.shape
        x, y = start
        for i in range(l):
            for j in range(c):
                if self.field[x+i][y+j] + tetrimino.cell[i][j] > 1:
                    return False
        return True


class TetriminoExistError(Exception):
    pass
