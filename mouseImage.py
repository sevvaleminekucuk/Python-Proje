import tkinter as tk
from PIL import Image, ImageTk

class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """
    def __init__(self, widget, image_path):
        self.waittime = 500     #miliseconds
        self.wraplength = 180   #pixels
        self.widget = widget
        self.image_path = image_path
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + self.widget.winfo_width() + 3
        y += self.widget.winfo_rooty() + self.widget.winfo_height() + 3
        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))

        # background image
        img = Image.open(self.image_path)
        img = img.resize((100, 100), Image.ANTIALIAS)

        bg_image = ImageTk.PhotoImage(img)
        label = tk.Label(self.tw, image = bg_image)
        label.image = bg_image
        label.pack(side = "bottom", fill = "both")


    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()

# testing ...
# if __name__ == '__main__':
#     root = tk.Tk()
#     root.mainloop()