from gui import Window

def main():
    window = Window(800, 600, "gray37", "Test Window")
    window.wait_for_close()

if __name__ == "__main__":
    main()
