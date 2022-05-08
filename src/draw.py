from system import *

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

def draw_empty_tank(tank):
	'''
	Draw a empty tank by changing the background color to red

			Parameters:
				tank (Tank) : A Tank object
	'''

	tank.canvas.itemconfig(tank.id, fill="red")
	tank.canvas.itemconfig("text", text="{}".format(tank.quantity))

def draw_not_empty_tank(canvas, tank, color):
    '''
	Draw a not empty tank by changing the background color to the tank color

			Parameters:
                canvas (Canvas) : A Canvas object, canvas possessing the tank
                tank (Tank) : A Tank object
				color (str) : A String
	'''

    canvas.itemconfig(tank.id, fill=color)

def write_motor_tanks(canvas, tank_list):
	'''
	Write the new tanks that powered the motor

			Parameters:
                canvas (Canvas) : A Canvas object, canvas possessing the tank
                tank_list (list) : A list
	'''

	if (isinstance(tank_list, list)):
		temp = ""

		for tank in tank_list:
			temp += tank + '\n'

		if (isinstance(canvas, Canvas)):
			canvas.itemconfig("text", text=temp)
		else:
			raise TypeError("Canvas should be Canvas, got {}".format(type(canvas)))
	else:
		raise TypeError("Tank list should be list, got {}".format(type(tank_list)))

def write_player_score(player):
	'''
	Write the new player's score

			Parameters:
                player (Player) : A Player object
	'''

	player.scoreCanvas.itemconfig("text", text="Previous Score : {}\nScore : {}".format(player.max_score, player.score))
