from turtle import width


def draw_valve_horizon(canvas, valve):
    '''
	Draw an open valve by drawing a horizontal line

			Parameters:
                canvas (Canvas) : A Canvas object, canvas possessing the valve
				valve (Valve) : A Valve object
	'''

    canvas.coords(valve, 8, 70, 68, 70)

def draw_valve_vertical(canvas, valve):
    '''
	Draw an closed valve by drawing a vertical line

			Parameters:
                canvas (Canvas) : A Canvas object, canvas possessing the valve
				valve (Valve) : A Valve object
	'''

    canvas.coords(valve, 37, 40, 37, 99)

def draw_pump_start(canvas, pump):
    '''
	Draw a working pump by changing the background color to blue

			Parameters:
                canvas (Canvas) : A Canvas object, canvas possessing the pump
				pump (Pump) : A Pump object
	'''

    canvas.itemconfig(pump, fill="blue")

def draw_pump_stop(canvas, pump):
    '''
	Draw a working pump by changing the background color to red

			Parameters:
                canvas (Canvas) : A Canvas object, canvas possessing the pump
				pump (Pump) : A Pump object
	'''

    canvas.itemconfig(pump, fill="red")

def draw_broken_first_pump(canvas):
    '''
	Draw a broken first pump by adding a cross over it

			Parameters:
                canvas (Canvas) : A Canvas object, canvas possessing the pump
	'''
    
    canvas.create_line(30, 90, 70, 130, width=5)
    canvas.create_line(70, 90, 30, 130, width=5)

def draw_broken_second_pump(canvas):
    '''
	Draw a broken second pump by adding a cross over it

			Parameters:
                canvas (Canvas) : A Canvas object, canvas possessing the pump
	'''

    canvas.create_line(80, 90, 120, 130, width=5)
    canvas.create_line(120, 90, 80, 130, width=5)

def draw_empty_tank(canvas, tank):
    '''
	Draw a empty tank by changing the background color to red

			Parameters:
                canvas (Canvas) : A Canvas object, canvas possessing the tank
                tank (Tank) : A Tank object
	'''

    canvas.itemconfig(tank, fill="red")

