class Tetrimino:
    def __init__(self, cell):
        if (cell < 0).all() or (cell > 1).all():
            raise ValueError
        elif cell.shape != (4, 4):
            raise ValueError
        self.cell = cell
