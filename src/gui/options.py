import tkinter as tk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from config import *


def create_options(host, w, h):

    options = tb.Frame(host, bootstyle="primary", width=w, height=h)
    options.pack(side="left", fill="both")
    create_drag_and_drop(options, w, h)



def create_drag_and_drop(host, w, h):

    dad = tb.Labelframe(host, text="Files", width=w, height=h)
    dad.pack(fill="y")

    inside_frame = tb.Frame(dad)

    label = tb.Label(inside_frame, text="Hola mundo como \n estas\nads\nasd", font=("Helvetica", 18))
    label.pack()

    scroll = tb.Scrollbar(dad, orient="vertical", bootstyle="danger round")
    scroll.pack(side="right")

    scroll.config(command=inside_frame.yview)

