from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width: int, height: int, bg_color: str, title: str):
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title(title)
        self.canvas = Canvas(self.__root, bg=bg_color, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color="white"):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2

    def draw(self, canvas, fill_color: str):
        canvas.create_line(
            self.point_1.x, self.point_1.y, self.point_2.x, self.point_2.y, fill=fill_color, width=2
        )

if __name__ == "__main__":
    window = Window(800, 600, "gray37", "Test Window")
    window.wait_for_close()
