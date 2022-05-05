def draw_valve_horizon(canvas, valve):
    canvas.coords(valve, 8, 70, 68, 70)

def draw_valve_vertical(canvas, valve):
    canvas.coords(valve, 37, 40, 37, 99)

def draw_pump_start(canvas, pump):
    canvas.itemconfig(pump, fill="blue")

def draw_pump_stop(canvas, pump):
    canvas.itemconfig(pump, fill="red")

