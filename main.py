from mainFrame import MainFrame
import tkinter as tk


def main():
    """ Initializes MainFrame Login Interface """
    root = tk.Tk()
    root.title("Inventory Management System")
    root.resizable(False, False)
    app = MainFrame(root)
    root.mainloop()

if __name__ == "__main__":
    main()

