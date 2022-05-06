from system import *
from playerCommands import *

from tkinter import *

# create window

game = Tk()

# Custom window

game.title("TVP Game")
game.geometry("1280x100")
game.minsize(1280, 1000)

# Frame

system = Frame(game)
button = Frame(game, bg="black")
subButton = Frame(button, bg="black")
subSubButton = Frame(button, bg="black")

# Canvas

# Tanks

tank1Canvas = Canvas(system, bg="black", bd=1, width=140, height=140)
temp = tank1Canvas.create_rectangle(0, 0, 150, 150, fill="orange")
tank1Canvas.create_text(75, 60, text="Tank1", font=("Arial", 15), fill="black")
pump11 = Pump(tank1Canvas.create_oval(30, 90, 70, 130, fill="blue"))
tank1Canvas.create_text(50, 110, text="p11", font=("Arial", 11), fill="white")
pump12 = Pump(tank1Canvas.create_oval(80, 90, 120, 130, fill="blue"))
tank1Canvas.create_text(100, 110, text="p12", font=("Arial", 11), fill="white")
tank1Canvas.grid(row=0, column=1)

tank1 = Tank(temp, pump11, pump12, 100)

tank2Canvas = Canvas(system, bg="black", bd=1, width=140, height=140)
temp = tank2Canvas.create_rectangle(0, 0, 150, 150, fill="green")
tank2Canvas.create_text(75, 60, text="Tank2", font=("Arial", 15), fill="black")
pump21 = Pump(tank2Canvas.create_oval(30, 90, 70, 130, fill="blue"))
tank2Canvas.create_text(50, 110, text="p21", font=("Arial", 11), fill="white")
pump22 = Pump(tank2Canvas.create_oval(80, 90, 120, 130, fill="blue"))
tank2Canvas.create_text(100, 110, text="p22", font=("Arial", 11), fill="white")
tank2Canvas.grid(row=0, column=5)

tank2 = Tank(temp, pump21, pump22, 50)

tank3Canvas = Canvas(system, bg="black", bd=1, width=140, height=140)
temp = tank3Canvas.create_rectangle(0, 0, 150, 150, fill="yellow")
tank3Canvas.create_text(75, 60, text="Tank3", font=("Arial", 15), fill="black")
pump31 = Pump(tank3Canvas.create_oval(30, 90, 70, 130, fill="blue"))
tank3Canvas.create_text(50, 110, text="p31", font=("Arial", 11), fill="white")
pump32 = Pump(tank3Canvas.create_oval(80, 90, 120, 130, fill="blue"))
tank3Canvas.create_text(100, 110, text="p32", font=("Arial", 11), fill="white")
tank3Canvas.grid(row=0, column=9)

tank3 = Tank(temp, pump31, pump32, 100)

# Valves

valveT12Canvas = Canvas(system, width=70, height=140)
valveT12Canvas.create_oval(5, 37, 70, 102, fill="black")
valveT12 = Valve(valveT12Canvas.create_line(37, 40, 37, 99, fill="white", width=5))
valveT12Canvas.create_text(37, 20, text="VT12", font=("Arial", 15), fill="black")
valveT12Canvas.grid(row=0, column=3)

valveT23Canvas = Canvas(system, width=70, height=140)
valveT23Canvas.create_oval(5, 37, 70, 102, fill="black")
valveT23 = Valve(valveT23Canvas.create_line(37, 40, 37, 99, fill="white", width=5))
valveT23Canvas.create_text(37, 20, text="VT23", font=("Arial", 15), fill="black")
valveT23Canvas.grid(row=0, column=7)

valve12Canvas = Canvas(system, width=70, height=140)
valve12Canvas.create_oval(5, 37, 70, 102, fill="black")
valve12 = Valve(valve12Canvas.create_line(37, 40, 37, 99, fill="white", width=5))
valve12Canvas.create_text(37, 20, text="V12", font=("Arial", 15), fill="black")
valve12Canvas.grid(row=1, column=3)

valve23Canvas = Canvas(system, width=70, height=140)
valve23Canvas.create_oval(5, 37, 70, 102, fill="black")
valve23 = Valve(valve23Canvas.create_line(37, 40, 37, 99, fill="white", width=5))
valve23Canvas.create_text(37, 20, text="V23", font=("Arial", 15), fill="black")
valve23Canvas.grid(row=2, column=7)

valve13Canvas = Canvas(system, width=70, height=140)
valve13Canvas.create_oval(5, 37, 70, 102, fill="black")
valve13 = Valve(valve13Canvas.create_line(37, 40, 37, 99, fill="white", width=5))
valve13Canvas.create_text(37, 20, text="V13", font=("Arial", 15), fill="black")
valve13Canvas.grid(row=4, column=3)

