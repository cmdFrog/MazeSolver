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







if __name__ == "__main__":
    window = Window(800, 600, "gray37", "Test Window")
    window.wait_for_close()
