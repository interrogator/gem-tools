"""gem-tools simple gui"""

from tkinter import Tk, Label, Button

class GemGUI:
    def __init__(self, master, **kwargs):
        self.master = master
        master.title("gem-tools")

        self.filename = kwargs.pop('filename')

        self.label = Label(master, text="Simple gem-interface!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Testing!")

    # show the image using pil, and have some interface for removing by number...

root = Tk()
the_gui = GemGUI(root, **kwargs)
root.mainloop()


# this means a person can run "python -m gem_tools.gui"
if __name__ == "__main__":
    the_gui()
