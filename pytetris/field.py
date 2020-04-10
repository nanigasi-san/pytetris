import numpy as np


class Field:
    def __init__(self):
        self.field = np.zeros((20, 10))

    def update(self):
        self.field = np.array(([line if sum(line) < 10 else [0] * 10 for line in self.field]))

    def add(self, start, tetrimino):
        l, c = tetrimino.cell.shape
        x, y = start
        for i in range(l):
            for j in range(c):
                self.field[x+i][y+j] = 1
                print(x+i, y+j)
