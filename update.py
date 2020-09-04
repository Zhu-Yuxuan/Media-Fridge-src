from tkinter import *


class GUI():

    def __init__(self, root):
        self.initGUI(root)

    def loop(self):
        print("loop proc running")
        self.root.after(1000, self.loop)

    def initGUI(self, root):
        self.root = root
        self.root.title("test")
        self.root.geometry("400x200+80+600")
        self.root.resizable = False
        self.root.after(1000, self.loop)

        self.root.mainloop()


if __name__ == "__main__":
    root = Tk()
    myGUI = GUI(root)