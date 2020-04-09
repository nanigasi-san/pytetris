import numpy as np


class Field:
    def __init__(self):
        self.field = np.zeros((20, 10))
    def update(self):
        self.field = np.array(([line if sum(line) < 10 else [0] * 10 for line in self.field]))

print(Field().field)
