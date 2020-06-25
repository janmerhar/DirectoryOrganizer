# https://www.youtube.com/watch?v=H71ts4XxWYU
import tkinter as tk
from tkinter import filedialog
import os

def izberiDir():
    root = tk.Tk()
    root.withdraw()

    dir = filedialog.askdirectory()
    return dir 

def narediDir(startDir):
    end = input("Vnesi ime mape: ")
    endDir = startDir + '/' + end 
    os.mkdir(endDir)

dir = izberiDir()
narediDir(dir)

#naredi kreiranje posameznih map in določanja .pripon