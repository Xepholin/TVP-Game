from system import *
from playerCommands import *

from tkinter import *

# create window

game = Tk()

# Custom window

game.title("TVP Game")
game.geometry("1000x1200")
game.minsize(1000, 1200)

# Frame

main = Frame(game)
"""
frameTank1 = Frame(main, bg='black', bd=1)
frameTank1.grid(row=0, column=0)

frameTank2 = Frame(main, bg='black', bd=1)
frameTank2.grid(row=0, column=4)

frameTank3 = Frame(main, bg='black', bd=1)
frameTank3.grid(row=0, column=8)
"""

# Canvas

tank1Canvas = Canvas(main, bg="black", bd=1, width=140, height=140)
temp = tank1Canvas.create_rectangle(0, 0, 150, 150, fill="orange")
tank1Canvas.create_text(75, 60, text="Tank1", font=("Arial", 15), fill="black")
pump11 = Pump(tank1Canvas.create_oval(30, 90, 70, 130, fill="black"))
tank1Canvas.create_text(50, 110, text="p11", font=("Arial", 11), fill="white")
pump12 = Pump(tank1Canvas.create_oval(80, 90, 120, 130, fill="black"))
tank1Canvas.create_text(100, 110, text="p12", font=("Arial", 11), fill="white")
tank1Canvas.grid(row=0, column=0)

tank1 = Tank(temp, pump11, pump12, 100)

pipe1 = Canvas(main, width=70, height=70)
pipe1.create_line(0, 35, 70, 35)
pipe1.grid(row=0, column=1)

valve1 = Canvas(main, width=70, height=140)
valve1.create_oval(5, 37, 70, 102, fill="black")
valve1.create_line(37, 40, 37, 99, fill="white", width=5)
valve1.create_text(37, 20, text="VT12", font=("Arial", 15), fill="black")
valve1.grid(row=0, column=2)

pipe2 = Canvas(main, width=70, height=70)
pipe2.create_line(0, 35, 70, 35)
pipe2.grid(row=0, column=3)

tank2Canvas = Canvas(main, bg="black", bd=1, width=140, height=140)
temp = tank2Canvas.create_rectangle(0, 0, 150, 150, fill="green")
tank2Canvas.create_text(75, 60, text="Tank2", font=("Arial", 15), fill="black")
pump21 = Pump(tank2Canvas.create_oval(30, 90, 70, 130, fill="black"))
tank2Canvas.create_text(50, 110, text="p21", font=("Arial", 11), fill="white")
pump22 = Pump(tank2Canvas.create_oval(80, 90, 120, 130, fill="black"))
tank2Canvas.create_text(100, 110, text="p22", font=("Arial", 11), fill="white")
tank2Canvas.grid(row=0, column=4)

tank2 = Tank(temp, pump21, pump22, 50)

pipe3 = Canvas(main, width=70, height=70)
pipe3.create_line(0, 35, 70, 35)
pipe3.grid(row=0, column=5)

valve2 = Canvas(main, width=70, height=140)
valve2.create_oval(5, 37, 70, 102, fill="black")
valve2.create_line(37, 40, 37, 99, fill="white", width=5)
valve2.create_text(37, 20, text="VT23", font=("Arial", 15), fill="black")
valve2.grid(row=0, column=6)

pipe4 = Canvas(main, width=70, height=70)
pipe4.create_line(0, 35, 70, 35)
pipe4.grid(row=0, column=7)

tank3Canvas = Canvas(main, bg="black", bd=1, width=140, height=140)
temp = tank3Canvas.create_rectangle(0, 0, 150, 150, fill="yellow")
tank3Canvas.create_text(75, 60, text="Tank3", font=("Arial", 15), fill="black")
pump31 = Pump(tank3Canvas.create_oval(30, 90, 70, 130, fill="black"))
tank3Canvas.create_text(50, 110, text="p31", font=("Arial", 11), fill="white")
pump32 = Pump(tank3Canvas.create_oval(80, 90, 120, 130, fill="black"))
tank3Canvas.create_text(100, 110, text="p32", font=("Arial", 11), fill="white")
tank3Canvas.grid(row=0, column=8)

tank3 = Tank(temp, pump31, pump32, 100)


# Text
"""
tank1Text = Label(tank1, text="Tank1", font=("Arial", 20), bg="orange", fg="black")
tank1Text.pack()

tank2Text = Label(tank2Canvas, text="Tank2", font=("Arial", 20), bg="green", fg="black")
tank2Text.pack()

tank3Text = Label(tank3Canvas, text="Tank3", font=("Arial", 20), bg="yellow", fg="black")
tank3Text.pack()
"""

# Display Frame

main.pack()

# Display window

game.mainloop()