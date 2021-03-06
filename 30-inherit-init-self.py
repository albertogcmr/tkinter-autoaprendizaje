from tkinter import *

class TipicalFrame(Frame):
    def __init__(self, the_window, **kwargs):
        super().__init__(**kwargs)
        self['height']=150
        self['width']=150
        self['bd']=8
        print('id of self is {}'.format(id(self)))


# main window
my_window = Tk()

# build the GUI
frame_a = TipicalFrame(my_window, relief=RAISED, bg='red')
print('id of frame_a is {}'.format(id(frame_a)))

frame_b = TipicalFrame(my_window, relief=SUNKEN, bg='green')
print('id of frame_b is {}'.format(id(frame_b)))


frame_a.grid(row=0, column=0)
frame_b.grid(row=0, column=1)

my_window.mainloop()
