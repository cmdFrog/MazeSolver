from gui import Window
from cell import Cell

def main():
    window = Window(800, 600, "gray37", "Test Window")

    cell = Cell(window)
    cell.has_right_wall = False
    cell.draw(50, 50, 100, 100)

    cell2 = Cell(window)
    cell2.has_left_wall = False
    cell2.has_bottom_wall = False
    cell2.draw(100, 50, 150, 100)

    cell3 = Cell(window)
    cell3.has_top_wall = False
    cell3.draw(100, 100, 150, 150)

    cell.draw_move(cell3)
    cell2.draw_move(cell3, undo=True)
    cell.draw_move(cell2)

    window.wait_for_close()

if __name__ == "__main__":
    main()
