"""gem-tools simple gui"""

try:
    from tkinter import Tk, Label, Button
except ImportError:
    import Tkinter as tkinter
    from Tkinter import Tk, Label, Button

class GemGUI:
    def __init__(self, master, filepath, image, classified_contours, contour_types, **kwargs):
        
        self.master = master
        master.title("gem-tools")
        self.filepath = filepath

        # here, put a button for deleting numbers
        self.remove_box = Text(root, undo=True, wrap=WORD)
        self.remove_box.pack()
        self.remove_box.insert(END, 'Numbers here')

        self.re_run = Button(master, text="Re-run", command=rerun)
        self.re_run.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

    def show_image(self, filepath):
        """show an image in tk app"""
        from PIL import Image, ImageTk
        self.image = Image.open(self.filepath)
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = Label(image=self.photo)
        label.image = photo # keep a reference!
        label.pack()

    def delete_numbers(nums):
        from gem_tools.generator import redraw
        updated_contours, updated_contour_types = redraw(image, classified_contours, contour_types, nums)
        hires_contours = project(image, original, updated_contours)

    def rerun(self):
        false_positives = self.remove_box.get(1.0, END)
        false_positives = ''.join([i for i in false_positives if i.isnum() or i.isspace()])
        fps = [int(i) for i in false_positives.split()]
        delete_numbers(fps)
        show_image()


    # show the image using pil, and have some interface for removing by number...

root = Tk()
the_gui = GemGUI(root, filepath, image, classified_contours, contour_types)
root.mainloop()

# this means a person can run "python -m gem_tools.gui"
if __name__ == "__main__":
    the_gui()
