from gui import Point, Line

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if not self._win:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        elif not self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, self._win.bg_color)
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        elif not self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, self._win.bg_color)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        elif not self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, self._win.bg_color)
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        elif not self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, self._win.bg_color)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        elif not self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, self._win.bg_color)

    def center_point(self):
        return Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)

    def draw_move(self, to_cell, undo=False):
        if not self._win:
            return
        self_center = self.center_point()
        to_center = to_cell.center_point()
        if not undo:
            line = Line(self_center, to_center)
            self._win.draw_line(line, "gray")
        if undo:
            line = Line(self_center, to_center)
            self._win.draw_line(line, "red")

    if __name__ == "__main__":
        pass
