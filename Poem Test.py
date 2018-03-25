#Copyright ® 2018 Aymaan Shaikh
#Please Contact Before Using Code

import turtle
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_text(150, 100, text='There was a little man,')
canvas.create_text(130, 120, text='He was a goose.',
fill='red')
canvas.create_text(150, 150, text='He alwyas "road a moose,',
font=('Times', 15))
canvas.create_text(200, 200, text='He fell to the ground,',
font=('Helvetica', 20))
canvas.create_text(220, 250, text='And heard a tiny sound',
font=('Courier', 22))
canvas.create_text(220, 300, text='Plop, he fell to the water"', font=('Courier', 20))
