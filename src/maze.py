import time
#import pprint
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        self._cells = [[Cell(self.win) for _ in range(self.num_rows)] for _ in range(self.num_cols)]
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cells(i, j)

    def _draw_cells(self, i, j):
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if not self.win:
            return
        self.win.redraw()
        time.sleep(0.03)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cells(0, 0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cells(self.num_cols - 1, self.num_rows - 1)



if __name__ == "__main__":
    num_cols1 = 2
    num_rows1 = 3
    m1 = Maze(0, 0, num_rows1, num_cols1, 10, 10)
    #pprint.pp(m1._cells)
