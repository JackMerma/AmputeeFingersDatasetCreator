import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from config import *
from src.gui.options import *


def gui():

    root = tb.Window(themename=MAIN_THEME)
    root.title(APP_TITLE)
    root.geometry(f"{WINDOWS_GEOMETRY_HEIGHT}x{WINDOWS_GEOMETRY_WIDTH}")

    w = WINDOWS_GEOMETRY_WIDTH
    h = WINDOWS_GEOMETRY_HEIGHT

    create_options(root, w, h)

    """
    frame1 = tb.Labelframe(root, text="Frame 1", width=w, height=100)
    frame1.pack(side="left", fill="x")

    frame2 = tb.Labelframe(root, text="Frame 2", width=w, height=200)
    frame2.pack(side="left", fill="x")

    """

    root.mainloop()
