import random
import pyautogui as pg
import time
from utils import make_sentence, type_sentence
import tkinter as tk
# from essential_generators import DocumentGenerator

# gen = DocumentGenerator()

width, height= pg.size() #width and height of screen

# sentence = make_sentence()
# sentence = gen.sentence()
# time.sleep(2)

window = tk.Tk()
running = False

def execute_loop():
  time.sleep(2)
  global running
  if running:
    type_sentence(make_sentence())
    window.after(30, execute_loop)

def start_loop(event=None):
  print("\nStarting Loop Now\n")
  global running
  running = True
  window.after(0, execute_loop)

def stop_loop(event):
  print("\n\nStopping Loop Now\n")
  global running
  running = False

button = tk.Button(
    text="Start Writing",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

button.bind("<Button-1>", start_loop)
button.pack()

button = tk.Button(
    text="Stop Writing",
    width=25,
    height=5,
    bg="red",
    fg="yellow",
)

button.bind("<Button-1>", stop_loop)
button.pack()

window.geometry('+0+0')
window.mainloop()