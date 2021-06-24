from sys import exit
import tkinter as gui
from tkinter import filedialog, Text
import os


root = gui.Tk()

def rysuj():
    os.system("%user%")
    otworz: int= os.system("python rysunek.py")

def odpalJarvisa():
    os.system("cls")
    otworz1: int=os.system("python jarvis.py")

def zamknij():
    exit(0)

canvas = gui.Canvas(root, height=700, width=600, bg="white")
canvas.pack()

frame = gui.Frame(root, bg="blue")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = gui.Button(root, text="narysuj", padx=10, pady=5, fg="white", bg="black", command=rysuj)
openFile.pack()


jarvis = gui.Button(root, text="odpal jarvisa 1.0", padx=10, pady=5, fg="white", bg="black", command=odpalJarvisa)
jarvis.pack()


closeProgram = gui.Button(root, text="zamknij", padx=10, pady=5, fg="white", bg="black", command=zamknij)
closeProgram.pack()



root.mainloop()