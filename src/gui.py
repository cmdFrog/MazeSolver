from tkinter import Tk, BOTH, Canvas, Entry, Button, Label, StringVar, BooleanVar, Checkbutton, Frame
from maze import Maze

class Window:
    def __init__(self, width: int, height: int, bg_color: str, title: str):
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title(title)
        self.canvas = Canvas(self.__root, bg=bg_color, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.var = StringVar()
        self.seed_var = StringVar()
        self.submitted_seed = None
        self.set_seed_var = BooleanVar()
        self._input()
        self.maze = None
        self.submitted_number = None
        self.bg_color = bg_color
        self.running = False

    def _input(self):
        self.main_frame = Frame(self.__root)
        self.main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        self.entry_label = Label(self.main_frame, text="Enter maze size:")
        self.entry_label.grid(row=0, column=0, sticky="w")

        self.entry = Entry(self.main_frame, textvariable=self.var, validate="key", validatecommand=(self.__root.register(self.validate), '%P'))
        self.entry.grid(row=0, column=1, padx=5)

        self.submit_button = Button(self.main_frame, text="Submit", command=self.submit)
        self.submit_button.grid(row=0, column=2, padx=5)

        self.maze_button = Button(self.main_frame, text="Create Maze", command=self.create_maze)
        self.maze_button.grid(row=0, column=3, padx=5)

        self.solve_button = Button(self.main_frame, text="Solve", command=self.solve_maze, state="disabled")
        self.solve_button.grid(row=1, column=3, padx=5)

        self.set_seed_checkbutton = Checkbutton(self.main_frame, text="Set fixed seed", variable=self.set_seed_var, command=self.toggle_seed_entry)
        self.set_seed_checkbutton.grid(row=0, column=4, padx=5, sticky="e")
        self.seed_submit_button = Button(self.main_frame, text="Submit Seed", command=self.submit_seed, state='disabled')
        self.seed_submit_button.grid(row=0, column=6, padx=5, sticky="e")

        self.seed_entry = Entry(self.main_frame, textvariable=self.seed_var, validate="key", validatecommand=(self.__root.register(self.validate), '%P'), state="disabled")
        self.seed_entry.grid(row=0, column=5, padx=5, sticky="e")

        self.entry.bind('<Return>', self.submit)
        self.seed_submit_button.bind('<Return>', self.submit_seed)

        self.result_label = Label(self.main_frame, text="")
        self.result_label.grid(row=1, column=0, columnspan=3, sticky="w")

    def validate(self, new_value):
        if new_value.isdigit() or new_value == "":
            return True
        return False

    def toggle_seed_entry(self):
        if self.set_seed_var.get():
            self.seed_entry.config(state="normal")
            self.seed_submit_button.config(state="normal")
        else:
            self.seed_entry.config(state="disabled")
            self.seed_submit_button.config(state="disabled")
            self.submitted_seed = None


    def submit_seed(self, _event=None):
        input_text = self.seed_var.get()
        if input_text == "":
            self.result_label.config(text="No or invalid input.", fg="red")
        else:
            self.result_label.config(text=f"Entered number: {input_text}", fg="green")
            self.submitted_seed = int(input_text)

    def submit(self, _event=None):
        input_text = self.var.get()
        if input_text == "" or int(input_text) > 100:
            self.result_label.config(text="No or invalid input. Max size is 100.", fg="red")
        else:
            self.result_label.config(text=f"Entered number: {input_text}", fg="green")
            self.submitted_number = int(input_text)

    def create_maze(self):
        if self.submitted_number is None:
            self.result_label.config(text="Please submit a number first", fg="red")
        else:
            self.maze_button.config(state="disabled")
            self.solve_button.config(state="disabled")
            self.canvas.delete("all")
            self.result_label.config(text=f"Creating maze with size of: {self.submitted_number}", fg="green")
            self.maze = Maze(50, 50, self.submitted_number, self.submitted_number, 50, 50, self, seed=self.submitted_seed)
            while not self.maze.anim_finished:
                self.__root.update_idletasks()
                self.__root.update()
            self.solve_button.config(state="normal")
            self.maze_button.config(state="normal")

    def solve_maze(self):
        self.maze_button.config(state="disabled")
        self.solve_button.config(state="disabled")
        self.maze.solve()
        while not self.maze.solve_finished:
            self.__root.update_idletasks()
            self.__root.update()
        self.solve_button.config(state="normal")
        self.maze_button.config(state="normal")

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
