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

system = Frame(game)
button = Frame(game, bg="black")
subButton = Frame(button, bg="black")
subSubButton = Frame(button, bg="black")

# Canvas

tank1Canvas = Canvas(system, bg="black", bd=1, width=140, height=140)
temp = tank1Canvas.create_rectangle(0, 0, 150, 150, fill="orange")
tank1Canvas.create_text(75, 60, text="Tank1", font=("Arial", 15), fill="black")
pump11 = Pump(tank1Canvas.create_oval(30, 90, 70, 130, fill="blue"))
tank1Canvas.create_text(50, 110, text="p11", font=("Arial", 11), fill="white")
pump12 = Pump(tank1Canvas.create_oval(80, 90, 120, 130, fill="blue"))
tank1Canvas.create_text(100, 110, text="p12", font=("Arial", 11), fill="white")
tank1Canvas.grid(row=0, column=0)

tank1 = Tank(temp, pump11, pump12, 100)

pipe1 = Canvas(system, width=70, height=70)
pipe1.create_line(0, 35, 70, 35)
pipe1.grid(row=0, column=1)

valveT12Canvas = Canvas(system, width=70, height=140)
valveT12Canvas.create_oval(5, 37, 70, 102, fill="black")
valveT12 = Valve(valveT12Canvas.create_line(37, 40, 37, 99, fill="white", width=5))
valveT12Canvas.create_text(37, 20, text="VT12", font=("Arial", 15), fill="black")
valveT12Canvas.grid(row=0, column=2)

pipe2 = Canvas(system, width=70, height=70)
pipe2.create_line(0, 35, 70, 35)
pipe2.grid(row=0, column=3)

tank2Canvas = Canvas(system, bg="black", bd=1, width=140, height=140)
temp = tank2Canvas.create_rectangle(0, 0, 150, 150, fill="green")
tank2Canvas.create_text(75, 60, text="Tank2", font=("Arial", 15), fill="black")
pump21 = Pump(tank2Canvas.create_oval(30, 90, 70, 130, fill="blue"))
tank2Canvas.create_text(50, 110, text="p21", font=("Arial", 11), fill="white")
pump22 = Pump(tank2Canvas.create_oval(80, 90, 120, 130, fill="blue"))
tank2Canvas.create_text(100, 110, text="p22", font=("Arial", 11), fill="white")
tank2Canvas.grid(row=0, column=4)

tank2 = Tank(temp, pump21, pump22, 50)

pipe3 = Canvas(system, width=70, height=70)
pipe3.create_line(0, 35, 70, 35)
pipe3.grid(row=0, column=5)

valveT23Canvas = Canvas(system, width=70, height=140)
valveT23Canvas.create_oval(5, 37, 70, 102, fill="black")
valveT23 = Valve(valveT23Canvas.create_line(37, 40, 37, 99, fill="white", width=5))
valveT23Canvas.create_text(37, 20, text="VT23", font=("Arial", 15), fill="black")
valveT23Canvas.grid(row=0, column=6)

pipe4 = Canvas(system, width=70, height=70)
pipe4.create_line(0, 35, 70, 35)
pipe4.grid(row=0, column=7)

tank3Canvas = Canvas(system, bg="black", bd=1, width=140, height=140)
temp = tank3Canvas.create_rectangle(0, 0, 150, 150, fill="yellow")
tank3Canvas.create_text(75, 60, text="Tank3", font=("Arial", 15), fill="black")
pump31 = Pump(tank3Canvas.create_oval(30, 90, 70, 130, fill="blue"))
tank3Canvas.create_text(50, 110, text="p31", font=("Arial", 11), fill="white")
pump32 = Pump(tank3Canvas.create_oval(80, 90, 120, 130, fill="blue"))
tank3Canvas.create_text(100, 110, text="p32", font=("Arial", 11), fill="white")
tank3Canvas.grid(row=0, column=8)

tank3 = Tank(temp, pump31, pump32, 100)


# Button

valveT12ButtonBorder = Frame(subButton, highlightbackground="white", highlightthickness=2, bd=0)
valveT12Button = Button(valveT12ButtonBorder, text="VT12", font=("Arial, 25"), width=5, height=1, bg="black", bd=1, fg="white", command= lambda: interact_valve(valveT12Canvas, valveT12))
valveT12ButtonBorder.grid(row=0, column=0, padx=60, pady=10)
valveT12Button.pack()

valveT23ButtonBorder = Frame(subButton, highlightbackground="white", highlightthickness=2, bd=0)
valveT23Button = Button(valveT23ButtonBorder, text="VT23", font=("Arial, 25"), width=5, height=1, bg="black", bd=1, fg="white", command= lambda: interact_valve(valveT23Canvas, valveT23))
valveT23ButtonBorder.grid(row=0, column=1, padx=20,pady=10)
valveT23Button.pack()

pump12ButtonBorder = Frame(subSubButton, highlightbackground="white", highlightthickness=2, bd=0)
pump12Button = Button(pump12ButtonBorder, text="P12", font=("Arial, 25"), width=5, height=1, bg="black", bd=1, fg="white", command= lambda: interact_pump(tank1Canvas, tank1))
pump12ButtonBorder.grid(row=0, column=0, padx=40,pady=10)
pump12Button.pack()

pump22ButtonBorder = Frame(subSubButton, highlightbackground="white", highlightthickness=2, bd=0)
pump22Button = Button(pump22ButtonBorder, text="P22", font=("Arial, 25"), width=5, height=1, bg="black", bd=1, fg="white", command= lambda: interact_pump(tank2Canvas, tank2))
pump22ButtonBorder.grid(row=0, column=1, padx=20,pady=10)
pump22Button.pack()

pump32ButtonBorder = Frame(subSubButton, highlightbackground="white", highlightthickness=2, bd=0)
pump32Button = Button(pump32ButtonBorder, text="P32", font=("Arial, 25"), width=5, height=1, bg="black", bd=1, fg="white", command= lambda: interact_pump(tank3Canvas, tank3))
pump32ButtonBorder.grid(row=0, column=2, padx=20,pady=10)
pump32Button.pack()

valve12ButtonBorder = Frame(subSubButton, highlightbackground="white", highlightthickness=2, bd=0)
valve12Button = Button(valve12ButtonBorder, text="V12", font=("Arial, 25"), width=5, height=1, bg="black", bd=1, fg="white", command= lambda: interact_valve(valveT12))
valve12ButtonBorder.grid(row=1, column=0, padx=40,pady=10)
valve12Button.pack()

valve13ButtonBorder = Frame(subSubButton, highlightbackground="white", highlightthickness=2, bd=0)
valve13Button = Button(valve13ButtonBorder, text="V13", font=("Arial, 25"), width=5, height=1, bg="black", bd=1, fg="white", command= lambda: interact_valve(valveT12))
valve13ButtonBorder.grid(row=1, column=1, padx=20,pady=10)
valve13Button.pack()

valve23ButtonBorder = Frame(subSubButton, highlightbackground="white", highlightthickness=2, bd=0)
valve23Button = Button(valve23ButtonBorder, text="V23", font=("Arial, 25"), width=5, height=1, bg="black", bd=1, fg="white", command= lambda: interact_valve(valveT12))
valve23ButtonBorder.grid(row=1, column=2, padx=20,pady=10)
valve23Button.pack()

# Display Frame

system.pack()
button.pack(side=BOTTOM, fill=BOTH)
subButton.pack()
subSubButton.pack()

# Display window

game.mainloop()