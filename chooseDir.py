# https://www.youtube.com/watch?v=H71ts4XxWYU
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


dir = filedialog.askdirectory()
print(dir)