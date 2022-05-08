from draw import *
from system import *

from tkinter import messagebox

def open_valve(valve):
	'''
	Puts the valve in open state

			Parameters:
				valve (Valve) : A Valve object
	'''

	if (isinstance(valve, Valve)):
		valve.set_state(1)
	else:
		raise TypeError("Type of valve should be Valve, got {}".format(type(valve)))

def close_valve(valve):
	'''
	Puts the valve in closed state

			Parameters:
				valve (Valve) : A Valve object
	'''
	if (isinstance(valve, Valve)):
		valve.set_state(0)
	else:
		raise TypeError("Type of valve should be Valve, got {}".format(type(valve)))

def find_valve(simulation, valveName):
	'''
	Searches for a valve for a given name

			Parameters:
					simulation (Simulation) : A Simulation object
					valveName (str) : A String

			Return:
					A Valve object
	'''

	if (valveName == "T12"):
		return simulation.valveT12
	elif (valveName == "T23"):
		return simulation.valveT23
	elif (valveName == "13"):
		return simulation.valve13
	elif (valveName == "12"):
		return simulation.valve12
	elif (valveName == "23"):
		return simulation.valve23
	else:
		raise ValueError("Valve name incorrect !")

def update_powered_motor(simulation, valveName, state):
	'''
	Update the new tanks that powered the motor and change the text

		Parameters:
				simulation (Simulation) : A Simulation object
				valveName (str) : A String
				state (int) : A Integer, to see if the valve is opening or closing, value = 0 or 1 -> 0 = closing / 1 = opening
	'''
	
	if (state == 1):
		if (valveName == "12"):
			simulation.motor1.add_tank("T2")
			simulation.motor2.add_tank("T1")

			write_motor_tanks(simulation.motor1.canvas, simulation.motor1.powered)
			write_motor_tanks(simulation.motor2.canvas, simulation.motor2.powered)
		elif (valveName == "23"):
			simulation.motor2.add_tank("T3")
			simulation.motor3.add_tank("T2")

			write_motor_tanks(simulation.motor2.canvas, simulation.motor2.powered)
			write_motor_tanks(simulation.motor3.canvas, simulation.motor3.powered)
		elif (valveName == "13"):
			simulation.motor1.add_tank("T3")
			simulation.motor3.add_tank("T1")

			write_motor_tanks(simulation.motor1.canvas, simulation.motor1.powered)
			write_motor_tanks(simulation.motor3.canvas, simulation.motor3.powered)
		else:
			raise ValueError("Valve name incorrect !")
	elif (state == 0):
		if (valveName == "12"):
			simulation.motor1.remove_tank("T2")
			simulation.motor2.remove_tank("T1")

			write_motor_tanks(simulation.motor1.canvas, simulation.motor1.powered)
			write_motor_tanks(simulation.motor2.canvas, simulation.motor2.powered)
		elif (valveName == "23"):
			simulation.motor2.remove_tank("T3")
			simulation.motor3.remove_tank("T2")

			write_motor_tanks(simulation.motor2.canvas, simulation.motor2.powered)
			write_motor_tanks(simulation.motor3.canvas, simulation.motor3.powered)
		elif (valveName == "13"):
			simulation.motor1.remove_tank("T3")
			simulation.motor3.remove_tank("T1")

			write_motor_tanks(simulation.motor1.canvas, simulation.motor1.powered)
			write_motor_tanks(simulation.motor3.canvas, simulation.motor3.powered)
		else:
			raise ValueError("Valve name incorrect !")
	else:
		raise ValueError("State value should be 0 or 1, got {}".format(state))

