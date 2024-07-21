from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from config import *

def gui():

    root = tb.Window(themename="superhero")
    root.title(APP_TITLE)
    root.geometry(f"{WINDOWS_GEOMETRY_HEIGHT}x{WINDOWS_GEOMETRY_WIDTH}")

    my_label = tb.Label(text="Hello world", font=("Helvetica", 28), bootstyle="default")
    my_label.pack(pady=50)


    root.mainloop()
