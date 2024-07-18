from tkinter import Tk, BOTH, Canvas, Entry, Button, Label, StringVar, BooleanVar, Checkbutton, Frame
from maze import Maze

class Window:
    def __init__(self, width: int, height: int, bg_color: str, title: str):
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title(title)
        self.canvas = Canvas(self.__root, bg=bg_color, width=width, height=height, bd=0, highlightbackground="gray48", highlightthickness=5)
        self.canvas.pack(fill=BOTH, expand=1)
        self.var = StringVar()
        self.seed_var = StringVar()
        self.submitted_seed = None
        self.set_seed_var = BooleanVar()
        self.close_flag = False
        self.bg_color = bg_color
        self._input()
        self.maze = None
        self.submitted_number = None
        self.running = False

    def _input(self):
        # Frame
        self.main_frame = Frame(self.__root, bg=self.bg_color, pady=5, padx=5, highlightthickness=0)
        self.main_frame.pack(fill=BOTH, expand=1)
        # Size input label
        self.entry_label = Label(self.main_frame, bg=self.bg_color, text="Enter maze size:", fg="white", font='Helvetica 10 bold', highlightthickness=0)
        self.entry_label.grid(row=0, column=0, sticky="w")
        # Size input entry
        self.entry = Entry(self.main_frame, textvariable=self.var, validate="key", validatecommand=(self.__root.register(self.validate), '%P'), highlightthickness=0)
        self.entry.grid(row=0, column=1, padx=5)
        # Size input button
        self.submit_button = Button(self.main_frame, text="Submit", command=self.submit, highlightthickness=0)
        self.submit_button.grid(row=0, column=2, padx=5)
        # Maze build button
        self.maze_button = Button(self.main_frame, text="Create Maze", command=self.create_maze, highlightthickness=0)
        self.maze_button.grid(row=0, column=3, padx=5, pady=5)
        # Maze solve button
        self.solve_button = Button(self.main_frame, text="Solve", command=self.solve_maze, state="disabled", highlightthickness=0)
        self.solve_button.grid(row=1, column=3, padx=5, pady=5)
        # Set seed checkbox
        self.set_seed_checkbutton = Checkbutton(self.main_frame, text="Set fixed seed", variable=self.set_seed_var, command=self.toggle_seed_entry, bg=self.bg_color, fg="white", font='Helvetica 10 bold', highlightthickness=0, selectcolor="black")
        self.set_seed_checkbutton.grid(row=0, column=4, padx=5, sticky="e")
        # Seed submit button
        self.seed_submit_button = Button(self.main_frame, text="Submit Seed", command=self.submit_seed, state='disabled', highlightthickness=0)
        self.seed_submit_button.grid(row=0, column=6, padx=5, sticky="e")
        # Seed input entry
        self.seed_entry = Entry(self.main_frame, textvariable=self.seed_var, validate="key", validatecommand=(self.__root.register(self.validate), '%P'), state="disabled", highlightthickness=0)
        self.seed_entry.grid(row=0, column=5, padx=5, sticky="e")
        # General result label for all user actions
        self.result_label = Label(self.main_frame, text="", bg=self.bg_color, highlightthickness=0, font='Helvetica 10 bold')
        self.result_label.grid(row=1, column=0, columnspan=3, sticky="w")
        # Key bindings for entry fields (enter and num pad enter)
        self.entry.bind('<Return>', self.submit)
        self.seed_entry.bind('<Return>', self.submit_seed)
        self.entry.bind('<KP_Enter>', self.submit)
        self.seed_entry.bind('<KP_Enter>', self.submit_seed)

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
        if input_text == "" or int(input_text) > 15:
            self.result_label.config(text="No or invalid input. Max size is 15.", fg="red")
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
        self.close_flag = True

    def draw_line(self, line, fill_color="white"):
        line.draw(self.canvas, fill_color)

if __name__ == "__main__":
    window = Window(800, 600, "gray37", "Test Window")
    window.wait_for_close()