def interact_valve(canvas, simulation, valveName):
	'''
	Puts the valve in closed state

		Parameters:
				canvas (Canvas) : A Canvas object, canvas possessing the valve
				simulation (Simulation) : A Simulation object
				valveName (str) : A String
	'''

	valve = find_valve(simulation, valveName)

	if (valve.get_state() == 0):
		
		if (valveName != "T12" and valveName != "T23"):
			update_powered_motor(simulation, valveName, 1)
			
			if (simulation.tank1.state == 0 or simulation.tank2.state == 0 or simulation.tank3.state == 0):
				if (simulation.tank1.first_pump.get_state() == 1 and simulation.tank1.second_pump.get_state() == 1):
					if (simulation.tank2.first_pump.get_state() == 1 and simulation.tank2.second_pump.get_state() == 1):
						if (simulation.tank3.first_pump.get_state() == 1 and simulation.tank3.second_pump.get_state() == 1):
							messagebox.showwarning("Warning", "A tank is empty: priority to closing a valve to rebalance the fuel level in the tanks")
		else:
			if (valveName == "T12"):
				average = int((simulation.tank1.quantity + simulation.tank2.quantity) / 2)
				not_empty_tank(simulation, "T12", average)
			elif (valveName == "T23"):
				average = int((simulation.tank2.quantity + simulation.tank3.quantity) / 2)
				not_empty_tank(simulation, "T23", average)

		open_valve(valve)
		draw_valve_horizon(canvas, valve.id)
	else:
		if (valveName != "T12" and valveName != "T23"):
			update_powered_motor(simulation, valveName, 0)

			if (simulation.tank1.state == 0 or simulation.tank2.state == 0 or simulation.tank3.state == 0):
				if (simulation.tank1.first_pump.get_state() == 1 and simulation.tank1.second_pump.get_state() == 1):
					if (simulation.tank2.first_pump.get_state() == 1 and simulation.tank2.second_pump.get_state() == 1):
						if (simulation.tank3.first_pump.get_state() == 1 and simulation.tank3.second_pump.get_state() == 1):
							messagebox.showwarning("Warning", "A tank is empty: priority to closing a valve to rebalance the fuel level in the tanks")
		close_valve(valve)
		draw_valve_vertical(canvas, valve.id)

def start_pump(pump):
	'''
	Puts the pump in worked state

			Parameters:
					pump (Pump) : A Pump object
	'''
	
	if (isinstance(pump, Pump)):
		pump.set_state(1)
	else:
		raise TypeError("Pump should be Pump, got {}".format(type(pump)))


def stop_pump(pump):
	'''
	Puts the pump in stopped state

			Parameters:
					pump (Pump) : A Pump object
	'''
	
	if (isinstance(pump, Pump)):
		pump.set_state(0)
	else:
		raise TypeError("Pump should be Pump, got {}".format(type(pump)))

def find_tank(simulation, tankNum):
	'''
	Searches for a tank for a given number

			Parameters:
					simulation (Simulation) : A Simulation object
					tankNum (str) : A String

			Return:
					A Tank object
	'''

	if (tankNum == "1"):
		return simulation.tank1
	elif (tankNum == "2"):
		return simulation.tank2
	elif (tankNum == "3"):
		return simulation.tank3
	else:
		raise ValueError("Tank number incorrect !")

def interact_pump(canvas, simulation, tankNum):
	'''
	Puts the pump in stopped state, if the pump is broken, display a message box

			Parameters:
					canvas (Canvas) : A Canvas object, canvas possessing the tank
					simulation (Simulation) : A Simulation object
					tankNum (str) : A String
	'''
	
	tank = find_tank(simulation, tankNum)

	if (tank.second_pump.get_state() == 0):
		if (simulation.tank1.state == 0 or simulation.tank2.state == 0 or simulation.tank3.state == 0):
			messagebox.showwarning("Warning", "A tank is empty: priority to closing a valve to rebalance the fuel level in the tanks")
		start_pump(tank.second_pump)
		draw_pump_start(canvas, tank.second_pump.id)
	elif (tank.second_pump.get_state() == 1):
		if (simulation.tank1.state == 0 or simulation.tank2.state == 0 or simulation.tank3.state == 0):
			messagebox.showwarning("Warning", "A tank is empty: priority to closing a valve to rebalance the fuel level in the tanks")
		stop_pump(tank.second_pump)
		draw_pump_stop(canvas, tank.second_pump.id)
	else:
		messagebox.showwarning("Warning", "The pump is broken !")

	if (tank.second_pump.get_state() == -1) and (tank.first_pump.get_state() == -1):
		messagebox.showwarning("Warning", "The two tank pumps are broken, turn on a standby pump from another tank and open a valve to powered all motors")
		if simulation.tank1.secund_pump.get_state() == 0:
			start_pump(simulation.tank1.second_pump)
			if tankNum == 2:
				open_valve(simulation,"V12")
			if tankNum == 3:
				open_valve(simulation,"V13")
		elif simulation.tank2.secund_pump.get_state() == 0:
			start_pump(simulation.tank2.second_pump)
			if tankNum == 1:
				open_valve(simulation,"V12")
			if tankNum == 3:
				open_valve(simulation,"V23")
		elif simulation.tank3.secund_pump.get_state() == 0:
			start_pump(simulation.tank3.second_pump)
			if tankNum == 1:
				open_valve(simulation,"V13")
			if tankNum == 2:
				open_valve(simulation,"V23")


