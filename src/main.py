from gui import Window
from maze import Maze

def main():
    window = Window(800, 600, "gray37", "Test Window")

    Maze(50, 50, 10, 10, 50, 50, window)

    window.wait_for_close()

if __name__ == "__main__":
    main()