# Pipes

pipe = Canvas(system, width=70, height=70)
pipe.create_line(0, 35, 70, 35, width=5)
pipe.grid(row=0, column=2)

pipe = Canvas(system, width=70, height=70)
pipe.create_line(0, 35, 70, 35, width=5)
pipe.grid(row=0, column=4)

pipe = Canvas(system, width=70, height=70)
pipe.create_line(0, 35, 70, 35, width=5)
pipe.grid(row=0, column=6)

pipe = Canvas(system, width=70, height=70)
pipe.create_line(0, 35, 70, 35, width=5)
pipe.grid(row=0, column=8)

pipe = Canvas(system, width=140, height=140)
pipe.create_line(70, 0, 70, 140, width=5)
pipe.create_line(70, 70, 140, 70, width=5)
pipe.grid(row=1, column=1)

pipe = Canvas(system, width=140, height=140)
pipe.create_line(70, 0, 70, 140, width=5)
pipe.create_line(70, 70, 0, 70, width=5)
pipe.grid(row=2, column=1)

pipe = Canvas(system, width=140, height=140)
pipe.create_line(70, 0, 70, 140, width=5)
pipe.create_line(0, 70, 70, 70, width=5)
pipe.grid(row=1, column=5)

pipe = Canvas(system, width=140, height=140)
pipe.create_line(70, 0, 70, 140, width=5)
pipe.create_line(70, 70, 140, 70, width=5)
pipe.grid(row=2, column=5)

pipe = Canvas(system, width=140, height=140)
pipe.create_line(70, 0, 70, 140, width=5)
pipe.create_line(70, 70, 140, 70, width=5)
pipe.grid(row=1, column=9)

pipe = Canvas(system, width=140, height=140)
pipe.create_line(70, 0, 70, 140, width=5)
pipe.create_line(70, 70, 0, 70, width=5)
pipe.grid(row=2, column=9)

pipe = Canvas(system, width=70, height=140)
pipe.create_line(0, 70, 70, 70, width=5)
pipe.grid(row=1, column=2)

pipe = Canvas(system, width=70, height=140)
pipe.create_line(0, 70, 70, 70, width=5)
pipe.grid(row=1, column=4)

pipe = Canvas(system, width=70, height=140)
pipe.create_line(0, 70, 70, 70, width=5)
pipe.grid(row=2, column=6)

pipe = Canvas(system, width=70, height=140)
pipe.create_line(0, 70, 70, 70, width=5)
pipe.grid(row=2, column=8)

pipe = Canvas(system, width=140, height=140)
pipe.create_line(0, 70, 70, 70, width=5)
pipe.create_line(70, 70, 70, 140, width=5)
pipe.grid(row=1, column=10)

pipe = Canvas(system, width=140, height=140)
pipe.create_line(70, 0, 70, 140, width=5)
pipe.grid(row=2, column=10)

pipe = Canvas(system, width=140, height=140)
pipe.create_line(70, 0, 70, 140, width=5)
pipe.grid(row=3, column=10)

pipe = Canvas(system, width=140, height=140)
pipe.create_line(70, 0, 70, 70, width=5)
pipe.create_line(70, 70, 0, 70, width=5)
pipe.grid(row=4, column=10)

pipe = Canvas(system, width=140, height=140)
pipe.create_line(0, 70, 140, 70, width=5)
pipe.grid(row=4, column=9)

pipe = Canvas(system, width=70, height=140)
pipe.create_line(0, 70, 70, 70, width=5)
pipe.grid(row=4, column=8)

pipe = Canvas(system, width=70, height=140)
pipe.create_line(0, 70, 70, 70, width=5)
pipe.grid(row=4, column=7)

pipe = Canvas(system, width=70, height=140)
pipe.create_line(0, 70, 70, 70, width=5)
pipe.grid(row=4, column=6)

pipe = Canvas(system, width=140, height=140)
pipe.create_line(0, 70, 140, 70, width=5)
pipe.grid(row=4, column=5)

pipe = Canvas(system, width=70, height=140)
pipe.create_line(0, 70, 70, 70, width=5)
pipe.grid(row=4, column=4)

pipe = Canvas(system, width=70, height=140)
pipe.create_line(0, 70, 70, 70, width=5)
pipe.grid(row=4, column=2)

pipe = Canvas(system, width=140, height=140)
pipe.create_line(0, 70, 140, 70, width=5)
pipe.grid(row=4, column=1)

pipe = Canvas(system, width=140, height=140)
pipe.create_line(140, 70, 70, 70, width=5)
pipe.create_line(70, 70, 70, 0, width=5)
pipe.grid(row=4, column=0)

pipe = Canvas(system, width=140, height=140)
pipe.create_line(70, 0, 70, 140, width=5)
pipe.grid(row=3, column=0)