def broke_first_pump(tank):
	'''
	Puts the first pump in broken state

			Parameters:
					tank (Tank) : A Tank object
	'''

	
	tank.first_pump.set_state(-1)
	draw_broken_first_pump(tank.canvas)

def broke_second_pump(tank):
	'''
	Puts the second pump in broken state

			Parameters:
					tank (Tank) : A Tank object
	'''

	tank.second_pump.set_state(-1)
	draw_broken_second_pump(tank.canvas)


def empty_tank(simulation, tankNum):
	'''
	Puts the tank in empty state

			Parameters:
					simulation (Simulation) : A Simulation object
					tankNum (str) : A String
	'''

	if (tankNum == "1"):
		if (simulation.valveT12.get_state() == 0):
			tank = find_tank(simulation, tankNum)

			tank.set_state(0)
			tank.set_quantity(0)
			draw_empty_tank(tank)
		else:
			messagebox.showerror("Error", "The valves connected to the tank must be closed")
	elif (tankNum == "2"):
		if (simulation.valveT12.get_state() == 0 and simulation.valveT23.get_state() == 0):
			tank = find_tank(simulation, tankNum)

			tank.set_state(0)
			tank.set_quantity(0)
			draw_empty_tank(tank)
		else:
			messagebox.showerror("Error", "The valves connected to the tank must be closed")
	elif (tankNum == "3"):
		if (simulation.valveT23.get_state() == 0):
			tank = find_tank(simulation, tankNum)

			tank.set_state(0)
			tank.set_quantity(0)
			draw_empty_tank(tank)
		else:
			messagebox.showerror("Error", "The valves connected to the tank must be closed")
	else:
		raise ValueError("Tank number incorrect !")

def not_empty_tank(simulation, valveName, new_quantity):
	'''
	Puts the tank in not empty state and set the new quantity of the tank

			Parameters:
					canvas (Canvas) : A Canvas object, canvas possessing the tank
					simulation (Simulation) : A Simulation object
					valveName (str) : A String
					new_quantity (int) : A Integer

	'''

	if (valveName == "T12"):
		if (simulation.tank1.get_quantity() == 0):	
			simulation.tank1.set_state(1)
			draw_not_empty_tank(simulation.tank1.canvas, simulation.tank1, simulation.tank1.color)
		elif (simulation.tank2.get_quantity() == 0):
			simulation.tank2.set_state(1)
			draw_not_empty_tank(simulation.tank2.canvas, simulation.tank2, simulation.tank2.color)

		simulation.tank1.set_quantity(new_quantity)
		simulation.tank2.set_quantity(new_quantity)

		simulation.tank1.canvas.itemconfig("text", text="{}".format(simulation.tank1.quantity))
		simulation.tank2.canvas.itemconfig("text", text="{}".format(simulation.tank2.quantity))
	elif (valveName == "T23"):
		if (simulation.tank2.get_quantity() == 0):	
			simulation.tank2.set_state(1)
			draw_not_empty_tank(simulation.tank2.canvas, simulation.tank2, simulation.tank2.color)
		elif (simulation.tank3.get_quantity() == 0):
			simulation.tank3.set_state(1)
			draw_not_empty_tank(simulation.tank3.canvas, simulation.tank3, simulation.tank3.color)

		simulation.tank2.set_quantity(new_quantity)
		simulation.tank3.set_quantity(new_quantity)

		simulation.tank2.canvas.itemconfig("text", text="{}".format(simulation.tank2.quantity))
		simulation.tank3.canvas.itemconfig("text", text="{}".format(simulation.tank3.quantity))