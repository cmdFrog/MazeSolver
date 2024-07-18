import os
from gui import Window

def main():
    path = find_path(["src/cmdFrog.ico", "cmdFrog.ico"])
    window = Window(850, 850, "gray37", "Maze Solver", path = path)
    window.wait_for_close()

def find_path(paths):
    for path in paths:
        if os.path.isfile(path):
            return path
    return None


if __name__ == "__main__":
    main()
