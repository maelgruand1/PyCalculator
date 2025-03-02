import tkinter as tk

def tkWin(title, size):
    win = tk.Tk()
    win.geometry(size)
    win.title(title)
    return win

