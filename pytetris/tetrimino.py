class Tetrimino:
    def __init__(self, cell):
        if (cell >= 0).all() and (cell <= 1).all():
            self.cell = cell
        else:
            raise ValueError
