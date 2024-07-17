from tkinter import Tk, BOTH, Canvas, Entry, Button, Label, StringVar
from maze import Maze

class Window:
    def __init__(self, width: int, height: int, bg_color: str, title: str):
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title(title)
        self.canvas = Canvas(self.__root, bg=bg_color, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.var = StringVar()
        self._input()
        self.maze = None
        self.submitted_number = None
        self.bg_color = bg_color
        self.running = False

    def _input(self):
        self.result_label = Label(self.__root, text="")
        self.result_label.pack(anchor="w")
        self.label = Label(self.__root, text="Enter maze size:")
        self.label.pack(side="left")
        self.entry = Entry(self.__root, textvariable=self.var, validate="key", validatecommand=(self.__root.register(self.validate), '%P'))
        self.entry.pack(pady=10, side='left')
        self.submit_button = Button(self.__root, text="Submit", command=self.submit)
        self.submit_button.pack(side='left')
        self.entry.bind('<Return>', self.submit)
        self.maze_button = Button(self.__root, text="Create Maze", command=self.create_maze)
        self.maze_button.pack(anchor="n")
        self.solve_button = Button(self.__root, text="Solve", command=self.solve_maze)
        self.solve_button.pack(anchor="n")

    def validate(self, new_value):
        if new_value.isdigit() or new_value == "":
            return True
        return False

    def submit(self, _event=None):
        input_text = self.var.get()
        if input_text == "":
            print("No input")
            self.result_label.config(text="No input")
        else:
            print("Entered number:", input_text)
            self.result_label.config(text=f"Entered number: {input_text}")
            self.submitted_number = int(input_text)

    def create_maze(self):
        if self.submitted_number is None:
            print("Please submit a number first")
            self.result_label.config(text="Please submit a number first")
        else:
            self.canvas.delete("all")
            self.result_label.config(text=f"Creating maze with size of: {self.submitted_number}")
            self.maze = Maze(50, 50, self.submitted_number, self.submitted_number, 50, 50, self)

    def solve_maze(self):
        self.maze.solve()

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

if __name__ == "__main__":
    window = Window(800, 600, "gray37", "Test Window")
    window.wait_for_close()
