from gui import Window

def main():
    window = Window(850, 850, "gray37", "Test Window")
    window.wait_for_close()

if __name__ == "__main__":
    main()
