from gui import Window, Point, Line

def main():
    window = Window(800, 600, "gray37", "Test Window")
    line = Line(Point(390, 300), Point(410, 300))
    line2 = Line(Point(400, 290), Point(400, 310))
    window.draw_line(line, "white")
    window.draw_line(line2, "white")
    window.wait_for_close()

if __name__ == "__main__":
    main()
