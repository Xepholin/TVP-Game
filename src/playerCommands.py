from draw import *

from tkinter import messagebox

def open_valve(valve):
	'''
	Puts the valve in open state

			Parameters:
				valve (Valve) : A Valve object
	'''

	valve.set_state(1)

def close_valve(valve):
    '''
    Puts the valve in closed state

            Parameters:
				valve (Valve) : A Valve object
    '''

    valve.set_state(0)

def interact_valve(canvas, valve):
	'''
	Puts the valve in closed state

		Parameters:
				canvas (Canvas) : A Canvas object, canvas possessing the valve
				valve (Valve) : A Valve object
	'''

	if (valve.get_state() == 0):
		open_valve(valve)
		draw_valve_horizon(canvas, valve.id)
	else:
		close_valve(valve)
		draw_valve_vertical(canvas, valve.id)

def start_pump(pump):
    '''
    Puts the pump in worked state

            Parameters:
                    pump (Pump) : A Pump object
    '''

    pump.set_state(1)

def stop_pump(pump):
    '''
    Puts the pump in stopped state

            Parameters:
					pump (Pump) : A Pump object
    '''

    pump.set_state(0)

def interact_pump(canvas, tank):
	'''
	Puts the pump in stopped state, if the pump is broken, display a message box

			Parameters:
					canvas (Canvas) : A Canvas object, canvas possessing the tank
					tank (Tank) : A Tank object
	'''

	if (tank.second_pump.get_state() == 0):
		open_valve(tank.second_pump)
		draw_pump_start(canvas, tank.second_pump.id)
	elif (tank.second_pump.get_state() == 1):
		close_valve(tank.second_pump)
		draw_pump_stop(canvas, tank.second_pump.id)
	else:
		messagebox.showwarning("Warning", "The pump is broken !")


def broke_first_pump(canvas, pump):
	'''
	Puts the first pump in broken state

			Parameters:
					canvas (Canvas) : A Canvas object, canvas possessing the pump
					pump (Pump) : A Pump object
	'''

	pump.set_state(-1)
	draw_broken_first_pump(canvas)

def broke_second_pump(canvas, pump):
	'''
	Puts the second pump in broken state

			Parameters:
					canvas (Canvas) : A Canvas object, canvas possessing the pump
					pump (Pump) : A Pump object
	'''

	pump.set_state(-1)
	draw_broken_second_pump(canvas)


def empty_tank(canvas, tank):
	'''
	Puts the tank in empty state

			Parameters:
					canvas (Canvas) : A Canvas object, canvas possessing the tank
					tank (Tank) : A Tank object
	'''

	tank.set_state(0)
	draw_empty_tank(canvas, tank.id)