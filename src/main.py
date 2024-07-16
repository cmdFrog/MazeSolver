from gui import Window
from maze import Maze

def main():
    window = Window(800, 600, "gray37", "Test Window")

    m1 = Maze(50, 50, 10, 14, 50, 50, window)
    m1.solve()

    window.wait_for_close()

if __name__ == "__main__":
    main()
