from draw import *

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
				canvas (Canvas) : A Canvas object
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
	Puts the pump in stopped state

			Parameters:
					canvas (Canvas) : A Canvas object
					tank (Tank) : A Tank object
	'''

	if (tank.second_pump.get_state() == 0):
			open_valve(tank.second_pump)
			draw_pump_start(canvas, tank.second_pump.id)
	elif (tank.second_pump.get_state() == 1):
			close_valve(tank.second_pump)
			draw_pump_stop(canvas, tank.second_pump.id)

def broke_pump(pump):
    '''
    Puts the pump in broken state

            Parameters:
                    pump (Pump) : A Pump object
    '''

    pump.set_state(-1)

def empty_tank(tank):
    '''
    Puts the tank in empty state

            Parameters:
                    tank (Tank) : A Tank object
    '''

    tank.set_state(0)