"""gem-tools simple gui"""

# python 2/3 safe imports?
try:
    import tkinter
    from tkinter import *
    from tkinter import Tk, Label, Button, Text
except ImportError:
    import Tkinter
    from Tkinter import *
    import Tkinter as tkinter
    from Tkinter import Tk, Label, Button, Text


class GemGUI:
    def __init__(self, root, filepath, image, classified_contours, contour_types, **kwargs):
        
        self.root = root
        root.title("gem-tools")
        self.filepath = filepath
        # we might need to somehow return these two things:
        self.updated_contours = None
        self.hires_contours = None

        def delete_numbers(self, nums, init=False):
            from gem_tools.generator import redraw, project
            if init:
                redraw(image, classified_contours, contour_types, nums)
            else:
                updated_contours, updated_contour_types = redraw(image, classified_contours, contour_types, nums)
                hires_contours = project(image, original, updated_contours)
                self.updated_contours = updated_contours
                self.hires_contours = hires_contours

        def show_image(filepath):
            """show an image in tk app"""
            import PIL
            from PIL import Image, ImageTk
            self.image = Image.open(self.filepath)
            basewidth = 300
            wpercent = (basewidth/float(self.image.size[0]))
            hsize = int((float(self.image.size[1])*float(wpercent)))
            self.image = self.image.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(self.image)
            self.label = Label(image=self.photo)
            self.label.image = self.photo # keep a reference!
            self.label.pack()

        def rerun(init=False):
            false_positives = self.remove_box.get(1.0, 'end')
            false_positives = ''.join([i for i in false_positives if i.isdigit() or i.isspace()])
            fps = [int(i) for i in false_positives.split()]
            delete_numbers(self, fps, init=init)
            show_image(self.filepath)
            
        # here, put a button for deleting numbers
        self.remove_box = Text(root, undo=True, height=5, width=40)
        self.remove_box.pack()
        self.remove_box.insert('end', 'Numbers here')

        rerun(init=True)
        self.re_run = Button(root, text="Run", command=rerun)
        self.re_run.pack()

        self.close_button = Button(root, text="Close", command=root.quit)
        self.close_button.pack()

def the_gui(filepath, image, classified_contours, contour_types):
    root = Tk()
    the_gui = GemGUI(root, filepath, image, classified_contours, contour_types)
    root.mainloop()

# this means a person can run "python -m gem_tools.gui"
if __name__ == "__main__":
    the_gui()