pipe = Canvas(system, width=140, height=140)
pipe.create_line(70, 140, 70, 70, width=5)
pipe.create_line(70, 70, 140, 70, width=5)
pipe.grid(row=2, column=0)


# Motors

motor1 = Canvas(system, bg="grey", bd=1, width=70, height=140)
motor1.create_rectangle(0,0, 150, 150, fill="grey")
motor1.create_text(35, 70, text="M1", font=("Arial", 15), fill="black")
motor1.grid(row=3, column=1)

motor2 = Canvas(system, bg="grey", bd=1, width=70, height=140)
motor2.create_rectangle(0,0, 150, 150, fill="grey")
motor2.create_text(35, 70, text="M2", font=("Arial", 15), fill="black")
motor2.grid(row=3, column=5)

motor3 = Canvas(system, bg="grey", bd=1, width=70, height=140)
motor3.create_rectangle(0,0, 150, 150, fill="grey")
motor3.create_text(35, 70, text="M3", font=("Arial", 15), fill="black")
motor3.grid(row=3, column=9)

# Button

valveT12ButtonBorder = Frame(subButton, highlightbackground="white", highlightthickness=2, bd=0)
valveT12Button = Button(valveT12ButtonBorder, text="VT12", font=("Arial, 25"), width=5, height=1, bg="black", bd=1, fg="white", command= lambda: interact_valve(valveT12Canvas, valveT12))
valveT12ButtonBorder.grid(row=0, column=1, padx=30, pady=10)
valveT12Button.pack()

valveT23ButtonBorder = Frame(subButton, highlightbackground="white", highlightthickness=2, bd=0)
valveT23Button = Button(valveT23ButtonBorder, text="VT23", font=("Arial, 25"), width=5, height=1, bg="black", bd=1, fg="white", command= lambda: interact_valve(valveT23Canvas, valveT23))
valveT23ButtonBorder.grid(row=0, column=2, padx=30,pady=10)
valveT23Button.pack()

pump12ButtonBorder = Frame(subSubButton, highlightbackground="white", highlightthickness=2, bd=0)
pump12Button = Button(pump12ButtonBorder, text="P12", font=("Arial, 25"), width=5, height=1, bg="black", bd=1, fg="white", command= lambda: interact_pump(tank1Canvas, tank1))
pump12ButtonBorder.grid(row=0, column=1, padx=30,pady=10)
pump12Button.pack()

pump22ButtonBorder = Frame(subSubButton, highlightbackground="white", highlightthickness=2, bd=0)
pump22Button = Button(pump22ButtonBorder, text="P22", font=("Arial, 25"), width=5, height=1, bg="black", bd=1, fg="white", command= lambda: interact_pump(tank2Canvas, tank2))
pump22ButtonBorder.grid(row=0, column=2, padx=30,pady=10)
pump22Button.pack()

pump32ButtonBorder = Frame(subSubButton, highlightbackground="white", highlightthickness=2, bd=0)
pump32Button = Button(pump32ButtonBorder, text="P32", font=("Arial, 25"), width=5, height=1, bg="black", bd=1, fg="white", command= lambda: interact_pump(tank3Canvas, tank3))
pump32ButtonBorder.grid(row=0, column=3, padx=30,pady=10)
pump32Button.pack()

valve12ButtonBorder = Frame(subSubButton, highlightbackground="white", highlightthickness=2, bd=0)
valve12Button = Button(valve12ButtonBorder, text="V12", font=("Arial, 25"), width=5, height=1, bg="black", bd=1, fg="white", command= lambda: interact_valve(valve12Canvas, valve12))
valve12ButtonBorder.grid(row=1, column=1, padx=30,pady=10)
valve12Button.pack()

valve13ButtonBorder = Frame(subSubButton, highlightbackground="white", highlightthickness=2, bd=0)
valve13Button = Button(valve13ButtonBorder, text="V13", font=("Arial, 25"), width=5, height=1, bg="black", bd=1, fg="white", command= lambda: interact_valve(valve13Canvas, valve13))
valve13ButtonBorder.grid(row=1, column=2, padx=30,pady=10)
valve13Button.pack()

valve23ButtonBorder = Frame(subSubButton, highlightbackground="white", highlightthickness=2, bd=0)
valve23Button = Button(valve23ButtonBorder, text="V23", font=("Arial, 25"), width=5, height=1, bg="black", bd=1, fg="white", command= lambda: interact_valve(valve23Canvas, valve23))
valve23ButtonBorder.grid(row=1, column=3, padx=30,pady=10)
valve23Button.pack()

# Display Frame

system.pack()
button.pack(side=BOTTOM, fill=BOTH)
subButton.pack()
subSubButton.pack()

# Display window

game.mainloop()