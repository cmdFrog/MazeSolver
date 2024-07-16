import time
import random
#import pprint
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed:
            random.seed(seed)
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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

    def _break_walls_r(self, i ,j):
        self._cells[i][j].visited = True

        while True:
            directions = []

            # check directions

            if j > 0 and not self._cells[i][j - 1].visited: # up
                directions.append((i, j - 1, "up"))

            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited: # down
                directions.append((i, j + 1, "down"))

            if i > 0 and not self._cells[i - 1][j].visited: # left
                directions.append((i - 1, j, "left"))

            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited: # right
                directions.append((i + 1, j, "right"))

            # break if no directions
            if len(directions) == 0:
                self._draw_cells(i, j)
                return

            ni, nj, direction = directions[random.randrange(len(directions))]

            # break walls between current and chosen cell
            if direction == "up":
                self._cells[i][j].has_top_wall = False
                self._cells[ni][nj].has_bottom_wall = False
            if direction == "down":
                self._cells[i][j].has_bottom_wall = False
                self._cells[ni][nj].has_top_wall = False
            if direction == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[ni][nj].has_right_wall = False
            if direction == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[ni][nj].has_left_wall = False

            #recursively call on chosen cell
            self._break_walls_r(ni, nj)

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[self.num_cols - 1][self.num_rows - 1]:
            return True
        if j > 0 and not self._cells[i][j - 1].visited: # up
            if not self._cells[i][j].has_top_wall and not self._cells[i][j - 1].has_bottom_wall:
                self._cells[i][j].draw_move(self._cells[i][j - 1])
                if self._solve_r(i, j - 1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        if j < self.num_rows - 1 and not self._cells[i][j + 1].visited: # down
            if not self._cells[i][j].has_bottom_wall and not self._cells[i][j + 1].has_top_wall:
                self._cells[i][j].draw_move(self._cells[i][j + 1])
                if self._solve_r(i, j + 1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        if i > 0 and not self._cells[i - 1][j].visited: # left
            if not self._cells[i][j].has_left_wall and not self._cells[i - 1][j].has_right_wall:
                self._cells[i][j].draw_move(self._cells[i - 1][j])
                if self._solve_r(i - 1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        if i < self.num_cols - 1 and not self._cells[i + 1][j].visited: # right
            if not self._cells[i][j].has_right_wall and not self._cells[i + 1][j].has_left_wall:
                self._cells[i][j].draw_move(self._cells[i + 1][j])
                if self._solve_r(i + 1, j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        return False



if __name__ == "__main__":
    num_cols1 = 2
    num_rows1 = 3
    m1 = Maze(0, 0, num_rows1, num_cols1, 10, 10)
    #pprint.pp(m1._cells)
