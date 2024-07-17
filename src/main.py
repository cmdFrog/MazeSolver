from gui import Window

def main():
    window = Window(1000, 800, "gray37", "Test Window")
    window.wait_for_close()

if __name__ == "__main__":
    main()
