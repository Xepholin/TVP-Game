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